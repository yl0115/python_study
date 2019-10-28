# 列表生成式(列表推导式)：通俗理解使用for循环快速创建一个列表，最终要获取一个列表

my_list = []
for i in range(1, 6):
    print(i)
    my_list.append(i)
print(my_list)
m = [i for i in range(1,8)]
print("你是一个打住", m)

# 列表推导式，目的快读创建一个列表
# 列表推导式的语法格式
my_list1 = [value for value in range(1, 7)]
my_list2 = [i for i in range(1, 9)]
print(my_list2)
print(my_list1)
my_list1 = [value * 2 for value in range(1, 7)]
print(my_list1)

result = [len(value) for value in ['abc', 'ab']]
print(result)

result = [value + 'hello' for value in ['abc', 'ab']]
print(result)

my_list = [(x, y) for x in range(1, 3) for y in range(1, 3)]
print(my_list)
my_list = [i for i in range(1, 10) if i % 2 == 0]
my_list3 =[i for i in range(2, 8) if i % 3 == 0]
print(my_list3)
print(my_list)
