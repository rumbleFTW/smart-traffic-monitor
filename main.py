from easyocr import Reader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cv2
import pandas as pd
import smtplib
import os
from twilio.rest import Client
import geocoder
import re

g = geocoder.ip('me')

CAMERA_LOCATION = g.json['address']+f'. [Lat: {g.lat}, Lng:{g.lng}]'

def sendSMS(number):

    TWILIO_ACCOUNT_SID = 'AC9a24f8d6a167aaa9f8e197b631e02c28'
    TWILIO_AUTH_TOKEN = '76131d4d4f15c1f9b181632db2b5eaef'


    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
            body=f'You were caught riding without helmet near {CAMERA_LOCATION}, and were fined Rupees 500. Please visit https://bit.ly/3QQxTRO to pay your due challan. If you are caught riding again without proper gear, you will be severely penalized.',
            from_='+19203455833',
            to=f'+{number}'
        )

    print(message.sid)

def sendMail(mail):
    message = MIMEMultipart("alternative")
    message["Subject"] = 'Notification regarding e-challan fine'
    message["From"] = mail
    message["To"] = mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    body = f'You were caught riding without helmet near {CAMERA_LOCATION}, and were fined Rupees 500. Please visit https://bit.ly/3QQxTRO to pay your due challan. If you are caught riding again without proper gear, you will be severely penalized.'

    message.attach(MIMEText(body, "plain"))
    server.login('smart.traffic.monitor@gmail.com', 'vimtcznlsxshqyrp')
    server.sendmail('smart.traffic.monitor@gmail.com', mail, message.as_string())
    server.quit()
  

database = pd.read_csv('database.csv')

BASE_DIR = 'yolo/runs/detect/exp/crops/No-helmet'


if __name__ == '__main__':

    warnedNums = []

    for path in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, path).replace('No-helmet', 'Numberplate')
        img = cv2.imread(path, 0)
        reader = Reader(['en'])
        number = reader.readtext(img, mag_ratio=3)
        licensePlate = ""

        for i in [0, 1]:
            for item in number[i]:
                if type(item) == str:
                    licensePlate += item

        licensePlate = licensePlate.replace(' ', '')
        licensePlate = licensePlate.upper()
        licensePlate = re.sub(r'[^a-zA-Z0-9]', '', licensePlate)
        print('License number is:', licensePlate)

        if licensePlate not in warnedNums:
            for index, plate in enumerate(database['Registration']):
                if licensePlate == plate:
                    database.at[index, 'Due challan'] += 500
                    mail = database['Email'][index]
                    num = database['Phone number'][index]
                    sendMail(mail)
                    sendSMS(num)
                    print(f"{database['Name'][index]} successfully notified!")
                    warnedNums.append(licensePlate)
                    database.to_csv('database.csv', index=False)