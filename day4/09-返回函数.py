# 返回函数：在函数里面返回一个函数
def sho():
    def inner():
        print("hahh")
    # 返回一个函数
    return inner


# 获取返回的函数
new_func = sho()
# 执行返回的函数
new_func()



def fuhao(fu):
    if fu == '+':
        def jia(num1, num2):
            result = num1 + num2
            return result
        return jia
    elif fu == '-':
        def jian(num1, num2):
            result = num1-num2
            return result
        return jian


new_funct = fuhao('-')
result = new_funct(5, 6)
print(result)
