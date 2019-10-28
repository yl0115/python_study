class Student(object):
    __slots__ = ('name', 'age', '_score')


    def get_score(self):
        return self._score


    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


stu = Student()
stu.set_score(100)
print(stu.get_score())
stu.set_score(1)
stu.age = 1000
print(stu.age)


class Animal(object):
    __slots__ = ('name', 'age', '_score')

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value <  0 or value > 100:
            raise ValueError('score must between 0~100')
        self._score = value


a = Animal()
a.score = 20
print(a.score)
a.score = 11  # 实际转化为a.set_score()
print(a.score)  # 实际转化为a.get_score()


class Dog(object):
    @property
    def brith(self):
        return self._brith

    @brith.setter
    def brith(self, value):
        self._brith = value

    @property
    def age(self):
        return 2015 - self._brith


d = Dog()

d.brith = 2011
print(d.brith)
print(d.age)

