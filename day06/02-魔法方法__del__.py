# coding=gbk
# __del__:�������ͷŵ�ʱ����Զ�����__del__����
# 1�������˳�����������ʹ�õĶ���ȫ������
# 2����ǰ�����ڴ��ַû�б���ʹ��ʱ��ô���������
import time


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ���������ü���Ϊ0��ʱ������__del__
    def __del__(self):
        print('�����ͷ���:', self)


# ��������
person = Person('С��', 20)
print(person)
# ɾ������
del person
# ���ü������ڴ��ַ������ʹ�ô�������ǰ����
time.sleep(6)
print("�����ͷ���")

