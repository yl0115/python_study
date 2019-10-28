# continue:结束本次循环可以继续下次循环,整个循环不一定结束
# break：跳出当前循环，当前循环结束
# continue和break不能单独使用智能在循环使用

num = 1
while num <= 5:
    if num == 2:
        num += 1
        # 执行continue结束本次循环，continue后面的代码不执行
        continue
    print(num)
    num += 1
else:
    print('本次循环结束')
num = 1
while num <= 5:
    if num == 2:
        num += 1
        # 执行break结束当前循环，break后面的代码不执行
        break
    print(num)
    num += 1
else:
    # 如果循环语句里面执行了break那么else不会执行
    print('本次循环结束')
print("====================for======================")
for i in range(1, 5):
    if i ==2:
        continue
    print(i)
else:
    print("循环语句结束")
print("=============break==========")
for i in range(1, 5):
    if i == 2:
        break
    print(i)
else:
    print("循环语句结束")

# 循环中只要不执行break就会执行else，前提是要有else
result = input("请输入姓名：")
for i in ['张三', '李四']:
    if i == result:
        print(i)
        break
else:
    print("没有找到")

