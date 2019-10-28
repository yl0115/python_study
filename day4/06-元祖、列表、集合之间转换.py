my_list = [1, 4]
my_tuple = (5, 7)
my_set = {4, 9}
# 把列表、元祖转成集合
result = set(my_list)
print(result)
result = set(my_tuple)
print(result)
# 把列表、集合转元祖
result = tuple(my_list)
print(result)
result = tuple(my_set)
print(result)
# 把元祖和集合转列表
result = list(my_set)
print(result)
result = list(my_tuple)
print(result)