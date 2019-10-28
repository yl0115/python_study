# coding=gbk
# __del__:当对象释放的时候会自动调用__del__方法
# 1、程序退出，程序中所使用的对象全部销毁
# 2、当前对象内存地址没有变量使用时那么对象会销毁
import time


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当对象引用计数为0的时候会调用__del__
    def __del__(self):
        print('对象释放了:', self)


# 创建对象
person = Person('小米', 20)
print(person)
# 删除变量
del person
# 引用计数：内存地址被变量使用次数，当前引用
time.sleep(6)
print("程序释放了")

