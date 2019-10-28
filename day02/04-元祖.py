# 以小括号()表现形式数据集合   比如(1,2,3)
# 元祖只能根据下表取值，不能对元祖数据进行修改删除
my_tuple = (1, 4, 'abc', True)
print(my_tuple[-1])
print(my_tuple[0])

my_tuple = (1, [3, 5])
# 获取列表根据列表修改数据
my_tuple[1][1] = 6
print(my_tuple)
# 元祖中只有一个元素 需要加上逗号(5,)

# 查找元祖中的数据
# 判断数据是否存在
my_tuple = (5, 10)
result = 5 in my_tuple
print(result)
result = 5 not in my_tuple
print(result)
result = my_tuple.index(5)
print(result)
result = my_tuple.count(5)
print(result)
