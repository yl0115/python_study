# 函数就是实现某个功能的代码块，提高代码的复用性，减少代码的冗余


# 无参数无返回值函数
def show():
    print("大家好，今天的天气是小雨...！！！")


# 函数的调用
show()


# 有参数无返回值函数
def show(name, age):
    print('大家好我叫%s,我的年龄是%d' % (name, age))


# 函数调用,传入参数
show('test', 18)


# 无参数有返回值函数
def return_value():
    msg = '好好学习，天天向上'
    return msg


# 调用返回值函数，使用变量进行进行保存
result = return_value()
print(result)


# 有参数有返回值函数
def show_msg(name, age):
    msg = "我的名字叫%s，我的年龄：%d" % (name, age)
    return msg


result = show_msg('test', 15)
print(result)
