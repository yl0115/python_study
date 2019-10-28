# 函数的不定长参数：1、不定长位置参数2、不定长关键字参数
# 不定长参数：调用函数的时候不确定传入多少个参数，可能是0个或者多个
# 定义函数的时候：1、不定长位置参数2、不定长关键字参数

# -----------------------不定长位置参数-----------------
# 定义一个不定长位置参数
def show(*args):
    pass


def sum_num(*args):
    # 提示：args：会吧调用函数传入的位置参数封装到一个元祖里面，如果没有传入就是一个空元祖
    print(args, type(args))
    result = 0
    for i in args:
        result +=i
    return result


value = sum_num(1, 2, 3, 4, 5, 6)
print(value)


# 注意：*args：表示定义的函数是不定长的位置参数，调用函数的时候只能使用位置参数传值

# ---------------------不定长关键字参数函数定义及调用------------------
# 定义不定长关键字参数函数，**kwargs:表示的就是一个不定长关键字参数

def show_msg(**kwargs):
    # kwargs会把函数调用的关键字封装到字典里面
    print(kwargs, type(kwargs))
    for key,value in kwargs.items():
        print(key,value)



show_msg(a=2, b=3)
