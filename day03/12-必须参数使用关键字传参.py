# 定义必须参数使用关键字传参的函数
def show(address, sex, *, name, age):
    print("我叫：%s，年龄：%d，性别%s，地址%s" % (name, age, sex, address))


# 使用位置参数传参
# show('小明', 18)

# 使用关键字参数传参
# show(name='小东', age=1)

show('上海', '男', name='liu', age=12)
