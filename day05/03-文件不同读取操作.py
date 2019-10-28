# coding=gbk
# file = open('1.txt', "r", encoding='utf-8')
# content = file.read(2)
# print(content)
# file.close()
"""
    read、readline、readlines读取文件操作
    读取指定长度数据，提示：如果是r模式读取的是指定数据的长度
    注意点：在utf-8编码下，一个汉字占用三个字节，一个字符占用一个字节
    rb读的时字节数
"""


# 根据指定的文件指针读取数据
file = open('1.txt', 'rb')
# 查看文件指定的位置上
result = file.tell()
print(result)
# 设置文件指定的位置
file.seek(4)
result = file.tell()
print(result)
result = file.read()
content = result.decode('utf-8')
print(content)
file.close()



# 读取一行输入
file = open('1.txt', 'rb')
# 读取一行数据，当读取数据的时候遇到'\n'表示读取数据结束
value = file.readline()
value = value.decode('utf-8')
print(value)
file.close()


# 多行
file = open('1.txt', 'rb')
value = file.readlines()
for i in value:
    print(i.decode('utf-8'), sep="", end="")

