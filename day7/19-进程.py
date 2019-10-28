# 进程：每次创建一个进程操作系统会给这个进程分配相应的运行资源，一个进程里面默认有一个线程
# 真正干活的是线程，进程只提供资源
# 使用多进程也可以完成任务
import multiprocessing
import time


def show():
    for i in range(5):
        print('show')
        time.sleep(0.2)


def info():
    for i in range(5):
        print('info')
        time.sleep(0.2)


if __name__ == '__main__':
    first = multiprocessing.Process(target=show)
    second = multiprocessing.Process(target=info)
    first.start()
    second.start()




