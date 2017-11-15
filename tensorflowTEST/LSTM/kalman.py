import numpy as np
import matplotlib.pyplot as plt

def kalman_filter(measured,last_optimal,last_optimal_convarance):
    Q = 1.0     #measure
    R = 0.5     #drive
    drived = last_optimal + 0.1
    P = last_optimal_convarance + R     #variance of drived
    K = P/(P+Q) 
    print "K",K
    optimal = drived + (measured-drived)*K
    last_optimal_convarance = (1-K)*P
    return optimal,last_optimal_convarance

def generate_data():
    x = np.linspace(0,50,num=500)
    y = 2*x + np.random.normal(loc=0.0,scale=0.5 ,size=x.shape)
    return x,y

def measure_data(data):
    measured = data + np.random.normal(loc=0.0, scale=1)
    return measured

x,y_real= generate_data()

y_measured = []
y_optimal = []

for data in y_real:
    y_measured.append(measure_data(data))

opt =0 
lst_var =100
for i,data in enumerate(y_measured):
    opt,lst_var= kalman_filter(data,opt,lst_var)
    y_optimal.append(opt)


plt.plot(x,y_real,'r')
plt.plot(x,y_optimal,'b')
plt.plot(x,y_measured,'pink')
plt.show()
