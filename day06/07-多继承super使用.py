# coding=gbk


class A(object):
    def show_a(self):
        print("����A��")


class B(object):
    def show_b(self):
        print("����B��")


class C(A, B):
    def show_c(self):
        print(self.__class__.mro())
        # ָ����CҪ��self������̳�˳��������һ����
        super(C, self).show_b()


c = C()
c.show_c()


