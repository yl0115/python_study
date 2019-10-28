# -*- coding:utf-8 -*-
import socket
import requests
import logging
import unittest
from time import strftime


class My_Module(unittest.TestCase):
    tel = 18382413281
    newtel = 18215575122
    password = "1"

    def setUp(self):
        self.dev = True

        if self.dev:
            self.mind = r'http://192.168.3.72:8080/mind'
        else:
            self.mind = r'http://192.168.3.111:8080/mind'

    def tearDown(self):
        pass

    @unittest.skip("验证码")
    def test_sendSms(self):
        # 发送验证码
        url = r'/api/user/User_crud/sendSms'
        data = {"tel": self.tel}
        r = requests.post(self.mind + url, data=data)
        self.assertEqual(r.status_code, 200)

    @unittest.skip("验证码登录")
    def test_LoginBySms(self):
        # 验证码登录
        # 获取本机电脑名
        myname = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        smscode = str(input("请输入旧手机验证码："))
        data = {
            "tel": self.tel,
            "smsCode": smscode,
            "ipaddress": myaddr
        }
        url = r'/api/user/User_crud/LoginBySms'
        r = requests.post(self.mind + url, data=data)
        result = r.json()
        if result['msg'] == "登录成功":
            self.assertEqual(result['msg'], "登录成功")
            self.assertEqual(result['data']['user']['id'], 30)
            self.assertEqual(result['data']['user']['nickName'], self.tel)
            self.assertEqual(result['data']['user']['tel'], self.tel)
            self.assertEqual(result['data']['user']['tel'], self.tel)
        elif result['msg'] == "你已经登录":
            self.assertEqual(result['msg'], "你已经登录")
        else:
            self.assertEqual(result['msg'], "验证码错误,请重新输入")

    @unittest.skip("修改用户信息")
    def test_updateUser(self):
        # 修改用户信息
        url = r'/api/user/User_crud/updateUser'
        r = requests.put(self.mind + url)
        logging.info(r)

    # @unittest.skip("修改密码")
    def test_updatePwd(self):
        # 修改密码
        data = {"userId": 30, "oldPwd": "0", "newPwd": "1"}
        url = r'/api/user/User_crud/updatePwd'
        r = requests.put(self.mind + url, data=data)
        result = r.json()
        if result['info'] == '旧密码错误':
            self.assertEqual(result['code'], 0)
            self.assertEqual(result['data'], None)
        if result['code'] == 200:
            self.assertEqual(result['code'], 200)
            self.assertEqual(result['info'], "修改成功")
            self.assertEqual(result['data']['id'], data["userId"])
            self.assertEqual(result['data']['nickName'], self.tel)

    @unittest.skip("修改手机号码")
    def test_updateTel(self):
        # 修改手机号码
        smscode = str(input("请输入旧手机验证码："))
        data = {"userId": 30, "oldTel": self.tel, "smsCode": smscode, "newTel": self.newtel}
        url = r'/api/user/User_crud/updateTel'
        r = requests.put(self.mind + url, data=data)
        result = r.json()
        print(result)
        if result['code'] == 200:
            self.assertEqual(result['code'], 200)
        else:
            self.assertEqual(result['code'], 0)
            self.assertEqual(result['info'], '验证码错误,请重新输入')
            self.assertEqual(result['data'], None)

    @unittest.skip("设置登出时间")
    def test_addLoginOutTime(self):
        # 设置登出时间
        # 获取本机电脑名
        myname = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        # 获取当前时间
        newtime = strftime("%Y-%m-%d %H:%M:%S")
        data = {
                  "code": "444",
                  "id": 88,
                  "ipaddress": myaddr,
                  "logintime": "2019-08-14T11:37:38.000+0000",
                  "signouttime": newtime,
                  "userid": 30
            }
        url = r'/api/user/User_crud/addLoginOutTime'
        r = requests.put(self.mind + url)
        result = r.json()
        print(type(result))
        print(result)

    @unittest.skip("密码登录")
    def test_LoginByPwd(self):
        # 密码登录
        # 获取本机电脑名
        myname = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        data = {
            "tel": self.tel,
            "password": self.password,
            "ipaddress": myaddr
        }
        url = r'/api/user/User_crud/LoginByPwd'
        r = requests.post(self.mind + url, data=data)
        result = r.json()
        if result['success']:
            self.assertEqual(result['msg'], "你已经登录")
        else:
            pass


if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(My_Module('test_updatePwd'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)



