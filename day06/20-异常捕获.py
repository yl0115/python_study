# coding=gbk
# 提示：多数异常类都是继承Exception
# try:
#     # 可能发生异常的代码，放到try语句里面
#     num1 = input("请输入第一个数字：")
#     num2 = input("请输入第二个数字：")
#     result = int(num1)+int(num2)
#     print(result)
# except Exception as e:  # e表示异常对象
#     # 捕获到的异常会在except里面进行处理
#     print("请输入合法数字")
#     print(e)
# num1 = input("请输入第一个数字：")
# num2 = input("请输入第二个数字：")
# result = int(num1)+int(num2)
# print(result)


# 了解：可以捕获多个异常类型
try:
    name = 'zs'
    # del name
    # 在try里面遇到了代码异常，那么不会再执行try里面的代码，会直接执行except
    print(name)
    result = 1/1
    print(result)
except (NameError, ZeroDivisionError) as e:
    print(e, type(e))
else:
    print("没有异常会执行else")
finally:
    print("有没有异常都会执行finally")

