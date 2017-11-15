# -*- coding:utf-8 -*-
import tensorflow as tf
import numpy as np
from tensorflow.contrib import rnn
from tensorflow.examples.tutorials.mnist import input_data

state_size = 256
input_size = 28
time_step_size = 28
lr = 1e-3
batch_size = 128
class_num = 10

mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
print mnist.train.images.shape
_x = tf.placeholder(tf.float32, [batch_size,784])
y = tf.placeholder(tf.float32, [batch_size, class_num])
out_keep_holder = tf.placeholder(tf.float32)

x = tf.reshape(_x,[-1, time_step_size, input_size])
#构建模型
lstm_cell = rnn.BasicLSTMCell(num_units=state_size, state_is_tuple=True)
lstm_cell = rnn.DropoutWrapper(lstm_cell, input_keep_prob=1.0, output_keep_prob=out_keep_holder)

init_state = lstm_cell.zero_state(batch_size=batch_size, dtype=tf.float32)

output, current_state = tf.nn.dynamic_rnn(lstm_cell, x, initial_state=init_state, time_major=False)
last_output = output[:,-1,:]

W = tf.Variable(tf.truncated_normal([state_size, class_num],mean=0.0,stddev=0.1),dtype=tf.float32)
b = tf.Variable(tf.zeros(shape=[class_num]),dtype=tf.float32)

#y_pre = tf.nn.softmax( tf.matmul(last_output,W)+b )
y_pre = tf.matmul(last_output,W)+b 

#函数损失构建，评估函数，训练步骤
cross_entropy = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(logits=y_pre, labels=y))
train_op = tf.train.AdamOptimizer(lr).minimize(cross_entropy)

correct_prediction = tf.equal(tf.argmax(y_pre,1), tf.argmax(y,1))
accuracy_op = tf.reduce_mean(
    tf.cast(correct_prediction, tf.float32)
)
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(1000):
    batch = mnist.train.next_batch(batch_size)
    if i%50==0:
        fd ={_x:batch[0],y:batch[1],out_keep_holder:1.0}
        accuracy = sess.run(accuracy_op, feed_dict=fd)
        print accuracy
    fd ={_x:batch[0],y:batch[1],out_keep_holder:0.7}
    _,loss = sess.run([train_op, cross_entropy],feed_dict=fd)
