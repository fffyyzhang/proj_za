
import numpy as np



# 看看diff是不是差集,,,,是的，，，算的是差集
def testDiff():
    set1 = set([1,2,3,4])
    set2 = set([3, 4, 5, 6])
    print(set1.difference(set2))


#测试一下set能不能直接转np.array
def testSetToArray():
    set1 = set([1,2,3,4,5,5,5])
    arr = np.array(set1)
    d=1

# 测试一下集合能不能用enumerate
def testSetEnum():
    set1 = set([1, 2, 3, 4, 5, 5, 5,6])
    for i, v in enumerate(set1):
        print(i, v)


# 对set可以直接调用sorted，返回的东西是一个list
def testSortSet():
    s1 = set([3,2,1,2,4])
    print(sorted(s1))

if __name__ == "__main__":
    testSortSet()