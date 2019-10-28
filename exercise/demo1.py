# -*- coding:utf-8 -*-
import requests
import json
import logging


class Mind(object):
    def __init__(self):
        self.URL = r'http://192.168.3.111:8080/mind'

    def my(self):
        # 发送验证码
        address = r'/api/user/User_crud/sendSms'
        params = {"tel": "18382413281"}
        r = requests.post(self.URL+address, data=params)
        a = r.text
        print(a)
        if 'success' in a:
            logging.info('请勿重复发送验证码')
        else:
            logging.info('登录失败')


if __name__ == '__main__':
    md = Mind()
    md.my()
