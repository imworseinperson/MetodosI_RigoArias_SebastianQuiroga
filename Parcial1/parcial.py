import numpy as np
import matplotlib.pyplot as plt

def Function(x):
    return np.exp(-x)-x

x = np.linspace(-1,1, 200)
y=Function(x)
plt.plot(x,y)
plt.axhline(y=0, color='r')
plt.show()

