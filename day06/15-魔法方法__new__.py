# coding=gbk
# __new__:�����������ʱ������__new__����
# __init__:���󴴽���ɻ����init��������������Ӷ������Լ���ʼ���ġ�
# ����������Զ����������������ȵ���__new__��ʾ���󴴽���ɣ�Ȼ���ڵ���__init__�����������ʼ��


class Student(object):
    # new��������Ĳ�������Ҫ����init��������Ĳ���
    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        print('��������')
        return object.__new__(cls)

    # ���󴴽����ˣ���������Ӷ������Ե�
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('��ʼ��')


stu = Student('����', 20)

