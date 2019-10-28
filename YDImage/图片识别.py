import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
# text = pytesseract.image_to_string(Image.open(r'E:\客户数据\q\a\优单合同1.jpg'))
te = pytesseract.image_to_string(Image.open(r'E:\重庆商家入驻\2019.5.28\周豆花\店铺照片.jpg'))
# s = ['40x12', '40x60', '40x16', '60x80', '25x10']
# r = s in te
# print(r)
print(te)


