import numpy as np
import matplotlib.pyplot as plt

a = np.loadtxt('raw_data.txt')
b = np.loadtxt('predict_data.txt')
x_data = [item[0] for item in a]
y_data = [item[1] for item in a]
y_predict = b
plt.plot(x_data, y_data,'*')
plt.plot(x_data, y_predict, 'r')
plt.show()
