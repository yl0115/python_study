import multiprocessing


def add_list(queue):
    for i in range(3):
        queue.put(i)
        print(i)


def read_list(queue):
    while True:
        # 判断队列是否为空
        if queue.empty():
            break
        value = queue.get()
        print(value)


if __name__ == '__main__':
    # 默认队列里面可以放入任意多个数据
    # 3：表示队列中最大有三个数据
    queue = multiprocessing.Queue(3)
    # 创建两个子进程
    s1 = multiprocessing.Process(target=add_list, args=(queue,))
    s2 = multiprocessing.Process(target=read_list, args=(queue,))
    # 启动进程
    s1.start()
    # 进程等待，主进程等待子进程执行完毕后让后面的代码执行
    s1.join()
    s2.start()
# 多任务：使用线程和进程
# 从资源角度来说线程更佳节省资源
# 进程消耗的资源比较多

# 从代码稳定性来说：多进程要比多线程稳定性要强，因为一个进程挂不会影响其他进程




