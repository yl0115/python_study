# coding=gbk
# 单例:在应用程序中，不管创建多少次对象，只有一个实例对象


class Person(object):
    # 私有的类属性
    __instance = None

    def __new__(cls, *args, **kwargs):
        # if cls.__instance == None:
        if not cls.__instance:
            print('create new')
            # 把创建的对象返回给类属性
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print('shili new')


person = Person()
person1= Person()
print(person, person1)