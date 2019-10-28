# 可变类型：可以在原有数据的基础上对数据进行修改，（添加删除或者修改数据）修改后内存地址不变
# 不可变类型：不能再原有数据的基础上对数据进行修改，可以直接赋值一个新的值，内存地址会发生改变
# 可变类型：列表、集合、字典对数据进行修改后内存地址不变
# 不可变类型：字符串、数字、元祖，不能再原有的数据上进行修改
my_list = [1, 5, 7]
# 查看内存地址
print(my_list, id(my_list))
my_list[0] = 6
print(my_list, id(my_list))
my_list.append(9)
del my_list[0]
print(my_list, id(my_list))


my_dict = {'name': '李四', 'age': 18}
print(my_dict, id(my_dict))
my_dict['sex'] = '男'
del my_dict['age']
my_dict['name'] = '王七'
print(my_dict, id(my_dict))

my_set = {5, 7, 9}
print(my_set, id(my_set))
my_set.add('王文英')
my_set.remove(5)
print(my_set, id(my_set))
# 可变类型：允许在原有数据基础上修改数据，内存地址不变

# ----------------------不可变类型-------------------
my_str = 'hello'
print(my_str, id(my_str))
my_str = 'world'
print(my_str, id(my_str))


my_num = 5
print(my_num, id(my_num))
my_num = 6
print(my_num, id(my_num))


my_tuple = (1, 5, 6)
print(my_tuple,id(my_tuple))
my_tuple = (4, 6)
print(my_tuple, id(my_tuple))
# 不可变类型：修改后内存地址发生变化

