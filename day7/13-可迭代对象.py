# 可迭代对象：就是使用for循环遍历取值的对象就是可迭代对象
# for循环可直接遍历取值的对象：列表、元祖、字典、字符串、集合、range、
from collections import Iterator, Iterable
#
# result = isinstance([1, 2, 3].__iter__(), Iterable)
# # print(result)
# print([1, 2, 3].__iter__())
# 可迭代对象有一个__iter__()方法
result = dir([1, 2])
print(result)
a = isinstance(10, int)
print(a)



