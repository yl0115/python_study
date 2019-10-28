# 把字符串写入内存
import io

# StringIO的操作和文件写入和读取的操作很类是
str_io = io.StringIO()
# 向内存写入字符串数据
str_io.write('hello')
str_io.write('world')


# # 获取数据
# content = str_io.getvalue()
# print(content)


# 另一种获取数据方法

# 设置文件指针的位置到文件开头
str_io.seek(0)
result = str_io.read(2)  # 读取指定长度
print(result)

