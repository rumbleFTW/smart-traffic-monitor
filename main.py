from easyocr import Reader
import cv2



database = {'WB08R2567': {'Name': 'Rajdeep Ghosh', 'Address': 'Kolkata', 'Phone': 8240336721},
            'JK04B8946': {'Name': 'Akash Kotal', 'Address': 'Midnapore', 'Phone': 9382795506}}



img = cv2.imread('./yolo/runs/detect/exp3/crops/Numberplate/test1.jpg')

reader = Reader(['de'])
number = reader.readtext(img)
number = 'JK04B8946'


phoneNum = database[number]['Phone']


print(f'Message sent to +91 {phoneNum}')




