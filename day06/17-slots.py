# coding=gbk
# slots:指明创建对象的时候，不能再添加其他属性，只能是指定属性


class Student(object):
    # 这样做的好处可以让对象的属性固定
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('r', 1)
print(stu.name, stu.age)
stu.name = 'd'

print(stu.name, stu.age)