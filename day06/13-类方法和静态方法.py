# coding=gbk

class Person(object):
    def __init__(self):
        self.name = 'С��'

    # ˽�е�������
    __type = '������'

    # ������󷽷����ڷ����Ĳ���������self��ʾ���󷽷���self��ʾ��ǰ����
    def show(self):
        print("��������")

    # �����෽����cls��ʾ��ǰ��
    @classmethod
    def show_info(cls):
        print(cls)
        print("����һ���෽��")

    # ���徲̬��������ʾ����̬�����͵�ǰ����͵�ǰ��û�й�ϵ������ʹ��self��cls
    @staticmethod
    def show_msg():
        print("����һ����̬����")

    # Ӧ�ó������෽�������޸�������
    @classmethod
    def set_type(cls, type):
        cls.__type = type

    @classmethod
    def get_type(cls):
        return cls.__type

# ----------------���󷽷�����ͨ�õķ����������޸Ķ������Ժ�������--------------------
    def instance_set_type(self, type, name):
        print(self.name)
        self.name = name
        # ��ȡ��������Ӧ����
        self.__class__.__type = type

    def instance_get_type(self):
        print(self.name)
        return self.__class__.__type

    @staticmethod  # �Ȳ���Ҫ��ǰ����͵�ǰ��
    def sum_num(num1, num2):
        return num1+num2


# ��������
p = Person()
p.show()
p.show_info()
p.show_msg()
p.set_type('�ڹ�')
result = p.get_type()
print(result)

p.instance_set_type('����', 'С��')
result = p.instance_get_type()
print(result)

result = p.sum_num(1, 2)
print(result)

# ����þ�̬�������෽������Ҫ���뵱ǰ�࣬�������ö��󷽷���Ҫ����һ��ʵ��
Person.show(p)
Person.show_info()
Person.show_msg()