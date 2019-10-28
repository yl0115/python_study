# 迭代器： 在类里面有__iter__()、__next__()的方法创建的对象就是迭代器；作用：根据数据位置获取下一个位置的数据
class MyIterator(object):
    def __init__(self):
        self.my_list = [4, 5, 19]
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.my_list):
            # 获取迭代器中的下一个值
            result = self.my_list[self.current_index]
            self.current_index += 1
            return result
        else:
            # 抛出停止迭代异常
            raise StopIteration()


# 创建迭代器
my_iterator = MyIterator()
# # 使用__next__()函数获取迭代器中下一个值
# result = my_iterator.__next__()
# print(result)
# result = my_iterator.__next__()
# print(result)
# result = my_iterator.__next__()
# print(result)
for value in my_iterator:
    print(value)



