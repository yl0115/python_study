# coding=gbk
# ��̳��൱�ڼ̳ж������


class A(object):
    def show(self):
        print("����A��")


class B(object):
    def show1(self):
        print("����B��")


class C(A, B):
    pass


c = C()
c.show()
c.show1()

# python�������û���ѭmro����˳��̳�
print(C.mro())