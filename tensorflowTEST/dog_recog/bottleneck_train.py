import tensorflow as tf
import random
import pickle
import numpy as np
import tensorflow.contrib.slim as slim

print "load the bottleneck data..."
pk_train = open("bottleneck_value/data_train.pkl",'rb')
pk_test = open("bottleneck_value/data_train.pkl",'rb')
train_dict = pickle.load(pk_train)
test_dict = pickle.load(pk_test)
pk_train.close()
pk_test.close()

def prepare_data(train_dict, size):
    label_bat = np.random.randint(120,size=size)
    image_bat = []
    for item in label_bat:
        image_bat.extend(random.sample( train_dict[item+1],1))
    return image_bat, list(label_bat)

x_holder = tf.placeholder(tf.float32, shape=[None, 2048])
y_holder = tf.placeholder(tf.int32, shape=[None])
keep_holder = tf.placeholder(tf.float32)

net = slim.fully_connected(x_holder, 1024, scope='fc_1')
net = slim.dropout(net,keep_holder,scope='dropout')
logits = slim.fully_connected(net, 120, activation_fn=None, scope='fc_2')

cross_entropy = tf.reduce_mean(
    tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=y_holder)
)

evaluation = tf.reduce_mean(
    tf.cast(
        tf.equal(
            tf.cast(tf.argmax(logits,axis=-1), tf.int32),
            y_holder
            ),
        tf.float32
    )
)
train_op = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(10000):
    img_bat, lbl_bat = prepare_data(train_dict, 10)
    _, loss = sess.run([train_op,cross_entropy],feed_dict={x_holder:img_bat, y_holder:lbl_bat, keep_holder:0.6})
    if i%100==0:
        img_bat, lbl_bat = prepare_data(test_dict,200)
        precision = sess.run(evaluation, feed_dict={x_holder:img_bat, y_holder:lbl_bat, keep_holder:1})
        print "precision: ",precision
        print "caculate loss: ",loss

img_bat, lbl_bat = prepare_data(test_dict,1000)
prec = sess.run(evaluation, feed_dict={x_holder:img_bat, y_holder:lbl_bat, keep_holder:1})
print "final precision: ",prec