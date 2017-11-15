import pickle
import numpy as np
from tensorflow.contrib import slim as slim
import random
import tensorflow as tf

pk = open('data.pkl','rb')
data_dict = pickle.load(pk)
print "load the bottleneck data\nthe data is formed in dictionary",len(data_dict[1][1])

def prepare_data(data_dict):
    eval_data = {0:[],1:[],2:[],3:[],4:[]}
    train_data = {0:[],1:[],2:[],3:[],4:[]}
    for i in range(5):
        for j,item in enumerate(data_dict[i]):
            if j%5==0:
                eval_data[i].append(item)
            else:
                train_data[i].append(item)
    return eval_data, train_data

def next_batch(data, size):
    batch_lbl = np.random.randint(5,size=size)
    batch_img = []
    for item in batch_lbl:
        batch_img.extend(random.sample(data_dict[item],1))
    return batch_img, list(batch_lbl)

eval_data, train_data = prepare_data(data_dict)

x = tf.placeholder(tf.float32, [None,2048])
y_ = tf.placeholder(tf.int32, [None])
keep_= tf.placeholder(tf.float32)

net = slim.fully_connected(x, 1024, scope='fc_1')
net = slim.dropout(net, keep_, scope='dropout')
results = slim.fully_connected(net, 5, scope='fc_2',activation_fn=None)

bools = tf.equal(tf.cast(tf.argmax(results,axis=-1),tf.int32),y_)
evals = tf.reduce_mean( tf.cast(bools, tf.float32))


one_hot = tf.one_hot(y_,5,axis=-1)
cross_entropy = tf.reduce_mean(
     tf.losses.softmax_cross_entropy(logits=results ,onehot_labels=one_hot)
     )
tf.summary.scalar("loss", cross_entropy)
train_op = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)

merged = tf.summary.merge_all()
sess = tf.Session()
writer = tf.summary.FileWriter('./sum',sess.graph)

sess.run(tf.global_variables_initializer())

for i in range(5000):
    if i%100==0:
        img,lbl = next_batch(train_data,50)
        print sess.run(evals,feed_dict={x:img,y_:lbl,keep_:1})

    img,lbl = next_batch(train_data,10)
    _,summary = sess.run([train_op,merged], feed_dict={x:img,y_:lbl,keep_:0.7})

    writer.add_summary(summary,i)
    #print loss
writer.close()

img,lbl = next_batch(eval_data,400)
print sess.run(evals,feed_dict={x:img,y_:lbl,keep_:1})