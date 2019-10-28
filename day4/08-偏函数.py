import functools
# 偏函数：通俗理解指明函数的参数偏爱某个值，就叫做偏函数


def show(num1, num2, num3=1):
    result = num1 + num2 + num3
    return result


result = show(1, 2)
print(result)


# 定义一个偏函数
def show1(num1, num2, num3=3):
    return show(num1, num2, num3)


result = show1(1, 2)
print(result)


# 指明函数的参数设置为摸个值
new_func = functools.partial(show1, num2=9)
result = new_func(1)
print(result)

# 指明内置函数的参数偏爱某个值，生成一个偏函数
result = int('123')
print(result)
# 这就是偏函数（指让某个函数偏爱某一个参数
new_l = functools.partial(int, base=2)
result = new_l('1')
print(result)