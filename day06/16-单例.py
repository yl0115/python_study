# coding=gbk
# ����:��Ӧ�ó����У����ܴ������ٴζ���ֻ��һ��ʵ������


class Person(object):
    # ˽�е�������
    __instance = None

    def __new__(cls, *args, **kwargs):
        # if cls.__instance == None:
        if not cls.__instance:
            print('create new')
            # �Ѵ����Ķ��󷵻ظ�������
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self):
        print('shili new')


person = Person()
person1= Person()
print(person, person1)