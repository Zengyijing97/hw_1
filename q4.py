import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import math

d = np.load('data.npz')
for k in d.keys():
    print('', k, 'which is of size', d[k].shape)

def normal_distribution(x, mean, sigma):
    return np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)

v2 = d['v2']
mean = np.mean(v2)
sigma = np.var(v2)

x = np.linspace(-5, 5, 100)
print(v2)
print(mean)
print(sigma)
y = normal_distribution(x, mean, sigma)
plt.xlim(-5,5)
plt.hist(v2, bins = 20, density = True, stacked=True, color = 'green')
plt.plot(x, y, 'r')
plt.show()