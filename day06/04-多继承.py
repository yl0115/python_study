# coding=gbk
# 多继承相当于继承多个父类


class A(object):
    def show(self):
        print("我是A类")


class B(object):
    def show1(self):
        print("我是B类")


class C(A, B):
    pass


c = C()
c.show()
c.show1()

# python方法调用会遵循mro，类顺序继承
print(C.mro())