import threading
from time import ctime, sleep


"""
官方文档
https://docs.python.org/zh-cn/3/library/threading.html
"""


def task(func):
    for _ in range(3):
        print("{}. {}".format(func, ctime()))
        sleep(1)


# 1.创建锁
# mutex_lock = threading.Lock()
# 2.加锁
# mutex_lock.acquire()
# 3.释放锁
# mutex_lock.release()

threads = []
t1 = threading.Thread(target=task, args=('任务1',))
threads.append(t1)
t2 = threading.Thread(target=task, args=('任务2',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print("finish {}".format(ctime()))
