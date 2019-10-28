import os
import pytesseract
from PIL import Image


def all_path(dirname):
    result = os.listdir(dirname)
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR/tesseract.exe'
    index = 1
    for i in result:
        result = dirname+"\\"+i
        print(result)
        r = os.listdir(result)
        for value in r:
            if result+'\\'+'优单合同.jpg' == result+'\\'+value:
                break
            else:
                if value.endswith('.jpg'):
                    if '优单合同' in value:
                        continue
                    old_name = result+'\\'+value
                    te = pytesseract.image_to_string(Image.open(old_name))
                    new_name = result+'\\优单合同' + str(index) + '.jpg'
                    s = ['40x12', '40x60', '40x16', '60x80', '25x10', '50x70', '12x12', '60x12', '50x', '17.5']
                    for a in s:
                        if a in te:
                            os.rename(old_name, new_name)
                            print(index)
                            index += 1
                            break


if __name__ == '__main__':
    path = r'E:\成都内江\1'
    r_list = os.listdir(path)
    for w in r_list:
        b = path+'\\'+w
        all_path(b)
