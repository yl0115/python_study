# 切片：根据下标的范围获取一部分数据，列表和字符串可以使用切片
my_str = 'hello'
# my_str = my_str[1]
# print(my_str)
# 切片使用格式
# my_str[起始下标：结束下标：步长]
# 起始下标默认是0结束下标不包含，步长是1
result = my_str[1:4]
print(result)
result = my_str[0:3]
print(result)
result = my_str[:3]
print(result)
result = my_str[2:5]
print(result)
# 使用负数方式切片
result = my_str[-3:]
print(result)

result = my_str[:]
print(result)

# 步长为负数表示从后往前取
result = my_str[-2:-5:-1]
print(result)

# 使用证书下标切片方式获取数据
result = my_str[3:0:-1]
print(result)

# 倒着获取字符串中的每个数据
result = my_str[::-1]
print(result)

result = my_str[::2]
print(result)
