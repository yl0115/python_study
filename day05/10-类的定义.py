# coding=gbk
# 类的定义需要使用关键字class，人是有特征和行为（动作）
# 类里面有属性（特征）和方法（行为）


# 定义老师类,这是旧式类，自己不主动继承object，在python3里面旧式类默认继承object
# 在python2里面就没有父类
class Teacher():
    # 类属性
    country = '中国'

    # 方法
    def show(self):
        print("哈哈，我是授课老师的学生。")


# 通过类创建对象，类好比是一个模具，模具可以创建很多个对象
teacher = Teacher()  # 类名（），表示创建一个对象
# 调用方法，对象名点方法名字
teacher.show()

# 查看这个类继承的父类
print(Teacher.__bases__)