# 获取容器类型（字符串、list、tuple、set、dict）中的每一个数据，使用for循环是最简单的。
my_str = 'abc'
for i in my_str:
    print(i)

# 循环遍历时下标和数据都需要时可以使用enumerate
my_list = ['苹果', '鸭梨']
for i in enumerate(my_list):
    print(i, i[1], type(i))


# index value 获取的是列表中的每一个值就是拆包
for index, value in enumerate(my_list):
    if index == 1:
        print(index, value)
        break
    print(index, value)

for i in enumerate((1, 5)):
    print(i)

# 字典默认遍历的是key值
for i, t in {'name': '张三', 'age': 18}.items():
    print(i, t)

