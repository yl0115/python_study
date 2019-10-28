def decorator1(new_func):
    def inner():  # inner其实就是封装传入函数代码
        print("-"*10)
        new_func()
    return inner


def decorator2(new_func):
    def inner():  # inner其实就是封装传入函数代码
        print("*"*10)
        new_func()
    return inner


@decorator1  # show =decorator(decorator(inner))
@decorator2  # show = decorator(show) ==> decorator(inner)
def show():
    print("AAAA")


show()
