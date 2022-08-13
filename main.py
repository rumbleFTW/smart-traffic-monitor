from easyocr import Reader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cv2
import pandas as pd
import smtplib


CAMERA_LOCATION = 'New Town'

def sendMail(mail):
    message = MIMEMultipart("alternative")
    message["Subject"] = 'Notification regarding e-challan fine'
    message["From"] = mail
    message["To"] = mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    body = f'You were caught riding without helmet near {CAMERA_LOCATION}, and were fined Rupees 500. Please visit https://echallan.parivahan.gov.in/ to pay your due challan. If you are caught riding again without proper gear, you will be severely penalized.'

    message.attach(MIMEText(body, "plain"))
    server.login('smart.traffic.monitor@gmail.com', 'vimtcznlsxshqyrp')
    server.sendmail('smart.traffic.monitor@gmail.com', mail, message.as_string())
    server.quit()
  

database = pd.read_csv('traffic-two-wheeler-monitoring/database.csv')



img = cv2.imread('traffic-two-wheeler-monitoring/yolo/runs/detect/exp2/crops/Numberplate/IMG20220811133939.jpg')

reader = Reader(['de'])
number = reader.readtext(img)



licensePlate = ""

for i in [0, 1]:
  for item in number[i]:
    if type(item) == str:
      licensePlate += item

licensePlate = licensePlate.replace(' ', '')
print(f'Licence number is:', licensePlate)


for index, plate in enumerate(database['Registration']):
    if licensePlate == plate:
        database.at[index, 'Due challan'] += 500
        mail = database['Email'][index]
        sendMail(mail)
        print('Rider successfully notified!')
        database.to_csv('traffic-two-wheeler-monitoring/database.csv')