from collections import Iterator
# 生成器是一个特殊的迭代器，也就是说他可以通过next()函数和for循环取值
# 迭代器和生成器的好处是：根据需要每次生成一个值，不像列表把所有的数据都准备好，这样列表比较占用内存
# 生成器和迭代器内存暂用比较少
# 值只能往后取，不能往前面取
# 1、使用生成器表达式
# result = [x for x in range(6)]
# print(result, type(result))
#
# result = (x for x in range(6))
# print(result, type(result))
# 测试：使用next()获取下一个值
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())
# print(result.__next__())

# value = next(result)
# print(value)
# for i in result:
#     print(i)


# 2、使用yield创建生成器
def show():
    for i in range(5):
        # 代码遇到yield会暂停，然后把结果返回回去，下次启动生成器在暂停的位置往下执行
        # yield可以返回多次值，return只能返回一次值
        yield i


value = show()
result = isinstance(value, Iterator)
print(result)
for value in value:
    print(value, end=' ')


