# coding=gbk
# ��̬����ע����ͬһ��������������ֲ�ͬ�ı�����ʽ����python����Ҫ��������


class Text(object):
    def show(self):
        print("��ʾͼƬ")


class Image(object):
    def show(self):
        print("��ʾͼƬ")


class Video(object):
    def show(self):
        print("��ʾ��Ƶ")


class Person(object):
    def show(self):
        print("��������")


# ʵ����ʾ���ݹ���
def show_data(data):
    # ���ĵ�ͬһ������������ֲ�ͬ�ı�����ʽ����ô���ֲ���������̬
    # ��pythonֻ���Ķ��󷽷��������Ķ�������
    data.show()


image = Image()
video = Video()
text = Text()
person = Person()
show_data(person)