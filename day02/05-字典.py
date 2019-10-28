# 字典：以大括号表现形式的键值对数据集合{}比如：{"name":"zhangsan","age":18}
# key一般都是字符串，key是不可变类型：数字字符串元祖；不使用可变类型：[]{}
my_dict = {"name": "张三", "age": 18}
print(my_dict, type(my_dict))
# 通过key获取对应的value值，key值在字典里面是唯一的
value = my_dict['name']
print(value)

# 以中括号取值没有找到会报错，以get取值没有找到不会报错
value = my_dict['age']  # 没有取到值会报错
print(value)
result = my_dict.get('name')  # 没有取到值不会报错
print(result)

# 设置默认值
result = my_dict.get('sex', '男')
print(result)
