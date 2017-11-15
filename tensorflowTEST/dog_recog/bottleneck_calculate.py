import tensorflow as tf
import scipy.io as sio
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

data_train = sio.loadmat("./lists/train_list.mat")
data_test = sio.loadmat("./lists/test_list.mat")

img_train = ["Images/"+item[0][0] for item in data_train['file_list']]
lbl_train = [int(item[0]) for item in data_train['labels']]

img_test = ["Images/"+item[0][0] for item in data_test['file_list']]
lbl_test = [int(item[0]) for item in data_test['labels']]

sess = tf.Session()
sess.run(tf.global_variables_initializer())

data_dict = {}
for i in range(1,121):
    data_dict[i]=[]

for i,item in enumerate(img_train):
    img_string = gfile.FastGFile(item,'rb').read()
    lbl_index = lbl_train[i] 
    bn = sess.run(bottleneck_tensor,feed_dict={jpeg_data_tensor:img_string})
    bottleneck_value = np.squeeze(bn)
    data_dict[lbl_index].append(bottleneck_value)
    if i%100==0:
        print i
file_save = open('./data_train.pkl','wb')
pickle.dump(data_dict,file_save)

#clear the data_dict
data_dict = {}
for i in range(1,121):
    data_dict[i]=[]
#fill the data_dict, the key of which is the label, while the value is result of caculating
for i,item in enumerate(img_test):
    img_string = gfile.FastGFile(item,'rb').read()
    lbl_index = lbl_test[i] 
    bn = sess.run(bottleneck_tensor,feed_dict={jpeg_data_tensor:img_string})
    bottleneck_value = np.squeeze(bn)
    data_dict[lbl_index].append(bottleneck_value)
    if i%100==0:
        print i
file_save = open('./data_test.pkl','wb')
pickle.dump(data_dict,file_save)


print "ending..."
