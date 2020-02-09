
import numpy as np


#测试一下numpy array 最后一个维度设置成1的情况
def main():
    arr1 = np.array([[1,2,3], [1,2,3], [1,2,3]])
    arr2 = arr1[:, None]


    d=1


# 测试一下对numpy array 用coo的方式进行赋值
def testArrayAssign():
    mat = np.full((3,3), 0)
    mat[[0,1], [0,1]] = [1,1]
    print(mat)
    d=1


def testConditionalAssign():
    arr1 = np.array([[1.0, 2.0, 3.0], [1.0, 1., 1.], [1., 2., 4.]])
    arr1[arr1 > 1] = np.inf
    print(arr1)



# 使用np.delete可以删除array的特定id的行/列
def testArrDelete():
    arr1 = np.array([[1, 2, 3], [1, 1, 1], [1, 2, 4]])
    print(np.delete(arr1, [1], axis =0))


# 测试一下矩阵切片赋值来调整矩阵的行顺序,来reorder
def test_mat_reorder():
    mat1 = np.array(range(16)).reshape(4,4)
    mat1[[0, 1]]= mat1[[1, 2]] #有重叠也能正常赋值
    print(mat1)

# 测试：二维矩阵的shuffle
# 结果：内部的那个维是不改变的
# 结果2：直接用random.shuffle对二维的arr进行重排会出现错误
# 结论：对二位arr的第一维重排，使用np.shuffle或者tolist()之后使用random模块的shuffle函数
def testShuffle():
    arr1 = np.array(range(36)).reshape(6,6)
    np.random.shuffle(arr1)
    print(arr1)

    import random
    arr1 = np.array(range(36)).reshape(6, 6)
    ll = arr1.tolist()
    random.shuffle(ll)
    print(ll)

    d=1

def testSum():
    arr1 = np.array([[1,1,1]])
    arr2 = np.array([[1,1,1]])
    print(np.sum([arr1,arr2]))



def testRandomSeed():
    arr = np.array(range(100))
    from numpy.random import RandomState
    np.random.seed(RandomState(1234567890))
    #np.random.set_state(1234)
    np.random.shuffle(arr)
    print(arr)
    #np.random.seed(1234)
    np.random.shuffle(arr)

    print(arr)



def test_col_assign():
    arr = np.zeros((5,5))
    import  pandas as pd
    df = pd.DataFrame(np.ones((5,5)), columns=['1','2', '3', '4', '5'])
    arr[:, 2] = df['3'].values
    d=1


if __name__ == "__main__":
    test_col_assign()