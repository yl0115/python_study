# 序列化：把内存中的数据保存到本地，可以做到持久化存储
import pickle  # 比较通用，可以序列化任意对象类型

# 序列化
# my_list = [{"name": "张胜男", "age": 16}, {"name": "王鹏", "age": 19}]
# file = open('my_list.serialize', 'wb')
# pickle.dump(my_list, file)
# file.close()

# 反序列化
# file = open('my_list.serialize', 'rb')
# result = pickle.load(file)
# print(result)
# file.close()


class Student(object):
    def __init__(self):
        self.name = '张三'
        self.age = 15


# stu = Student()
# file = open('stu.serialize', 'wb')
# 序列化
# pickle.dump(stu, file)
# file.close()

file = open('stu.serialize', 'rb')
# 反序列化
result = pickle.load(file)
print(result.name, result.age)
file.close()
