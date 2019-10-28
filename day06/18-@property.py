# coding=gbk


class Student(object):
    def __init__(self):
        self.__score = 100

    @property
    def get_score(self):
        return self.__score

    @get_score.setter
    def get_score(self, score):
        self.__score = score


stu = Student()
# result = stu.get_score()
# print(result)
# stu.set_score(77)
# result = stu.get_score()
# print(result)
score = stu.get_score
print(score)
stu.set_score = 80
score = stu.get_score
print(score)
