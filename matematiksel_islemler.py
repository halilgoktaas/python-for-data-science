import numpy as np
v= np.array([1,2,3,4,5])
v/5
v * 5 / 10

v ** 2

np.subtract(v,1)
np.add(v,1)
np.mean(v)
np.sum(v)
np.max(v)

#numpy ile iki bilinmeyenli denklem çözümü
# 5 * x0 + x1 = 12
# x0 + 3*x1 = 10
a = np.array([[5,1],[1,3]])
b = np.array([12,10])
np.linalg.solve(a,b)