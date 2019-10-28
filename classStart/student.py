class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print("%s:%s" % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('bart Simpson', 51)
lisa = Student('lisa Simpson', 90)

bart.print_score()
result = bart.get_grade()
print(result)


def print_score(std):
    print("%s:%s" % (std.name, std.score))


print_score(bart)

result = lisa.get_grade()
print(result)
bart.age = 8
print(bart.age)
print(bart)

