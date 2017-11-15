import tensorflow as tf
from tensorflow.contrib import slim
import matplotlib.pyplot as plt
import numpy as np

img = plt.imread("./h.jpg")
w = slim.model_variable(
    'weight',
    shape=[10, 10, 3, 3],
    initializer = tf.truncated_normal_initializer(stddev=1),
    regularizer = slim.l2_regularizer(0.03),
    device='/CPU:0'
)
input_holder = tf.placeholder(tf.float32,[None, None, 3])
net = slim.conv2d(input_holder, 3, ( 3, ), scope='conv1_1')


regul_loss = tf.add_n(slim.losses.get_regularization_losses())




with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    product = sess.run(net, feed_dict={input_holder:img })
    print(sess.run(regul_loss))
    #pp = np.reshape(product, [product.shape[0], -1])
    plt.imshow(product)
    plt.show()