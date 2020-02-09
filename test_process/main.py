#测试多进程和queue

from multiprocessing import Queue, Process
import time, random


a = 1

def producer(name, food, q):
    print(a)
    for i in range(4):
        time.sleep(random.randint(1,2))
        f = '%s生产了%s%s'%(name, i, food)
        print(f)
        q.put(f)

def consumer(name, q):
    while True:
        food = q.get()
        if food is None:
            print('%s没有获取到东西！' %(name))
            break
        print('\033[31m%s消费了%s\033[0m' %(name, food))
        time.sleep(random.randint(1,2))



if __name__ == "__main__":
    q = Queue(20)
    p1 = Process(target=producer, args=('p1', '包子', q))
    p2 = Process(target=producer, args=('p2', '稀饭', q))
    p1.start()
    p2.start()
    c1 = Process(target=consumer, args=('c1',q))
    c2 = Process(target=consumer, args=('c2', q))
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    q.put(None)
    q.put(None)