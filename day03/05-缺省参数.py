# 缺省参数：在函数定义的时候参数就有值，这样的参数叫做缺省参数
# 如果给缺省参数传值就使用传入的值，如果不传值就使用默认值

def sum(num1, num2=2):
    result = num1 + num2
    return result


# 没有给参数传值，那么久使用默认值，如果传值就使用传入的值
value = sum(1, 9)
print(value)
