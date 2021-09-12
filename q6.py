from matplotlib import mlab
import matplotlib.pyplot as plt
import numpy as np

data = np.load("data-2class.npz")
for k in data.keys():
    print(k)
d = data['d']
l = data['l'].flatten()
# print(d)
# print(l)
label = l
plt.xlim([-5,10])
plt.ylim([-5,10])
d0 = []
d1 = []
for i in range(len(d)):
    if l[i] == 0:
        d0.append(d[i])
    else:
        d1.append(d[i])
# print(d0)
# for i in range(len(d0)):
#     plt.scatter(d0[i][0], d0[i][1], c = 'red')
# for i in range(len(d1)):
#     plt.scatter(d1[i][0], d1[i][1], c = 'blue')


class Gauss:
    """Class for computing the probability density function of a Gaussian distribution with given
    mean vector and covariance matrix, at point x"""

    def __init__(self, mu, sigma):
        """Initialise a distribution with mean mu and covariance sigma

        Precompute and store everything that is not dependent
        on the datapont, so as to keep things efficient"""
        D = np.size(mu)

        self.mu = mu
        self.icov = np.linalg.inv(sigma)
        sign, ld = np.linalg.slogdet(sigma)
        if sign != 1:
            print("Sign=", sign)

        self.lognum = D * np.log(2 * np.pi) + ld

    def logprob(self, x):
        """return log(p(x))"""
        d = x - self.mu
        return -.5 * (self.lognum + np.dot(np.dot(d, self.icov), d))

    def prob(self, x):
        """return p(x)"""
        return np.exp(self.logprob(x))


mean0 = [np.mean(d0[0]),np.mean(d0[1])]
sigma0 = np.cov(d0)
# print(mean0)
# print(sigma0)
Gauss0 = Gauss(mean0, sigma0)
#
for i in range(10):
    plt.scatter(i, Gauss0.prob(i), c = 'green')

# plt.plot([-5,18.5], [8,-5], linewidth = 0.5, c = 'green')
# plt.show()