# coding=gbk
# 重写：子类继承父类，父类的方法满足不了子类的需求，可以对父类方法进行重写
# 重写的特点1、继承关系，2、方法相同


class Person(object):
    def run(self):
        print("跑起来了")


class Student(Person):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 因为父类的方法满足不了子类需要对其进行重写
    def run(self):
        print("%s跑起来了" % self.name)


student = Student('王五', 20)
# 调用方法的时候先从本类去找，如果没有去父类找，遵循mro规则
student.run()
