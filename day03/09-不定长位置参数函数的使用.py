# 定义不定长位置参数函数
def show_msg(*args):
    print(args)
    for i in args:
        print(i)


# 定义不定长位置参数函数
def show(*args):
    # print(args, type(args))
    # show_msg(args)   # ((1, 2),)
    # 解决办法：对元祖进行拆包
    show_msg(*args)

show(1, 2)
