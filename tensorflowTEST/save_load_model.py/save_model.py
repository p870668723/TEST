import tensorflow as tf

x = tf.placeholder(tf.float32,shape=None,name='ph')
b = tf.constant(3.0,dtype=tf.float32)
c = tf.Variable(initial_value=3,trainable=True)
y = tf.multiply(x,b,name='out')

saver = tf.train.Saver()
sess = tf.Session()
sess.run(tf.global_variables_initializer())
print sess.run(c)
saver.save(sess,"./model/mm.ckpt")

sess.close()