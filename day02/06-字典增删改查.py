# 字典是无序的 列表和元祖是有序的
# 有序：输入的顺序和输出的数据顺序不一致
# 无序：输入的殊勋和输出的数据顺序一致
my_dict = {}
print(my_dict, type(my_dict))
# 添加键值对,key不在字典就是添加
my_dict['name'] = '张三'
print(my_dict)
my_dict['age'] = 18
my_dict['sex'] = '男'
my_dict['address'] = '北京'
print(my_dict)
# 修改键值对，key存在字典就是修改
my_dict['address'] = '成都'
print(my_dict)
# 删除键值对
del my_dict['age']
print(my_dict)
# popitem随机删除键值对
value = my_dict.popitem()
print(value, my_dict)
# 指定key删除键值对
value = my_dict.pop('sex')
print(value)
# 判断key是否存在
result = 'age' in my_dict
print(result)
# 默认判断是key需要判断value需要指定。values()
result = '张三' in my_dict.values()
print(result)