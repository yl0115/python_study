# 匿名函数：顾名思义就是函数没有名字lambda关键字第一的函数就是匿名函数
# 匿名函数只适合做一些简单的操作，返回值不需要加上return
result = (lambda x, y: x+y)(1, 2)
print(result)
# 一般使用变量保存匿名函数
func = lambda x, y: x*y
result = func(1, 6)
print(result)


# 匿名函数应用场景，简化代码
# 判断是否是偶数
def is_os(num):
    if num % 2 == 0:
        return True
    else:
        return False


result = is_os(9)
print(result)
# 匿名函数可以简单if判断
func = lambda num: True if num % 2==0 else False
result = func(4)
print(result)

# 对字典列表排序的时候还可以使用匿名函数
my_list = [{"name": "张三", "age": 18, "sex": "男"}, {"name": "李四", "age": 12, "sex": "女"}]
# 表示列表中的每一项数
# item["age"]:根据字典中age对应的value值排序
# 默认从小到大
# my_list.sort(key=lambda item: item['age'], reverse=False)
# print(my_list)

# 匿名函数也是一个函数


def get_value(item):
    return item['age']


my_list.sort(key=get_value, reverse=True)
print(my_list)
