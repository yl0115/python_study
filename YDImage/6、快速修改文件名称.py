# -*- coding: utf-8 -*-
import os
from PIL import Image
import threading
import random
from time import sleep
import re


class ThreadClass(object):
    def __init__(self):
        self.num = 0
        self.amount = 0
        self.num_sum = 0
        self.residue = 0
        # 文件后缀
        self.number = 0

    def deploy(self, paths):
        for i in os.listdir(paths):
            for j in os.listdir(paths+'\\'+i):
                abspath = paths + '\\' + i + '\\' + j
                if '广告' in abspath:
                    a = threading.Thread(target=self.io, args=(abspath,))
                    a.start()
                    a1 = threading.Thread(target=t.tskill_2345)
                    a1.start()
                    self.amount += 1
                    path_list = abspath.split('\\')
                    self.residue = self.num_sum - self.amount
                    print('\n\n' + "共" + str(self.num_sum) + "张图片，当前是第"
                          + str(self.amount) + "张" + ",还剩" + str(self.residue) + "张")
                    print('图片名称：' + path_list[2] + '\\' + path_list[3] + '\\' + path_list[4])
                    input_name = str(input('***********1、广告，2、店铺、3、合同，4、执照：'))
                    self.number += 1
                    number = str(self.number) + '.jpg'
                    shop_name = paths + '\\' + i + '\\'
                    print(shop_name)
                    if input_name == '1':
                        os.rename(abspath, shop_name + '广告位示意图' + number)
                    elif input_name == '2':
                        os.rename(abspath, shop_name + '店铺照片' + number)
                    elif input_name == '3':
                        os.rename(abspath, shop_name + '优单合同' + number)
                    elif input_name == '4':
                        os.rename(abspath, shop_name + '营业执照' + number)
                    else:
                        continue

    def con(self, paths):
        r_list = os.listdir(paths)
        for q_list in r_list:
            w_list = paths + '\\' + q_list
            for t_list in os.listdir(w_list):
                y_list = paths + '\\' + q_list + '\\' + t_list
                for u_list in os.listdir(y_list):
                    i_list = paths + '\\' + q_list + '\\' + t_list + '\\' + u_list
                    if '广告' in i_list:
                        self.num_sum += 1

    @staticmethod
    def tskill_2345():
        sleep(2)
        cmd = r'tasklist | findstr "2345PicViewer.exe"'
        console = os.popen(cmd)
        li = []
        for line in console.readlines():
            li.append(line)

        if li:
            li = str(li)
            pid = re.findall(r'\d+', li)
            if len(pid) <= 5:
                os.system('tskill %s' % pid[1])
            elif 5 < len(pid) <= 12:
                os.system('tskill %s' % pid[1])
                os.system('tskill %s' % pid[6])
            elif len(pid) > 13:
                os.system('tskill %s' % pid[1])
                os.system('tskill %s' % pid[6])
                os.system('tskill %s' % pid[11])
            else:
                os.system(r'taskkill /IM 2345PicViewer.exe /F')
        else:
            pass

    @staticmethod
    def io(paths):
        o = Image.open(paths)
        o.show()


if __name__ == '__main__':

    path = r'e:\成都内江'
    t = ThreadClass()
    t.con(path)
    r = os.listdir(path)
    for w in r:
        b = path+'\\'+w
        t.deploy(b)

