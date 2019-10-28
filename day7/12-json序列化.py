import json  # 只能支持部分数据类型，不通用，比如：列表、数组、字典、int类型；自定义类型不支持
# import pickle


# my_list = [{"name": "李四", "age": 78}, {"name": "张三", "age": 15}]
# file = open('my_list.txt', 'w', encoding='utf-8')
# json序列化
# result = json.dump(my_list, file)
# file.close()

# file = open('my_list.txt', 'r', encoding='utf-8')
# # json反序列化
# result = json.load(file)
# print(result)
# file.close()


class Student(object):
    def __init__(self):
        self.name = '李四'
        self.age = 23


# file = open('stu.txt', 'w', encoding='utf-8')
# stu = Student()
# # 序列化对象，本质上是把对象的属性进行保存
# print(stu.__dict__)
# json.dump(stu.__dict__, file)
# file.close()

file = open('stu.txt', 'r', encoding='utf-8')
result = json.load(file)
print(result)
file.close()


