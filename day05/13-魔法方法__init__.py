# coding=gbk
# ħ����������ǰ�����ĳ�����ܲ�����ʱ�򣬻��Զ�����ĳ������������__init__(),�������ʼ��ʱ���Զ�����
class Teacher:
    # init����������Ӳ���
    def __init__(self, name, age):
        # �������ʼ������Ӷ�������
        print("�����ʼ����")
        self.name = name
        self.age = age

    # ��ʾ��ʦ��Ϣ�ķ���
    def show_info(self):
        # self��ǰ�����Ǹ�����������self�������˭
        print(self.name, self.age)


teacher = Teacher('a', 15)
teacher.show_info()
teacher1 = Teacher('c', 7)
teacher1.show_info()
