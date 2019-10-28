# 全局变量：在函数外定义的变量叫做全局变量，全局变量可以在不同的函数内使用
score = 100


def show():
    global score  # 表示要对全局变量score数据进行修改
    score = 99
    print("分数", score)


def show_score():
    print("分数", score)

show()
show_score()
