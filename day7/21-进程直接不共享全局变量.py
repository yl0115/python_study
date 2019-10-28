import multiprocessing

my_list = []


def add_list():
    for i in range(5):
        my_list.append(i)
    print("add:", my_list)


def read_list():
    print("read:", my_list)


if __name__ == '__main__':
    # 创建两个子进程
    s1 = multiprocessing.Process(target=add_list)
    s2 = multiprocessing.Process(target=read_list)
    # 启动进程
    s1.start()
    # 进程等待，主进程等待子进程执行完毕后让后面的代码执行
    s1.join()
    s2.start()



