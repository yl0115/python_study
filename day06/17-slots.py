# coding=gbk
# slots:ָ�����������ʱ�򣬲���������������ԣ�ֻ����ָ������


class Student(object):
    # �������ĺô������ö�������Թ̶�
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('r', 1)
print(stu.name, stu.age)
stu.name = 'd'

print(stu.name, stu.age)