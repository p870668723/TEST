import tensorflow as tf
import pickle
import glob
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.python.platform import gfile

with gfile.FastGFile("./classify_image_graph_def.pb",'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())

bottleneck_tensor, jpeg_data_tensor = tf.import_graph_def(
    graph_def,
    None,
    return_elements=['pool_3/_reshape:0','DecodeJpeg/contents:0']
)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

flowers = glob.glob("./flower_photos/*/*")
flower_labels = [int(item.split('/')[2]) for item in flowers]
print flower_labels

data_dict = {0:[], 1:[], 2:[], 3:[], 4:[]}
for i,item in enumerate(flowers):
    img_string = gfile.FastGFile(item,'rb').read()
    lbl = int(item.split('/')[2])

    bn = sess.run(bottleneck_tensor,feed_dict={jpeg_data_tensor:img_string})
    bottleneck_value = np.squeeze(bn)

    data_dict[lbl].append(bottleneck_value)
    if i%100==0:
        print i
file_save = open('./data.pkl','wb')
pickle.dump(data_dict,file_save)

print "ending..."
