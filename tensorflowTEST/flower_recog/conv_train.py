import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.contrib.slim as slim
import glob
import time
c_matrix = tf.constant(128,dtype=tf.int16, shape=[120,120,3])
def parse_func(filenames, labels):
    image_string = tf.read_file(filenames)
    image_decoded = tf.image.decode_jpeg(image_string)
    image_resized = tf.image.resize_images(image_decoded, [120,120],method=tf.image.ResizeMethod.NEAREST_NEIGHBOR )
    image_resized = tf.cast(image_resized, tf.int16)
    image_resized = image_resized-c_matrix
    #image_resized = image_decoded
    return tf.cast(image_resized,tf.float32),tf.cast(labels,tf.int32)

filenames = glob.glob("./flower_photos/*/*")
labels = [int(item.split('/')[2]) for item in filenames]
#hold_label = [chr(65+item) for item in labels]
filename = tf.convert_to_tensor(filenames)
label = tf.convert_to_tensor(labels)
num = tf.placeholder(tf.int64)

dataset = tf.data.Dataset.from_tensor_slices((filename,label))
dataset = dataset.map(parse_func)
dataset = dataset.shuffle(buffer_size=3600)
dataset = dataset.batch(num)
dataset = dataset.repeat(20)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()

x = tf.placeholder(tf.float32, [None,120,120,3], name='x')
y_ = tf.placeholder(tf.int32, [None])
keep_= tf.placeholder(tf.float32,name='keep')

initializer = tf.truncated_normal_initializer(0.01)
padding = 'SAME'
regularizer = slim.l2_regularizer(0.0005)

tf.summary.image("input_image",x,max_outputs=10)
net = slim.conv2d(x, 32, [5,5],
                    padding=padding,
                    #weights_initializer = initializer,
                    #weights_regularizer = regularizer,
                    scope = 'conv1')
net = slim.max_pool2d(net, [2,2], scope='pool1')
net = slim.conv2d(net, 64, [5,5],
                    padding=padding,
                    #weights_initializer = initializer,
                    #weights_regularizer = regularizer,
                    scope = 'conv2')
net = slim.max_pool2d(net, [2,2], scope='pool2')
net = slim.conv2d(net, 128, [5,5],
                    padding=padding,
                    #weights_initializer = initializer,
                    #weights_regularizer = regularizer,
                    scope = 'conv3')
net = slim.max_pool2d(net, [2,2], scope='pool3')
net = slim.flatten(net)
net = slim.fully_connected(net, 1024, scope='fc_1')
net = slim.dropout(net, keep_, scope='dropout')
results = slim.fully_connected(net, 5, scope='fc_2',activation_fn=None)
print results.name

bools = tf.equal(tf.cast(tf.argmax(results,axis=-1),tf.int32),y_)
evals = tf.reduce_mean( tf.cast(bools, tf.float32))

one_hot = tf.one_hot(y_,5,axis=-1)
cross_entropy = tf.reduce_mean(
     tf.losses.softmax_cross_entropy(logits=results ,onehot_labels=one_hot)
     #tf.nn.softmax_cross_entropy_with_logits(logits=results ,labels=one_hot)
     )
tf.summary.scalar("loss", cross_entropy)
train_op = tf.train.AdamOptimizer(0.0001).minimize(cross_entropy)

merged = tf.summary.merge_all()
sess = tf.Session()
writer = tf.summary.FileWriter('./sum',sess.graph)
saver = tf.train.Saver()

sess.run(iterator.initializer,feed_dict={num:10})
sess.run(tf.global_variables_initializer())

for i in range(5000):
    nt = sess.run(next_element, feed_dict={num: 30})
    if i%20==0:
        print sess.run(evals,feed_dict={x:nt[0],y_:nt[1],keep_:1})

    _,summary = sess.run([train_op,merged], feed_dict={x:nt[0],y_:nt[1],keep_:0.7})

    writer.add_summary(summary,i)
saver.save(sess, "./model/mm.ckpt")
sess.close()
    #print loss

"""test code"""
#for i in range(10):
#    nt = sess.run(next_element)
#    print type(nt[0][0][0][0][0])
#    print (nt[0][0][0][0][0])
#    print type(nt[1][0])
#
#    fig = plt.figure()
#    for j in range(6):
#        a = fig.add_subplot(2,3,j+1)
#        plt.imshow(nt[0][j])
#        a.set_title(nt[1][j])
#    plt.show()
