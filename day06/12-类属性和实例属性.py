# coding=gbk

# ���������ڷ�����������ڲ���������Խ���������
# ʵ����������init�������涨������Խ���ʵ������


class Person(object):
    # �����ԣ�����û�д�������ʹ��������Կ��Զ����������
    type = "������"

    def __init__(self):
        # ʵ��(����)����
        self.name = '����'
        self.age = 27


# ----------------------�����ԵĲ���-----------------------------
# �鿴�����Ժͷ���
print(Person.__dict__)
# ����������
print(Person.type)
# ʹ���಻�ܷ��ʶ�������
# print(Person.name)

# �޸�������
Person.type = '������'
print(Person.type)
# �鿴�����Ժͷ���
print(Person.__dict__)

# ---------------------�������ԵĲ���------------------------------------
# ��������ʵ����
xiao_ming = Person()
# ʹ��ʵ�������󣩷��ʶ���ʵ��������
print(xiao_ming.name)
# ����ʵ��������������
print(xiao_ming.type)
# ����ʵ���������޸������ԣ�ʵ�������
xiao_ming.type = '������'
print(xiao_ming.__dict__)


# ʹ��ʵ���޸Ķ�������
xiao_ming.name = 'll'
print(xiao_ming.name)
print(xiao_ming.__dict__)

# �����Բ���������ɣ���������Բ���ʹ�ö�����ɣ�������Է���������


