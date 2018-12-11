import tensorflow as tf

# 创建一个变量, 初始化为标量 0.
from tensorflow.contrib.learn.python.learn.datasets.mnist import extract_images, extract_labels

state = tf.Variable(0, name='counter')

# 创建一个op(方法),使得state值加1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)

# 启动图后, 变量必须先经过`初始化` (init) op 初始化,
# 首先必须增加一个`初始化` op 到图中.
init_op = tf.global_variables_initializer()

# 运行op
with tf.Session() as sess:
    sess.run(init_op)
    print(sess.run(state))

    for _ in range(3):
        sess.run(update)
        # 列表形式的run则为 array
        print(sess.run([state, new_value]))
