import cv2
print(cv2.__version__)

def upscale(impath):
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    image = cv2.imread(impath, cv2.IMREAD_GRAYSCALE)
    path = "traffic-two-wheeler-monitoring/FSRCNN-small_x3.pb"
    sr.readModel(path)
    sr.setModel("fsrcnn", 4)
    result = sr.upsample(image)
    e, result = cv2.threshold(result, 128, 255, cv2.THRESH_TOZERO)
    cv2.imwrite(impath.replace("1", "11"), result)


upscale("traffic-two-wheeler-monitoring/test/test1.png")


# from easyocr import Reader

# img = cv2.imread("traffic-two-wheeler-monitoring/test/test11.png")

# reader = Reader(['en'])
# number = reader.readtext(img)


# licensePlate = ""

# for i in [0, 1]:
#     for item in number[i]:
#         if type(item) == str:
#             licensePlate += item

# licensePlate = licensePlate.replace(' ', '')
# licensePlate = licensePlate.upper()
# print(f'License number is:', licensePlate)