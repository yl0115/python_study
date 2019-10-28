# coding=gbk
# 子类继承父类可以使用父类的方法和属性
# 继承的好处：子类可以复用父类的代码


# 单继承：子类只继承一个父类
# 父类（基类），子类（派生类）
class Person(object):
    def __init__(self):
        self.name = '张三'
        self.age = 20

    # 对象方法，当前方法参数有self表示对象方法
    def show(self):
        print(self.name, self.age)


# 学生类是子类，小括号里面是父类
class Student(Person):
    pass


xiao_lan = Student()
xiao_lan.show()
print(xiao_lan.name, xiao_lan.age)

