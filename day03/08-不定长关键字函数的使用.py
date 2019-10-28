# 定义不定长关键字函数
def show_msg(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key, value)


def show(**kwargs):
    # 把关键字参数封装到字典里面
    show_msg(**kwargs)

show(a=1,  b=2)