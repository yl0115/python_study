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
            if result+'\\'+'营业执照.jpg' == result+'\\'+value:
                break
            else:
                if value.endswith('.jpg'):
                    if '营业执照' in value:
                        continue
                    old_name = result+'\\'+value
                    if '优单合同' in old_name:
                        print('合同不识别')
                    else:
                        te = pytesseract.image_to_string(Image.open(old_name))
                        new_name = result+'\\营业执照'+str(index)+'.jpg'
                        if '#' in te:
                            os.rename(old_name, new_name)
                            print(index)
                            index += 1


if __name__ == '__main__':
    path = r'E:\成都内江\1'
    r_list = os.listdir(path)
    for w in r_list:
        b = path+'\\'+w

        all_path(b)

