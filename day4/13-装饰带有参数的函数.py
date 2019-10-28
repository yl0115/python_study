# 定义一个装饰器函数
def decorator(new_func):
    def inner(num1, num2):
        print("计算结果如下：")
        return new_func(num1, num2)
    return inner


@decorator  # @decorator相当于sum_num = decorator(sum_num)
def sum_num(num1, num2):
    result = num1+num2
    return result


@decorator  # 相当于sum_msg = decorator(sum_msg)
def sum_msg(num1, num2):
    print(num1, num2)


value = sum_num(2, 6)
print(value)

sum_msg(2, 8)





