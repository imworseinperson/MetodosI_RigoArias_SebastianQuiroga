import numpy as np
import matplotlib.pyplot as plt

#Derivación punto 8

def Function(x):
    return np.tan(x)

def DerivadaDerecha(x,h):
    
    d = 0.
    
    if h != 0:
        d = (Function(x+h) - Function(x))/h
        
    return d

def DerivadaCentral(x,h):
    
    d = 0.
    
    if h != 0:
        d = (Function(x+h) - Function(x-h))/(2*h)
        
    return d

x = np.linspace(0.1, 1.1, 100)

h = 0.01

deriprogre = DerivadaDerecha(x, h)
dericentral = DerivadaCentral(x, h)

plt.plot(x, deriprogre, color='blue')
plt.plot(x, dericentral, color='red')
plt.show()