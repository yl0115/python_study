class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object(name is %s)' % self.name
    __repr__ = __str__


print(Student('brat'))


class Fb(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # 使用for循环进行类循环
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a+self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a


for i in Fb():
    print(i)


class Fib(object):
    def __getitem__(self, item):  # 按照下标一样取值，__getitem__
        a, b = 0, 1
        for x in range(item):
            a, b = b, a+b
            return a


f = Fib()
print(f[6])

print(list(range(100))[5:10])


class Student1(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):  # 直接对实例进行调用
        print('My name is %s.' % self.name)


s = Student1('bart')
s()

print(callable(Student1('1')))  # 通过callable（）函数可以判断一个对象是否是“可调用”对象

