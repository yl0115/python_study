# 高阶函数：当一个函数的参数可以接收另外一个函数或者还可以返回一个函数，那么这个函数就是叫做高阶函数
# 高阶函数针对的是接收或者返回的是函数，类似于这样的函数被称为高阶函数


def sum_num(num1, num2):
    result = num1 + num2
    return result


# 高阶函数，接收的一个参数是函数
def calc(num1, num2, new_func):
    value = new_func(num1, num2)
    return value


result = calc(1, 6, sum_num)
print(result)


# 高阶函数：还能返回一个函数
def test(new_func):
    new_func()

    def inner():
        print("我是一个内部函数")
    return inner


def show_msg():
    print("天气好闷热")


result = test(show_msg)
result()

