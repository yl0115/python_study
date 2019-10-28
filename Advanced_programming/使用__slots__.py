from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    pass

# def set_age(self, age):
#     self.age = age
#
#
# def set_score(self, score):
#     self.score = score
#
#
# stu = Student()
# stu.name = 'Michael'
# print(stu.name)
#
#
# stu.set_age = MethodType(set_age, stu)  # 给实例绑定一个方法
#
# stu.set_age(25)
# print(stu.age)
#
#
# Student.set_score = set_score  # 为了给所有实例绑定方法，直接给类绑定方法
# stu.set_score(100)
# print(stu.score)
# stu1 = Student()
# stu1.set_score(200)
# print(stu1.score)


stu = Student()
stu.name = 'bart'
stu.age = 15
stu.score = 90
print(stu.name, stu.age, stu.score)

