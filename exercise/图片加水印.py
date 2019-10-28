# -*- coding:utf-8 -*-
import time
import socket
import re
import requests
import random
from bs4 import BeautifulSoup
from PIL import Image, ImageFont, ImageDraw


def get_ip():
    # 获取本机电脑名
    myname = socket.getfqdn(socket.gethostname())
    # 获取本机ip
    myaddr = socket.gethostbyname(myname)
    return myaddr
    # print(myaddr)
    # remote_host = 'www.baidu.com'
    # try:
    #     print("IP address: %s" % socket.gethostbyname(remote_host))
    # except socket.error as err_msg:
    #     print("%s:%s" % (remote_host, err_msg))

    pass


def queryIpAddress(ipaddress):
    reaponse = requests.get(r"https://ip.cn/index.php?ip={}".format(ipaddress), timeout=10)
    soup = BeautifulSoup(reaponse.content, 'lxml')
    a = soup.find('div', attrs={'class': 'well'})
    b = a.find_all('p')[3].text
    address = b.replace("GeoIP: ", "")
    print(address)
    return address


def open_image():
    image_path = r'C:\Users\yd002\Desktop\广告位示意图002.jpg'
    image_path2 = r'C:\Users\yd002\Desktop\微信图片_20190816150219.jpg'
    im = Image.open(image_path).convert('RGBA')
    mark = Image.open(image_path2)
    txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
    txt.paste(mark, (im.size[0]-700, im.size[1]-200))
    # 设置字体
    fnt = ImageFont.truetype("c:/Windows/Fonts/msyh.ttc", 20)
    # 操作新建的空白图片>>将新建的图片添入画板
    d = ImageDraw.Draw(txt)
    # 获取时间
    get_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # 地址
    address = "四川省成都市金牛区韦家碾一路红心绿地广场" + '\n' + get_time + '\n' + 'ID串号：18382413281'\
              + str(random.randint(10, 99))
    # 在新建的图片上添加字体
    d.text((txt.size[0] - 400, txt.size[1] - 100), address, font=fnt, fill=(255, 255, 255, 255))
    # 合并两个图片
    out = Image.alpha_composite(im, txt)
    out.show()


open_image()
# ip = get_ip()
# queryIpAddress(ip)
