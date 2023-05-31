import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 7, 16384)   
y = np.sin(x)    
yy = np.cos(x)
yyy = np.tan(x)
tol = 20
yyy[yyy > tol] = np.nan
yyy[yyy < -tol] = np.nan

fig, ax = plt.subplots()

# ax.plot(x, y, linewidth=1.0)  
# ax.set(xlim=(0, 6.282), xticks=np.arange(0, 6.282), ylim=(-1, 1), yticks=np.arange(-1, 1))
# 
# ax.plot(x, yy, linewidth=1.0)  
# ax.set(xlim=(0, 6.282), xticks=np.arange(0, 6.282), ylim=(-1, 1), yticks=np.arange(-1, 1))

ax.plot(x, yyy, linewidth=1.0)  
ax.set(xlim=(0, 6.282), xticks=np.arange(0, 6.282), ylim=(-20, 20), yticks=np.arange(-1, 1))

plt.show()

'''
import matplotlib.pyplot as plt

x = [1, 2, 3]
y1 = [1, 2, 3]
y2 = [3, 2, 1]

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
'''