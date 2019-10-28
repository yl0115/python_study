my_str = "橘子,苹果,栗子"
# 以逗号形式分割
print(my_str.split(','))
my_url = "https://www.baidu.com"
# 开头是否已http开始
print(my_url.startswith('https'))
# 结尾是否已.com结尾
print(my_url.endswith('.com'))
# 替换某一个元素
print(my_url.replace('tt', 'n'))
# 查找某个元素的下面
print(my_url.find("t"))  # 未找到返回-1
print(my_url.index('t'))  # 未找到直接报错

# 需求：把字符串以指定字符串分割数据成为三部门
my_str = "aaabccc"
print(my_str.partition("b"))
# jion:根据指定字符串拼接数据，前提是最终的数据是字符串
flog_str = '-'
my_str = 'abc'
result = flog_str.join(my_str)
print(result)

my_list = ['a', 'c', 'd']
result = my_str.join(my_list)
print(result)

# 去掉空格
flag_str = " buhaoyisi "
print(flag_str.strip())
print(flag_str.lstrip())
print(flag_str.rstrip())

# 去除指定数据
my_str = "7"
print(my_str.strip('a'))


my_si = ['a', 'c', 'd']
result = my_str.join(my_si)
print("杨雷" + result)
