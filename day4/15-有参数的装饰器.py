def get_decorator(ch):
    # 定义装饰器
    def test(new_func):
        def inner(*args, **kwargs):
            print(ch*10, *args, **kwargs)
            new_func()
        return inner
    return test


# 把@后面的操作相当于执行了一个函数返回了一个装饰器
@get_decorator('A')  # 这就是一个有参数的装饰器
def show():
    print("1111")


show()