# coding=utf-8
# 新式类的定义方式，建议使用新式类的方式
class Teacher(object):
    # 类属性
    country = '中国'

    # 方法
    def show(self):
        print("哈哈，我是授课老师的学生。")


t1 = Teacher()
t2 = Teacher()
t1.show()
t2.show()