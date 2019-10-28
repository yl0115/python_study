# coding=gbk
# 1、打开源文件读取数据
# rb模式是比较通用的模式可以兼容不同的文件
file_src = open('1.txt', 'rb')
# 2、打开目标文件写入数据
# 可以指定文件拷贝路劲
dst_file = open('3副本.txt', 'wb')
# 循环读取
while True:
    file_data = file_src.read(1024)
    # 判断数据是否完成
    # if len(file_data) > 0:
    if file_data:
        # 表示有数据
        # 把原文件中数据写入到目标文件
        dst_file.write(file_data)
    else:
        print("数据读取完成：", file_data)
        break


dst_file.close()
file_src.close()



