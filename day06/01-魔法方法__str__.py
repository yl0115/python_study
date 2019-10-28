# coding=gbk
# __str__:当使用print打印对象的时候，会自动调用对象的__str__方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 返回对象描述信息
    def __str__(self):
        # 返回一个字符串信息
        return "我叫：%s,年龄：%d" % (self.name, self.age)


# 创建一个对象
# 调用init方法使用位置参数方式传参
# person = Person('张三', 14)
# print(person.name, person.age)
person = Person(name="李四", age=17)
print(person)

