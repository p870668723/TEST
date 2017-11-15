import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

c_matrix = tf.constant(128,dtype=tf.int16, shape=[120,120,3])
def read_img(filenames):
    image_string = tf.read_file(filenames)
    image_decoded = tf.image.decode_jpeg(image_string)
    image_resized = tf.image.resize_images(image_decoded, [120,120],method=tf.image.ResizeMethod.NEAREST_NEIGHBOR )
    image_resized = tf.cast(image_resized, tf.int16)
    image_resized = image_resized-c_matrix
    #image_resized = image_decoded
    return tf.cast(image_resized,tf.float32)

saver = tf.train.import_meta_graph("./model/mm.ckpt.meta")

img_batch = []
with tf.Session() as sess:
    saver.restore(sess,"./model/mm.ckpt")
    in_ph = tf.get_default_graph().get_tensor_by_name("x:0")
    result = tf.get_default_graph().get_tensor_by_name("fc_2/BiasAdd:0")
    keep = tf.get_default_graph().get_tensor_by_name("keep:0")

    rs = tf.argmax(result,axis=-1)
    sess.run(tf.global_variables_initializer())
    for i in range(1,6):
        img = sess.run(read_img("./test%d.jpg"%i))
        img_batch.append(img)
    print sess.run(rs,feed_dict={in_ph:img_batch, keep:1.0})