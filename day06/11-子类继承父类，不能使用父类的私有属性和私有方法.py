# coding=gbk

class Person(object):
    def __int__(self):
        self.__age = 10

    def __show(self):
        print('���ﶨ����һ��˽�з���')

    def test(self):
        print("test")


class Student(Person):
    def show(self):
        # ���ʸ����˽�����Ժ�˽�з���
        # print(self.__age)
        # self.__show()
        self.test()

    pass


student = Student()
student.show()
# print(student.__age)
# student.__show()


# �ܽ᣺����̳и��಻��ֱ��ʹ�ø���˽�����Ժ�˽�з���
