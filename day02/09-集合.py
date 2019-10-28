# 集合(set)：以大括号表现形式的数据集合，集合里面不能有重复的数据，集合是无序的
# 集合不能根据下标获取数据和修改数据，可以添加和删除
my_set = {'hello', 1, 4, 'abc'}
print(my_set, type(my_set))

# 添加数据
my_set.add(5)
print(my_set)

# 删除数据remove删除数据必须存在，不然会崩溃；discard删除指定数据，数据不存在不会报错。
my_set.remove('abc')
my_set.discard('hello')
print(my_set)
# 取值
for i in my_set:
    print(i)
#定义空的集合时不能使用大括号

m = {}
mm = set()
print(type(m))
print(type(mm))

# 集合可以对容器类型数据进行去重
my_list = [1, 1, 2, 2, 3, 6]
myser = set(my_list)
print(myser)


# 列表、元祖、集合三者之间可以相互转换
