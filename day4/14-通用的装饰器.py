# 定义一个装饰器函数
def decorator(new_func):
    def inner(*args, **kwargs):  # *不定长位置参数，**不定长关键字参数
        print("计算结果如下：")
        return new_func(*args, **kwargs)  # *符号是拆包 **也是拆包
    return inner


@decorator  # @decorator相当于sum_num = decoration(sum_num)
def sum_num(num1, num2):
    result = num1+num2
    return result


@decorator  # sum_msg = decorator(sum_msg)
def sum_msg(num1, num2):
    print(num1, num2)


@decorator
def show():  # 相当于代码show = decorator(show)
    print("我是一个无参无返回值的函数")


value = sum_num(1, 8)
print(value)
sum_msg(2, 3)
show()



