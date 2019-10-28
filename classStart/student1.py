class Student1(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print("%s:%s" %(self.__name, self.__score))

    def print_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student1('bart Simpson', 20)
bart.print_score()
bart.set_score(1)
result = bart.print_grade()
print(result)
print(bart)

