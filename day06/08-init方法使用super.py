# coding=gbk
class A(object):
    def __init__(self, name):
        print("A")
        self.name = name


class B(A):
    # ��������ṩ�˵��÷����������Զ����ø��෽��
    # ��������ṩ��init��������Ҫʹ�ø����init������Ҫ�Լ�����
    def __init__(self, subject):
        # ���ø����init����
        # self.__init__('����')
        # ʹ���������ø���init����
        # A.__init__(self, '����')
        # ʹ��super���е��ø�����init����
        # super(B, self).__init__('y')
        # super��д
        super().__init__('i')
        print("B")
        self.subject = subject

    def show(self):
        print("����B��")


b = B('python')
b.show()
print(b.subject)
print(b.name)