from scipy.sparse import lil_matrix, csr_matrix,dia_matrix
import numpy as np







# 用dict of list 初始化向量，最省劲的方法就是用networkx
# nx.adjacency_matrix(nx.from_dict_of_lists(graph))...
def test_lil_assign():
    d=1



def test_diagnal():
    m = csr_matrix( ([1,2,3], ([0,1,2],[0,1,2])), (3,3))
    #np.newaxis = None
    #m  = m[np.newaxis, :] #错的

    arr= np.array(range(100))
    arr2 = arr[None, :]


    print(m.todense())
    d=1
def test3():
    data = np.array([[1, 2, 3, 4]]).repeat(3, axis=0)
    offsets = np.array([0, -1, 2])
    #这里的offet指的是主对角线上面的线(正数)，负数就是主对角线下面的线
    m = dia_matrix((data, offsets), shape=(4, 4)).toarray()
    print(m)

    d=1




if __name__ == "__main__":
    test3()