import multiprocessing
import time


def show(name):
    print(multiprocessing.current_process())
    print(name)
    while True:
        print('show')
        time.sleep(0.2)


if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=show, args=('name',), daemon=True, name='d')
    sub_process.start()
    # 设置守护进程
    sub_process.daemon = True
    # 让子进程终止，销毁子进程
    # sub_process.terminate()
    time.sleep(2)
    print(multiprocessing.current_process())
    print('over')

