import numpy as np
a= np.random.randint(10,size=10)
a[0]
a[0:5]
a[0] = 999

m= np.random.randint(10,size = (3,5))
m[0,0]
m[1,1]
m[2,3]
m[2,3] = 999
m [1,:]
m[0:2, 0:3]