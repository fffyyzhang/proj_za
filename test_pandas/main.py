
import pandas as pd
import numpy as np

import copy

#测试一下对于dataframe，浅拷贝是不是够用了
def testDFCopy():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    df1 = copy.copy(df)
    df['one']  =-1
    print(df)
    print(df1)

    d=1


def testDrop():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    df = df.drop(1)
    print(df)

def testSelect():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    df = df[~df['one'].isin([0,4])]
    print(df)



# liy 貌似as_matrix和values是相等的，而且warning提示，这个方法过时了， 用.values!
def testAsMatrix():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    mat = df.as_matrix()
    print(mat)

    l = list(mat)
    print(l)

    mat2 = df.values
    print(mat2)

    print(mat == mat2)

    print(mat.flatten())

# 用指针df1添加列，会改变原来所指向的df
def testAppendCol():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    df1= df
    df['col'] = 1
    print(df)

#测试了一下，指定random state，每次panda sample出来的数据都是一样的了
def testRandomRow():
    df = pd.DataFrame(np.arange(256).reshape((16, 16)))
    df1 = df.sample(frac=0.5, random_state=None)
    print(df1)


def testDFInit():
    l = [(1,2), (3,4)]
    df = pd.DataFrame(l)
    print(df)


def test_init_dict():
    l = [{'a':1}, {'a':2, 'b':1}]
    df = pd.DataFrame(l)
    d=1


def test_concat():
    df1 = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    df2 = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['five', 'six', 'seven', 'eight'])

    df3 = pd.concat([df1]*100)
    d=1

#测试一下values这个东西是不是引用，还是复制
# 注意：value是引用的关系！！！！， 修改value这个arr的数值，会直接修改到dataframe里面的数值
def test_values():
    l = [(1,2), (3,4)]
    df = pd.DataFrame(l)
    v = df.values
    v[1] = [100,100]
    d=1


#测试group by里面的grp是原dataframe的复制抑或是指针？对其进行修改是否改变原始df中的数值
def test_group_by():

    d=1

#测试一下dataframe对行切片之后，对切片修改是否会改变原来dataframe里面的数值：
#会的！切片返回的不是copy！ 可以猜测pandas的设计原则还是尽量修改原dataframe，能不copy的
#地方都不copy

# def test_inplace():
#     df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
#     #df2 = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['five', 'six', 'seven', 'eight'])
#     df1 = df['one']
#     df1.iloc[1] = 100
#     print(df)

#给切片添加一列的情况下，被添加的列不会出现在原dataframe中
def test_inplace():
    df = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['one', 'two', 'three', 'four'])
    #df2 = pd.DataFrame(np.arange(16).reshape((4, 4)), columns=['five', 'six', 'seven', 'eight'])
    df1 = df['one']
    df1['five'] = -1
    print(df)

if __name__ == "__main__":
    test_inplace()






























