# coding=gbk
# __str__:��ʹ��print��ӡ�����ʱ�򣬻��Զ����ö����__str__����
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # ���ض���������Ϣ
    def __str__(self):
        # ����һ���ַ�����Ϣ
        return "�ҽУ�%s,���䣺%d" % (self.name, self.age)


# ����һ������
# ����init����ʹ��λ�ò�����ʽ����
# person = Person('����', 14)
# print(person.name, person.age)
person = Person(name="����", age=17)
print(person)

