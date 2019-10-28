# coding=gbk
# 多态：关注的是同一个方法，但会出现不同的表现形式，在python不需要关心类型


class Text(object):
    def show(self):
        print("显示图片")


class Image(object):
    def show(self):
        print("显示图片")


class Video(object):
    def show(self):
        print("显示视频")


class Person(object):
    def show(self):
        print("我在跳舞")


# 实现显示数据功能
def show_data(data):
    # 关心的同一个方法，会出现不同的表现形式，那么这种操作叫做多态
    # 在python只关心对象方法，不关心对象类型
    data.show()


image = Image()
video = Video()
text = Text()
person = Person()
show_data(person)