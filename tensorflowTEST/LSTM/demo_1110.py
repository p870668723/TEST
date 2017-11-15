import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

sess = tf.Session()

def generate_data():
    x = np.linspace(0,62.8,1000)
    y = np.sin(x)
    
def model(input_tensor,label_tensor):
    lstm = tf.nn.rnn_cell.BasicLSTMCell(30,1.0,True,None,None)
    multi_lstm = tf.nn.rnn_cell.MultiRNNCell([lstm]*2,True)
    x_ = tf.unstack(input_tensor, 10, 1)
    output, _ = tf.nn.dynamic_rnn(multi_lstm,x_,dtype=tf.float32)
    y_prediction = output[-1]
    loss = -tf.reduce_mean( label_tensor * tf.log(y_prediction) )
    train_op = tf.train.AdagradOptimizer(0.1).minimize(loss)
    return y_prediction, loss, train_op

input_holder = tf.placeholder(tf.float32, shape=[1,10])
label_holder = tf.placeholder(tf.float32)

y_prediction, loss, train_op = model(input_holder, label_holder)
ii = [range(10)]
ll = 10
sess.run(tf.global_variables_initializer())
_, l = sess.run([train_op, loss], feed_dict={input_holder:ii, label_holder:ll})
print l




