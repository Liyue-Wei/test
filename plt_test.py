import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 7, 250000)   
y = np.sin(x)    
yy = np.cos(x)
yyy = np.tan(x)

fig, ax = plt.subplots()

ax.plot(x, y, linewidth=1.0)  
ax.set(xlim=(0, 6.282), xticks=np.arange(0, 6.282), ylim=(-1, 1), yticks=np.arange(-1, 1))

ax.plot(x, yy, linewidth=1.0)  
ax.set(xlim=(0, 6.282), xticks=np.arange(0, 6.282), ylim=(-1, 1), yticks=np.arange(-1, 1))

# ax.plot(x, yyy, linewidth=1.0)  
# ax.set(xlim=(0, 16), xticks=np.arange(0, 32), ylim=(-2, 2), yticks=np.arange(-2, 2))

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