import numpy as np
import matplotlib.pyplot as plt
import math
def average_data(x):
    return sum(x)/len(x)

def var_data(x,mean):
    temp = {}
    for i in range(len(x)):
        temp[i] = (x[i] - mean)** 2
    print(temp)
    sum = 0
    for i in range(len(x)):
        sum += temp[i]
    return sum/len(x)

d = np.load('data.npz')
v2 = d['v2']
mean = average_data(v2)
var = var_data(v2,mean)
print(mean)
print(var)