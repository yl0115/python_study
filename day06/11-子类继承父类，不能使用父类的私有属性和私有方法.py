# coding=gbk

class Person(object):
    def __int__(self):
        self.__age = 10

    def __show(self):
        print('这里定义了一个私有方法')

    def test(self):
        print("test")


class Student(Person):
    def show(self):
        # 访问父类的私有属性和私有方法
        # print(self.__age)
        # self.__show()
        self.test()

    pass


student = Student()
student.show()
# print(student.__age)
# student.__show()


# 总结：子类继承父类不能直接使用父类私有属性和私有方法
