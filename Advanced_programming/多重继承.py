class Animal(object):
    pass


class Mammal(Animal):  # 哺乳动物
    pass


class Bird(Animal):  # 鸟
    pass


class Runnable(object):
    def run(self):
        print('running...')


class Flyable(object):
    def fly(self):
        print('Fiying...')


class Dog(Mammal, Runnable):  # 狗
    pass


class Bat(Mammal, Flyable):  # 蝙蝠
    pass


class Parrot(Bird, Flyable):  # 鹦鹉
    pass


class Ostrich(Bird, Runnable):  # 鸵鸟
    pass


