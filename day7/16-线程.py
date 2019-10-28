# 线程：执行代码的一个分支，默认程序中只有一个线程，
import time
import threading


def test_AA(content):
    for i in range(content):
        time.sleep(0.3)
        print('test_AA', i)


def test_BB(conut):
    for i in range(conut):
        time.sleep(0.3)
        print('test_BB', i)


if __name__ == '__main__':
    # 创建子线程执行对应代码
    # target表示目标函数
    # args表示以元祖的形式传参
    # sub_Thread = threading.Thread(target=test_AA, args=(3,))  # 以元祖传参
    # kwargs表示以字典方式给函数传参，key必须和形参一致
    sub_Thread1 = threading.Thread(target=test_AA, kwargs={"content": 6})  # 以字典传参
    sub_Thread1.start()
    sub_Thread2 = threading.Thread(target=test_BB, args=(5,))
    # 启动线程，只有启动才会启动线程
    sub_Thread2.start()

    # 主函数执行
    # test_BB()
    # 线程执行是无序的由cpu调度决定

