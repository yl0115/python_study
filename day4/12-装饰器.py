# 装饰器本质上就是一个函数，可以给原函数功能进行扩展，这样的好处不改变原函数定义及调用操作


# 装饰器==》通过闭包完成装饰器
def decorator(new_func):
    print("装饰器的代码执行了")

    def inner():
        print('-'*5)
        new_func()
    # 返回的函数是闭包
    return inner


# 在使用@decorator的时候装饰器的代码就会执行
@decorator  # show = decorator(show)
# 使用装饰器装饰下面函数
def show():
    print("AAAA")


show()





# show = decorator(show)
# show()


