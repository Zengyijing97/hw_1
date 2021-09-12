import numpy as np
import matplotlib.pyplot as plt
import math

def normal_distribution(x, mean, sigma):
    return np.exp(-1*((x-mean)**2)/(2*(sigma**2)))/(math.sqrt(2*np.pi) * sigma)

mean1, sigma1 = 0, 1
mean2, sigma2 = 0, 2
mean3, sigma3 = 0, 3
x = np.linspace(-5, 5, 100)

y1 = normal_distribution(x, mean1, sigma1)
y2 = normal_distribution(x, mean2, sigma2)
y3 = normal_distribution(x, mean3, sigma3)

plt.plot(x, y1, 'b', label='σ=1')
plt.plot(x, y2, 'orange', label='σ=2')
plt.plot(x, y3, 'g', label='σ=3')
plt.legend()
plt.grid()
plt.show()