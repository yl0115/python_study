__all__ = ['g_num', 'show']  # 置顶__all__会对from模块名 import * 只能使用指定功能代码
# 定义全局变量
g_num = 10


# 定义函数
def show():
    print('我是一个函数')


# 定义类
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return '神奇的天堂:  %s' % self.name

    def show_msg(self):
        print(self.name, self.age)




