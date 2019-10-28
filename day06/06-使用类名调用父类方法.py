# coding=gbk
class Animal(object):
    # 对象方法
    def run(self):
        print("动物跑起来了")


class Dog(Animal):
    def run(self):
        print("小狗跑起来了")

    def wang(self):
        # 再此调用父类方法
        # 1、self,前提当前类里面没有父类方法，否则调用的时当前类的方法
        # self.run()
        # 2、使用父类的类名，如果使用类名调用对象方法需要传入实例对象
        # Animal.run(self)
        # 3、super调用父类方法
        # 根据指定类，在类继承链中获取下一个类
        # 第一个参数Dog表示： 根据指定类找类继承链中获取下一个类
        # 第二个参数self表示：获取self对象类型的类继承链
        # super不一定是你直接继承的父类，
        super(Dog, self).run()
        # 打印继承链
        print(self.__class__.mro())
        print("汪汪汪")


dog = Dog()
dog.wang()
dog.run()
