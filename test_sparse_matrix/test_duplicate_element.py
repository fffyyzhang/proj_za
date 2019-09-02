import numpy as np
from scipy.sparse import csr_matrix, lil_matrix

#矩阵的(1,1)位置被两次赋值为不同的数值时，csr_matrix会自动报错
def doTest():
    mat = csr_matrix([1,-1,3], ([1,1,3], [1,1,2]), shape=(4,4))
    d=1


def testAssign():
    mat1 = lil_matrix((4,4))

    data = [
        [1,1,1,0],
        [1, 1, 1, 0],
    ]

    mat2 = lil_matrix(data, shape=(4,4))

    mat1[3:5,:] = mat2[0:2, :]

    d=1


#测试一下用 == x 这种panda的方式对矩阵元素进行选取切片,确实可以这样写
def testQP():
    mat = csr_matrix(([1,2,3], ([1,2,3],[1,2,3])), shape=(4,4))
    #liy -如果不加这个dtype=np.float32，则返回的是一个true false形式的矩阵

    mat_tmp = np.sum(mat)
    print(mat_tmp.todense())

    mat2 =  csr_matrix(mat ==1, dtype=np.float32)
    mat2
    print(mat2.todense())
    d=1



if __name__ == "__main__":
    testQP()