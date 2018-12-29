import tensorflow as tf

# 1*2的矩阵
matrix1 = tf.constant([[3.0, 3.0]])
# 2*1的矩阵
matrix2 = tf.constant([[1.0], [2.0]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)
with tf.Session()as sess:
    result = sess.run(product)
    print(result)
