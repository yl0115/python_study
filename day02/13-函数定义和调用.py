# 函数定义格式
# def 函数名(参数):
# #     功能代码实现
def show():
    print("我叫hello我今年18岁")


show()

# 定义带有参数的函数
def show(name, age):
    # 判断是否输入相符合的类型
    if isinstance(age, int):
        print("我叫%s我今年%d岁" % (name, age))
    else:
        print("你说输入的不是int类型")


show('test', 12)
