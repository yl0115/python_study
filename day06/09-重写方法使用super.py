# coding=gbk


class Person(object):
    def show(self):
        print("��������")


class plane(object):
    def show(self):
        print("���Ƿɻ�")

    def fly(self):
        print("�ɻ����Է�")


class Student(Person, plane):
    def show(self):
        # ������дҲ����ʹ��super�����ø���ķ���
        # ����������̳����е���һ����
        print(Student.__class__.mro(Student))

        super(Student, self).show()


stu = Student()
stu.show()