# coding=gbk
class Animal(object):
    # ���󷽷�
    def run(self):
        print("������������")


class Dog(Animal):
    def run(self):
        print("С����������")

    def wang(self):
        # �ٴ˵��ø��෽��
        # 1��self,ǰ�ᵱǰ������û�и��෽����������õ�ʱ��ǰ��ķ���
        # self.run()
        # 2��ʹ�ø�������������ʹ���������ö��󷽷���Ҫ����ʵ������
        # Animal.run(self)
        # 3��super���ø��෽��
        # ����ָ���࣬����̳����л�ȡ��һ����
        # ��һ������Dog��ʾ�� ����ָ��������̳����л�ȡ��һ����
        # �ڶ�������self��ʾ����ȡself�������͵���̳���
        # super��һ������ֱ�Ӽ̳еĸ��࣬
        super(Dog, self).run()
        # ��ӡ�̳���
        print(self.__class__.mro())
        print("������")


dog = Dog()
dog.wang()
dog.run()
