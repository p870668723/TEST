import tensorflow as tf

saver =tf.train.import_meta_graph("./model/mm.ckpt.meta")

sess = tf.Session()
saver.restore(sess, "./model/mm.ckpt")
x = tf.get_default_graph().get_tensor_by_name('ph:0')
y = tf.get_default_graph().get_tensor_by_name('out:0')
print sess.run(y,feed_dict={x:4.0})