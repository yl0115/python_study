import types


class Animal(object):
    def run(self):
        print("Animal is running...")


class Dog(Animal):
    def run(self):
        print("Dog is running")

    def eat(self):
        print("Eating meat..")


class Cat(Animal):
    def run(self):
        print("Cat is running")


class Tortoise(Animal):
    def run(self):
        print("Tortoise is running slowly...")


class Ai(object):
    def run(self):
        print("AI running")


class Husky(Dog):
    def run(self):
        print('Husky is running...')


an = Animal()
an.run()
d = Dog()
d.run()
c = Cat()
c.run()
print('--------------------------------------------')

a = list()
b = Animal()
c = Dog()
print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


print("----------------------------------------------")
run_twice(Tortoise())
run_twice(Cat())
run_twice(Dog())
run_twice(Animal())
run_twice(Ai())
print('+++++++++++++++++++++++++++++++++++++++++++++++')
print(type(c))


print('*************************************************')

print(type(Dog) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


a = Animal()
d = Dog()
h = Husky()


print(isinstance(h, Husky))
print(isinstance(h, Dog))
print(isinstance(h, Animal))
if isinstance(d, Dog) and isinstance(d, Animal):
    print('wwe')
else:
    print('12')

if isinstance(d, Husky):
    print('Yes')
else:
    print('No')

if isinstance('a', str) and isinstance(1, int):
    print('Yes')
else:
    print('No')

print(isinstance([1, 2, 3, 4, 5], (list, tuple)))
print(isinstance((1, 2, 3, 4, 5, 6), (list, tuple)))
print(dir('ABC'))
print(len('ABC'))
print('abc'.__len__())


class MyDog(object):
    def __init__(self):
        self.x = 9

    def __len__(self):
        return 100

    def power(self):
        return self.x * self.x


dog = MyDog()
print(len(dog))

print('abc'.upper())
print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x*self.x


obj = MyObject()
result = obj.power()
print(result)

print(hasattr(obj, 'x'))  # 有属性‘x’吗？
print(obj.x)
print(hasattr(obj, 'y'))
# print(obj.y)
print(setattr(obj, 'y', 5))  # 设置一个属性‘y’
print(getattr(obj, 'y'))  # 获取属性‘y’

print(obj.y)


print('------------------------------')
print(getattr(obj, 'z', 404))  # 获取属性‘z’，如果不存在，则返回默认值404
print(getattr(obj, 'power'))   # 获取属性‘power’
print(hasattr(obj, 'power'))  # 有属性power吗？
fn = getattr(obj, 'power')
print(fn)
fn()








