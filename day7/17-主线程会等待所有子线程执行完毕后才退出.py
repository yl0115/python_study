import threading
import time


def AA():
    print("AA", threading.current_thread())
    # 这个代码是在子线程中执行
    while True:
        print('AA')
        time.sleep(0.2)


if __name__ == '__main__':
    print("main", threading.current_thread())
    # target指定的目标函数会在子线程中执行
    # daemon设置守护主线程
    s1 = threading.Thread(target=AA, daemon=True)
    # 设置守护线程,主线程退出子线程直接销毁不再执行对应代码
    # s1.setDaemon(True)
    s1.start()
    time.sleep(1)
    print('over')
    # 总结：主线程会等待子线程执行完成以后程序再退出
