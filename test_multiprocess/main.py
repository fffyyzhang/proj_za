import multiprocessing
from tqdm import tqdm
from time import sleep
import time
import numpy as np
from multiprocessing import Pool

# prints [0, 1, 4, 9, 16]

# # method 2: imap
# for y in pool.imap(f, xs):
#     print (y)            # 0, 1, 4, 9, 16, respectively

#用pool来跑的函数必须定义在top-level，不能是local函数
def f(x):

    return x[0] * x[1]

def test1():


    pool = multiprocessing.Pool(processes=2)
    xs = [1]*100000

    #method 1: map
    # print (pool.map(f, xs))
    pbar = tqdm(total = len(xs))
    for i in pool.map(f, xs):
        pbar.update(1)

    pool.close()
    pool.join()



def next_t():
    for i in range(1000):
        yield (1,i)

def f(x):
    arr1 = np.ones((5,5))
    arr2 = np.zeros((5,5))
    return arr1, arr2

def test2():

    ret = []
    pool = multiprocessing.Pool(processes=1)
    #xs = [(1,2), (1,3), (1,4), (1,5)]
    N = 10000000
    xs =  range(N)

    #method 1: map
    # print (pool.map(f, xs))
    pbar = tqdm(total = N)
    for i in pool.map(f, xs):
        ret.append(i)
        pbar.update(1)

    pool.close()
    pool.join()
   # sleep(1)
    #print(ret)


def _foo(my_number):
   square = my_number * my_number
   time.sleep(0.5)

def test3():
    N = 10000000
    xs =  range(N)

    with Pool(20) as p:
        r = list(tqdm(p.imap(f, xs), total=N))


if __name__ == "__main__":
    test3()