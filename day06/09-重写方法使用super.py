# coding=gbk


class Person(object):
    def show(self):
        print("我是人类")


class plane(object):
    def show(self):
        print("我是飞机")

    def fly(self):
        print("飞机可以飞")


class Student(Person, plane):
    def show(self):
        # 方法重写也可以使用super，调用父类的方法
        # 根据类找类继承链中的下一个类
        print(Student.__class__.mro(Student))

        super(Student, self).show()


stu = Student()
stu.show()