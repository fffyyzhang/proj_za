
import tensorflow as tf


# tf.gather 就是切片
def testGather():
    mat1 = tf.constant([[0,0,0], [1,1,1], [2,2,2,]])

    mat2 = tf.gather(mat1, [1,2])

    with tf.Session() as sess:
        ret = sess.run(mat2)
        print(ret)

# multply是元素乘，matmul是矩阵乘
def testMultiply():
    mat1 = tf.constant([[0, 0, 0], [1, 1, 1], [2, 2, 2, ]])
    mat2 = tf.constant([[0, 3, 0], [0, 3, 0], [0, 3, 0, ]])
    mat3 =  tf.constant([[0, 3, 0], [0, 3, 0], [0, 3, 0, ], [0, 3, 0, ]])

    mat = tf.multiply(mat1, mat2)
    mat = tf.matmul(mat1, mat2)

    mat = tf.multiply(mat1, mat3)

    with tf.Session() as sess:
        ret = sess.run(mat)
        print(ret)










if __name__ == "__main__":
    testMultiply()