import threading

lock = threading.Lock()
g_num = 0


def AA():
    lock.acquire()
    global g_num
    for i in range(100000):
        g_num += 1
    print("AA", g_num)
    lock.release()


def BB():
    lock.acquire()
    global g_num
    for i in range(100000):
        g_num += 1
    print("BB", g_num)
    lock.release()


if __name__ == '__main__':
    a = threading.Thread(target=AA)
    a.start()
    b = threading.Thread(target=BB)
    b.start()


