# coding=gbk
# ���������ͷ�����ǰ�����'__'��ô��������Ժͷ�������˽�����Ժ�˽�з���

class Person(object):
    def __init__(self, name, age):
        # ��������
        self.name = name
        # ˽�����ԣ�˽������ֻ���ڱ����ڲ�ʹ�ã��������治��ʹ��
        # ע��˽������ֻ����init�����������
        self.__age = age

    def show(self):
        print(self.name)
        print(self.__age)

    def __money(self):
        print(100)


person = Person('y',4)
person.show()
# �鿴�����е�������Ϣ
print(person.__dict__)
# ˽��������粻�ܷ���
# print(person.__age)
# ˽�з�����粻�ܷ���
# person.__money()
# �����޸����е�˽������ֵ
# ���ﲻ���޸���˽�����ԣ����Ǹ����������һ��__age�Ķ�������
# ����Ҳ������ӵ�˽�����ԣ�˽������ֻ����init���������
person.__age = 20
print(person.__age)



# �鿴�����е�������Ϣ
print(person.__dict__)
# �鿴˽�з���
print(Person.__dict__)

# ��python����˽�����Ժ�˽�з���û���������Ե�˽�У�ֻ�ǰ�˽�����Ժ�˽�з������������ֵ�αװ

# �ǳ���������������Ժ�ʹ��
print(person.__dict__)
person._Person__age = 11
print(person._Person__age)
print(person.__dict__)



person._Person__money()



