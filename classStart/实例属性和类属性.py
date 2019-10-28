class Student(object):
    def __init__(self, name):
        self.name = name


stu = Student('bart')
print(stu.name)
stu.score = 90
print(stu.score)


class Student1(object):
    name = 'Stude1nt'


s = Student1()  # 创建实例s
print(s.name)  # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性。
print(Student1.name)  # 打印类的属性
s.name = 'yanglei'
print(s.name)
print(Student1.name)
del s.name
print(s.name)




