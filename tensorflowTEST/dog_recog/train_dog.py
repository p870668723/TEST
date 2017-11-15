import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import  tensorflow.contrib.slim as slim
import random
import scipy.io as sio

def parse_func(filenames, labels):
    image_string = tf.read_file(filenames)
    image_tensor = tf.image.decode_jpeg(image_string)
    image_tensor = tf.image.resize_images(image_tensor,[120,120],method=tf.image.ResizeMethod.NEAREST_NEIGHBOR)
    return tf.cast(image_tensor, tf.float32), tf.cast(labels, tf.int32)
    #return filenames, labels

data_train = sio.loadmat("./lists/train_list.mat")
data_test = sio.loadmat("./lists/test_list.mat")

img = ["Images/"+item[0][0] for item in data_train['file_list']]
lbl = [item[0] for item in data_train['labels']]

filenames = tf.convert_to_tensor(img)
labels = tf.convert_to_tensor(lbl)

dataset = tf.data.Dataset.from_tensor_slices((filenames,labels))
dataset = dataset.map(parse_func)
dataset = dataset.shuffle(buffer_size = 10000)
dataset = dataset.batch(10)
dataset = dataset.repeat(20)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

#sess=tf.Session()
#sess.run(iterator.initializer)
#sess.run(tf.global_variables_initializer())
#
#img_,lbl_ = sess.run(next_element)

x_holder = tf.placeholder(tf.float32, shape=[None, 120, 120 ,3])
y_holder = tf.placeholder(tf.int32, shape=[None])
keep_prob = tf.placeholder(tf.float32)

net = slim.conv2d(x_holder, 32, [5,5],scope="conv1")
net = slim.max_pool2d(net,[2,2], scope='pool1')
net = slim.conv2d(net, 64, [5,5],scope='conv2')
net = slim.max_pool2d(net,[2,2], scope='pool2')
net = slim.conv2d(net, 128, [5,5],scope='conv3')
net = slim.max_pool2d(net,[2,2], scope='pool3')
#net = slim.conv2d(net, 128, [5,5],scope='conv4')
net = slim.flatten(net)
net = slim.fully_connected(net, 1024, scope="fn1")
net = slim.dropout(net, keep_prob, scope='drop')
logits = slim.fully_connected(net, 120, activation_fn=None, scope='fn2')

precision = tf.reduce_mean(
    tf.cast(
        tf.equal(
            tf.argmax(logits,-1),
            tf.cast(y_holder,tf.int64)
            ),
        tf.float32
    )
)

one_hot_labels = tf.one_hot(y_holder, 120, axis=-1)
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=one_hot_labels)
)
train_op = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)

sess=tf.Session()
sess.run(iterator.initializer)
sess.run(tf.global_variables_initializer())

loss =0
for i in range(20000):
    img_,lbl_ = sess.run(next_element)
    _,loss = sess.run([train_op,cross_entropy],feed_dict={x_holder:img_, y_holder:lbl_, keep_prob:0.7})
    if i%10==0:
        print 'precision: ',sess.run(precision,feed_dict={x_holder:img_, y_holder:lbl_, keep_prob:1})
        print 'loss: ',loss
    #img_ = sess.run(tf.cast(img_,tf.uint8))
    #print lbl_
    #for i in range(9):
    #    plt.subplot(251+i)
    #    plt.imshow(img_[i])
    #plt.show()