# 列表：以[]中括号表现形式的数据集合   比如[1, 2]
# 列表里面可以放入任何数据
my_list = [1, 1.22, 'abc', True]
# 获取列表中可以根据下标获取
print(my_list[0])

# 把一个列表中的元素添加到另个列表中
list_num1 = ['1', '3', 5]
my_list.extend(list_num1)
print(my_list)

# 列表添加
my_list.append('ff')
my_list.append('耗子')
my_list.insert(0, 'dddd')
print(my_list)

# 修改数据
my_list[-1] = '桃子'
print(my_list)

# 删除数据
# remove删除指定数据
my_list.remove('abc')
# 根据下表删除指定数据
del my_list[0]
print(my_list)

# 根据下表删除数据，并返回删除数据
# pop不指定下标默认删除最后一个数据
result = my_list.pop()
print(result)
print(my_list)
result = my_list.pop(0)
print(result, my_list)

# 判断数据是否存在列表中
result = 'taozi' in my_list
print(result)
result = 't'not in my_list
print(result)

# 根据数据在列表中查找指定下标
# result =
my_list.append('耗子')
print(my_list)
print(my_list.index('耗子'))
print(my_list.count('耗子'))