# _*_ coding:utf-8_*_
import os
import re
import shutil
import win32con
import win32gui
from time import sleep


class Open_File(object):
    def __init__(self, paths):
        self.paths = paths
        self.amount = 0
        # 未填写计数
        self.num = 0
        # 填写计数
        self.num2 = 0
        self.address = 't'
        self.judge_num = '1'
        self.move = None
        self.whole = r'E:\永川填写'
        self.deficiency = r'E:\永川资料欠缺'

    @staticmethod
    def tskill_2345():
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
    def tskill_txt():
        cmd = r'tasklist | findstr "notepad.exe"'
        console = os.popen(cmd)

        li = []
        for line in console.readlines():
            li.append(line)

        if li:
            li = str(li)
            pid = re.findall(r'\d+', li)
            os.system('tskill %s' % pid[0])
        else:
            pass

    @staticmethod
    def c_folder(paths):
        hwnd = win32gui.FindWindow(None, paths)
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    @staticmethod
    def open_folder(paths):
        os.system('explorer.exe /n,' + paths)

    def get_path(self):
        for i in os.listdir(self.paths):
            # 拼接时间文件夹地址
            time_folder = self.paths + '\\' + i
            for j in os.listdir(time_folder):
                if self.move is None:
                    pass
                else:
                    shutil.move(self.move, self.whole)
                # 拼接商家地址
                store_folder = time_folder + '\\' + j
                # 判断是否是TXT文件
                self.judge_txt(store_folder)

    def judge_txt(self, paths):
        for k in os.listdir(paths):
            # 拼接详细地址的具体路劲
            address_file = paths + '\\' + k
            if k.endswith('.txt'):
                # 打开商家目录
                self.open_folder(paths)
            if '优单合同.jpg' in k:
                self.open_image(address_file)
            # 判断以后缀.txt结尾
            if k.endswith('.txt'):
                paths_list = paths.split('\\')

                # 判断是否录入
                self.judge_num = str(input('\n是否录入《' + paths_list[-2] + '\\' + paths_list[-1] + '》：'))
                if self.judge_num == '1':
                    self.tskill_2345()
                    self.tskill_txt()
                    self.c_folder(paths_list[-1])
                    # 未填写计数
                    self.num += 1
                    sleep(2)
                    shutil.move(paths, self.deficiency)
                else:
                    self.address = paths
                    # 调用写入函数
                    self.write_in(address_file)
                    break

    def write_in(self, paths):
        """
        :param paths:
        :return:
        """
        # 分割地址回去folder名称
        paths_list = paths.split('\\')
        address = str(input("请输入地址："))
        ditui = str(input("请输入地推："))
        name = str(input("请输入广告位主："))
        id_card = str(input("请输入身份证："))
        tel = str(input("请输入电话："))
        with open(paths, 'a+', encoding='utf-8') as f:
            f.write(address + '\n')
            f.write(ditui + '\n')
            f.write(name + '\n')
            f.write(id_card + '\n')
            f.write(tel + '\n')
            f.close()
        self.tskill_2345()
        self.tskill_txt()
        self.c_folder(paths_list[-2])
        # 拼接需要移动的路劲
        self.move = paths_list[0] + '\\' + paths_list[1] + '\\' + paths_list[2] + '\\' + paths_list[3]
        # 填写计数
        self.num2 += 1
        surplus = self.amount-self.num-self.num2
        print("\n店铺共计%d个，完成录入%d个，资料不全%d个,还剩%d个。\n" % (self.amount, self.num2, self.num, surplus))

    @staticmethod
    def open_image(paths):
        os.startfile(paths)

    def store_sum(self):
        """
        :return:
        """
        for i in os.listdir(self.paths):
            # 拼接时间文件夹地址
            time_folder = self.paths + '\\' + i
            for j in os.listdir(time_folder):
                # 拼接商家地址
                store_folder = time_folder + '\\' + j
                for k in os.listdir(store_folder):
                    address_txt = store_folder + '\\' + k
                    if address_txt.endswith('.txt'):
                        self.amount += 1


if __name__ == '__main__':
    path = r'e:\成都内江'
    of = Open_File(path)
    of.store_sum()
    of.get_path()


