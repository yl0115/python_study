# 全局变量
g_score = 100


def show_info():
    print('show_info')


def sum_num(num1, num2):
    result = num1+num2
    return result


# 主模块：执行那个模块那个就是主模块
# 判断是否是主模块
if __name__ == '__main__':
    # 测试sum_num函数是否有问题
    value = sum_num(1, 3)
    print(value)
    # 查看主模块
    print(__name__)
