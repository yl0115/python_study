# coding=gbk
# ��д������̳и��࣬����ķ������㲻����������󣬿��ԶԸ��෽��������д
# ��д���ص�1���̳й�ϵ��2��������ͬ


class Person(object):
    def run(self):
        print("��������")


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ��Ϊ����ķ������㲻��������Ҫ���������д
    def run(self):
        print("%s��������" % self.name)


student = Student('����', 20)
# ���÷�����ʱ���ȴӱ���ȥ�ң����û��ȥ�����ң���ѭmro����
student.run()
