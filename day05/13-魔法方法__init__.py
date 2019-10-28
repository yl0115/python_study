# coding=gbk
# 魔法方法：当前需完成某个功能操作的时候，会自动调用某个方法，比如__init__(),当对象初始化时会自动调用
class Teacher:
    # init方法可以添加参数
    def __init__(self, name, age):
        # 给对象初始化，添加对象属性
        print("对象初始化了")
        self.name = name
        self.age = age

    # 显示老师信息的方法
    def show_info(self):
        # self当前对象，那个对象调用这个self对象就是谁
        print(self.name, self.age)


teacher = Teacher('a', 15)
teacher.show_info()
teacher1 = Teacher('c', 7)
teacher1.show_info()
