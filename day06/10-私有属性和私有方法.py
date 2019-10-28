# coding=gbk
# 在属性名和方法名前面加上'__'那么定义的属性和方法就是私有属性和私有方法

class Person(object):
    def __init__(self, name, age):
        # 公共属性
        self.name = name
        # 私有属性，私有属性只能在本类内部使用，在类外面不能使用
        # 注意私有属性只能在init方法里面添加
        self.__age = age

    def show(self):
        print(self.name)
        print(self.__age)

    def __money(self):
        print(100)


person = Person('y',4)
person.show()
# 查看对象中的属性信息
print(person.__dict__)
# 私有属性外界不能访问
# print(person.__age)
# 私有方法外界不能访问
# person.__money()
# 本意修改类中的私有属性值
# 这里不是修改了私有属性，而是给对象添加了一个__age的对象属性
# 这里也不是添加的私有属性，私有属性只能在init方法中添加
person.__age = 20
print(person.__age)



# 查看对象中的属性信息
print(person.__dict__)
# 查看私有方法
print(Person.__dict__)

# 在python里面私有属性和私有方法没有做到绝对的私有，只是把私有属性和私有方法进行了名字的伪装

# 非常规操作，不建议以后使用
print(person.__dict__)
person._Person__age = 11
print(person._Person__age)
print(person.__dict__)



person._Person__money()



