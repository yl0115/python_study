# coding=gbk
# file = open('4.txt', 'w', encoding='utf-8')
# file.write('abc')
# file.close()
import os  # 文件和文件夹操作的相关模块
import shutil  # 文件操作的高级模块

# 重命名,目标文件必须要存在，才能重命名否则报错
# os.rename('4.txt', '444.txt')
# 创建文件夹
# os.mkdir("AAA")
# 修改文件夹名
# os.rename('AAA', 'VVV')

# 在文件夹BBB中创建文件
# 1、指定路劲创建
# file = open('VVV/t.txt', 'w', encoding='utf-8')
# file.write('ad')
# file.close()
# 2、切换到BBB目录创建，默认路劲是py文件操作目录
# 查看呢操作目录的路径
# current_path = os.getcwd()
# print(current_path)
# 切换到指定路劲
# current_path = os.chdir("VVV")
# curren = os.getcwd()
# print(curren)
# file = open('3.txt', 'w', encoding='utf-8')
# file.write('ac')
# file.close()

# ----------------------------------------------------------------
# 修改文件夹及文件夹下的文件
# os.renames('VVV/t.txt', 'CCC/3.txt')

# 查看目录下有哪些文件名列表信息
# file_name = os.listdir('CCC')
# print(file_name)



# os.chdir('CCC')
# c = os.getcwd()
# print(c)
# 当前目录的写法，点.表示当前目录
# file_name = os.listdir(".")
# file_name = os.listdir()
# print(file_name)




# --------------------删除文件or文件夹---------------------------
# 删除文件
# os.remove("CCC/3.txt")
# 删除文件夹
# os.rmdir("CCC")
# rmdir只能删除空目录
# os.rmdir("BBB")


# 删除目录树
# shutil.rmtree("BBB")


# -----------------------------扩展--------------------------------
# 获取1.txt的绝对路劲，从根目录算起的路劲就叫做绝对路劲
# 相对路劲，从当前目录算起的路劲就是叫做相对路劲
path = os.path.abspath("1.txt")
print(path)

# 根据绝对路劲获取路劲中的文件名
file_name = os.path.basename(path)
print(file_name)

# 获取文件名和文件后缀
file_name, file_extend = os.path.splitext(file_name)
print(file_name, file_extend, sep="@")
