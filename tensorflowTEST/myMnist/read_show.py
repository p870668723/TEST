import os
import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np
import time
import matplotlib.pyplot as plt
import struct


def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,'%s-labels.idx1-ubyte'% kind)
    images_path = os.path.join(path,'%s-images.idx3-ubyte'% kind)
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',lbpath.read(8))
        labels = np.fromfile(lbpath,dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',imgpath.read(16))
        images = np.fromfile(imgpath,dtype=np.uint8).reshape(len(labels), 784)
    return images, labels

img, lbl = load_mnist("./")

def reference(input_data, keep_prob):
    x = tf.reshape(input_data,[-1,28,28,1])
    #pics = net[...,0]
    #pics = tf.reshape(pics,[-1,10,10,1])
    tf.summary.image('image_input',x,10)
    net = slim.conv2d(x,32,[5,5],scope='conv1')
    net = slim.max_pool2d(net, [2,2], scope='pool1')
    net = slim.conv2d(net,64,[5,5],padding='valid',scope='conv2')
    net = slim.max_pool2d(net, [2,2], scope='pool2')
    net = slim.flatten(net)
    net = slim.fully_connected(net, 1024, scope='fc1')
    net = slim.dropout(net, keep_prob, scope='dropout')
    result = slim.fully_connected(net,10, activation_fn=None, scope='fc2')
    return result

x_ = tf.placeholder(tf.float32,[None,None])
y_ = tf.placeholder(tf.int32,[None])
keep_prob = tf.placeholder(tf.float32)

labels = tf.one_hot(y_,10,axis=-1)
logits = reference(x_, keep_prob)
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits , labels=labels))
train_op = tf.train.GradientDescentOptimizer(0.001).minimize(cross_entropy)

evals = tf.equal(tf.cast(tf.argmax(logits, axis=-1),tf.int32),y_)
evalss =tf.reduce_mean(tf.cast(evals,tf.float32))

tf.summary.scalar('cross_entropy',cross_entropy)
tf.summary.scalar('precision',evalss)
merged = tf.summary.merge_all()
saver = tf.train.Saver()
sess = tf.Session()

writer = tf.summary.FileWriter("./sum/",sess.graph)


#saver.restore(sess,"./model/model_900.ckpt")
##for test
#trainable_var = [item.name for item in tf.trainable_variables()]
#print sess.run(trainable_var[0])

sess.run(tf.global_variables_initializer())
for i in range(1,1000):
    i = i*10
    _,summary,ls = sess.run([train_op,merged,cross_entropy],feed_dict={x_:img[i:i+10], y_:lbl[i:i+10], keep_prob: 0.6})

    writer.add_summary(summary,i)

    if i%1000==0:
        precision = sess.run(evalss, feed_dict={x_:img[i:i+50], y_:lbl[i:i+50], keep_prob:1})
        saver.save(sess,"./model/model_%d.ckpt"%(i/10))
        print ls
        print precision

print "finish training..."
test_img, test_lbl = load_mnist('./','t10k')
precision = sess.run(evalss, feed_dict={x_:test_img[0:100], y_:test_lbl[0:100], keep_prob:1})
print precision