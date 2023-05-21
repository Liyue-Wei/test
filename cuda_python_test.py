import cupy as cp
# import numpy as np
import os
import time

t_now = float(time.time())
for i in range(100000):
    x = cp.arange(100000000).reshape(10000, 10000).astype('f')
# print(x, x.sum(axis=1))
print("count with cupy by cuda {}\n".format(float(time.time())-t_now))

'''
t_now = float(time.time())
for i in range(1000):
    x = np.arange(1000000).reshape(1000, 1000).astype('f')
print(x, x.sum(axis=1))
print("count with numpy by cpu {}\n".format(float(time.time())-t_now))
'''

os.system('pause')
