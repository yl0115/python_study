# coding=gbk
# 1、打开源文件读取数据
# rb模式是比较通用的模式可以兼容不同的文件
file_src = open('1.txt', 'rb')
# 读取文件全部数据
file_data = file_src.read()
# 2、打开目标文件写入数据
# 可以指定文件拷贝路劲
dst_file = open('3副本.txt', 'wb')
# 把原文件中数据写入到目标文件
dst_file.write(file_data)

dst_file.close()
file_src.close()



