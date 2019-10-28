#  自定义异常类
class CustomException(Exception):
    def __init__(self, content):
        self.content = content

    #  抛出异常信息描述
    def __str__(self):
        return '我是自定义异常,因为数据不是a,而是%s' % self.content


content = input("请输入数据：")
if content != 'a':
    #  抛出自定义异常
    raise CustomException(content)
    # raise只能抛出异常类型
else:
    print(content)
