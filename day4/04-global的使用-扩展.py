# 定义一个不可变全局变量
g_num = 10
print("函数外",g_num, id(g_num))


def modify():
    # 声明要修改全局变量
    global g_num
    g_num = 1
    print("函数内", g_num)
    print("函数内", id(g_num))


modify()
print(g_num)

# 定义一个可变类型的全局变量
g_list = [2,5]
print("函数外", id(g_list), type(g_list))


def modify1():
    # 在原有的数据上添加一条数据
    # 如果只是修改数据，那么这里可以不添加global
    # global g_list
    # g_list.append(6)
    g_list = [1, 2]
    print("函数内", g_list)
    print("函数内", id(g_list), type(g_list))


modify1()
print(g_list)


