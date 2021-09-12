import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import timeit2

# s = np.sqrt(2.)
# print("The square root of 2 is:", s)

d = np.load('data.npz')
for k in d.keys():
    print('', k, 'which is of size', d[k].shape)

v = d['v']

print("The order of V", v.shape)
print("The two-norm of v", np.sqrt(v.T.dot(v)))

print("Timing inner product")
# %timeit v.T.dot(v)
# %time for t in [1,2,3,4,5]: print("  Number of elements >",t,":",len([x for x in v if x>t]))
# %time for t in [1,2,3,4,5]: print("  Using numpy, the number of elements >",t,":",np.sum(v>t))
# def countLargerThan(t):
#     count=0
#     for x in v:
#         if x>t:
#             count+=1
#     return count
# def countAll():
#     for t in range(1,6):
#         print("  Using for loops, the number of elements >",t,":",countLargerThan(t))
# %time countAll()