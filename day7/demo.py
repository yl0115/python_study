class MyIterator(object):
    __slots__ = ['my_list', 'index']

    def __init__(self, my_list, index):
        self.my_list = my_list
        self.index = index

    @property
    def set_index(self):
        return self.index

    @set_index.setter
    def set_index(self, index):
        if isinstance(index, int):
            self.index = index
        else:
            raise ValueError('Please enter valid data！')

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            result = self.my_list[self.index]
            self.index += 1
            return result
        raise StopIteration()


if __name__ == '__main__':
    MyList = [i for i in range(10)]
    MyIndex = 0
    my_iterator = MyIterator(MyList, MyIndex)
    for value in my_iterator:
        print(value, end=" ")




