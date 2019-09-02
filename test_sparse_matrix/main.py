from scipy.sparse import lil_matrix, csr_matrix,dia_matrix, coo_matrix







# 测试内容：矩阵切片返回的结果是否会重新编号,改变shape
# 测试结果：
# 1. coo不能切片，必须转csr
# 2. 切片之后返回的矩阵是一个独立的矩阵，shape会变化，id会从0开始重新编号
def testSlice():
    mat = coo_matrix( ([1, -1, 3], ([1, 2, 3], [1, 2, 3]) ), shape=(4, 4))
    mat = csr_matrix(mat)
    print(mat.todense())
    mat2 = mat[[3,2]]

    mat2_coo = coo_matrix(mat2)
    print(mat2.todense())

    d=1











if __name__ == "__main__":
    testSlice()