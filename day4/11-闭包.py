# 闭包：在函数嵌套的情况下，内部函数使用了外部函数的参数或者变量，并把内部函数返回，返回的这个函数可以成为闭包（对应的就是函数）
# 通过闭包可以生成不同的函数
# 闭包的好处可以根据不同的条件生成不同的函数


def num():
    result = 10

    def inner():
        print(result)
    return inner

new_func = num()
print(new_func)
new_func()


# 闭包的应用场景，可以根据参数生成不同的返回函数（闭包）

def hello(msg, count):
    res = 2

    def return_msg():
        result = msg*count + res
        return result
    return return_msg  # 返回函数时后面一定记得不加小括号，切记切记


new_func1 = hello(3, 2)
print(new_func1)
result = new_func1()
print(result)

