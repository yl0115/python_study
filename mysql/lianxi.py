# -*-coding:utf-8-*-
from xpinyin import Pinyin
from selenium import webdriver
from time import sleep
import os
from PIL import Image


class LianXi(object):
    def __init__(self):
        self.accept_next_alert = True
        self.p = Pinyin()

    def pinyin(self):
        """
        :return:
        """
        su = '命运赠送的东西'
        a = self.p.get_pinyin(su, splitter=' ')
        print(a)

    @staticmethod
    def selenium_chram():
        """
        selenium
        :return:
        """
        driver = webdriver.Chrome()
        driver.get(r'http://192.168.3.132:8081/youdan/index.html')
        driver.maximize_window()
        driver.find_element_by_link_text('卖家').click()
        driver.get(r'%s' % driver.current_url)
        html_source = driver.page_source
        with open('1.txt', 'w', encoding='utf-8') as f:
            f.write(html_source)

    @staticmethod
    def opencharm():
        driver = webdriver.Chrome()
        os.startfile(r'e:\getJSON\启动服务.bat')
        driver.get(r'http://localhost:8008/public/index.html')
        sleep(6)

    @staticmethod
    def update_image():
        abspath = os.path.dirname(os.path.abspath(__file__))
        abspath = abspath + '\\images'
        for i in os.listdir(abspath):
            im = Image.open(abspath+'\\'+i)
            width = im.size[0]
            height = im.size[1]
            a = im.resize((width//10, height//10))
            a.save(abspath+'\\'+i)


if __name__ == '__main__':
    lx = LianXi()
    # lx.pinyin()
    # lx.selenium_chram()
    lx.update_image()

