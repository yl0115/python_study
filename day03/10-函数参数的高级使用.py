# name age是必填参数，*args是不定长位置参数，**kwargs是不定长关键字参数
def show(name, age, *args, **kwargs):
    print(name, age, args, kwargs)


# 不能使用下面的方式进行调用，因为前面使用的关键字后面不能使用位置参数
# show(name='lisi', age=18, 1, 4, c=1, v=3)

show('李四', 20, 1, 2, 3, a='苹果', b='香蕉')


