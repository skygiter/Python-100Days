"""
实现进程间的通信


"""
import multiprocessing
import os


def sub_task(queue):
    print('子进程进程号:', os.getpid())
    counter = 0
    while counter < 1000:
        queue.put('Pong')
        counter += 1


if __name__ == '__main__':
    print('当前进程号:', os.getpid())
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=sub_task, args=(queue,))
    p.start()
    counter = 0
    while counter < 1000:
        queue.put('Ping')
        counter += 1
    p.join()
    print('子任务已经完成.')
    for _ in range(2000):
        print(queue.get(), end='')
