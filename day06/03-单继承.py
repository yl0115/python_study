# coding=gbk
# ����̳и������ʹ�ø���ķ���������
# �̳еĺô���������Ը��ø���Ĵ���


# ���̳У�����ֻ�̳�һ������
# ���ࣨ���ࣩ�����ࣨ�����ࣩ
class Person(object):
    def __init__(self):
        self.name = '����'
        self.age = 20

    # ���󷽷�����ǰ����������self��ʾ���󷽷�
    def show(self):
        print(self.name, self.age)


# ѧ���������࣬С���������Ǹ���
class Student(Person):
    pass


xiao_lan = Student()
xiao_lan.show()
print(xiao_lan.name, xiao_lan.age)

