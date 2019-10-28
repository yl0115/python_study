# coding=gbk
class A(object):
    def __init__(self, name):
        print("A")
        self.name = name


class B(A):
    # 如果子类提供了调用方法，不会自动调用父类方法
    # 如果子类提供了init方法，想要使用父类的init方法需要自己调用
    def __init__(self, subject):
        # 调用父类的init方法
        # self.__init__('张三')
        # 使用类名调用父类init方法
        # A.__init__(self, '李四')
        # 使用super进行调用父类中init方法
        # super(B, self).__init__('y')
        # super简写
        super().__init__('i')
        print("B")
        self.subject = subject

    def show(self):
        print("我是B类")


b = B('python')
b.show()
print(b.subject)
print(b.name)