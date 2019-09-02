
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



if __name__ == "__main__":
    testAppendCol()