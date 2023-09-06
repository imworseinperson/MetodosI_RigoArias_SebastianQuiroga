import numpy as np

def Function(x):
    return np.exp(-x)-x

x = np.linspace(-1,1, 100)
y=Function(x)
