# 循环（for while）：根据条件循环执行某种操作
# 提示：while会玄幻哦按段条件是否成立，如果条件成立会执行while循环语句，但是if判断只会判断一次
# 1-5循环5次
num = 1
while num <= 5:
    print(num)
    num += 1
print("==================")
# for循环一般结合range使用，range是一个范围
for i in range(1, 6):
    print(i, end="#")
print("$$$$$$$$$$$$$$$$$$$")
for i in range(6):
    print(i)

# for循环和while循环可以结合if使用

