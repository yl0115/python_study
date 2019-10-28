# coding=gbk
# __new__:当创建对象的时候会调用__new__方法
# __init__:对象创建完成会调用init方法，给对象添加对象属性及初始化的。
# 创建对象会自动调用两个方法，先调用__new__表示对象创建完成，然后在调用__init__方法给对象初始化


class Student(object):
    # new方法里面的参数是需要兼容init方法里面的参数
    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        print('创建对象')
        return object.__new__(cls)

    # 对象创建完了，给对象添加对象属性的
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('初始化')


stu = Student('李四', 20)

