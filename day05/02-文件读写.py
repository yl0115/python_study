# 文件访问模式：
# 1、r表示只读，如果文件不存在会报错
# 2、w表示只写
# 3、a表示追加写入
# 4、rb表示以二级制方式读取文件数据
# 5、wb表示以二进制方式写入文件数据
# 6、ab表示以二级制方式追加写入文件数据
# 7、r+、w+、a+支持读写，但是要看前面的主模式
# 8、rb+、wb+、ab+支二进制读写

print("----------------r模式--------------")
# 打开文件用open函数
file = open('1.txt', 'r', encoding='utf-8')  # 默认为r模式，r表示只读
# 读取文件中的数据
result = file.read()
print(result)
# 关闭文件
file.close()
print("---------------w模式-----------------")
# w模式：如果文件不存在就会创建一个并写入
# w模式：如果文件存在，那么会把文件中原有数据先清空，如果在写入
# 如果使用w模式每次打开都会先清空在写入
# 提示：在window上开发python需要指定编码格式
file1 = open('1.txt', 'w', encoding='utf-8')
file1.write("hello你好")
# 打开写入多次是不会清空的
file1.write("1111")
file1.close()

print("-----------------a模式追加写入数据------------------")

file3 = open('1.txt', 'a', encoding="utf-8")
file3.write("aaa")
file3.close()

print("--------------rb模式以二进制方式读取文件---------------------")
# ValueError: binary mode doesn't take an encoding argument:以二进制形式读写的文件不需要加“ut-8”
file4 = open('1.txt', 'rb')
value = file4.read()
# 对二进制数据进行utf-8解码操作
result = value.decode('utf-8')
print(result)
file4.close()

print("------------------wb模式以二进制方式写入数据-----------------------------")
file5 = open('1.txt', 'wb')
# 字符串到二进制叫做编码
# 对字符串进行utf-8编码得到二进制数据
value = '"老师"'
result = value.encode('utf-8')
file5.write(result)
file5.close()

print("--------------------------ab模式以二进制方式追加写入数据-----------------------")
file5 = open('1.txt', 'ab')
# 字符串到二进制叫做编码
# 对字符串进行utf-8编码得到二进制数据
value = '"老师"'
result = value.encode('utf-8')
file5.write(result)
file5.close()

print("-----------------------r+读写--------------------------")
# 为了兼容不同的系统，只要没有看到b模式就可以使用encoding指定编码格式
file6 = open('1.txt', 'r+', encoding='utf-8')
# 写入数据时不能清空数据，把指定数据中的数据替换成写入数据，文件中其他数据依然存在
file6.write('a')
file6.close()

