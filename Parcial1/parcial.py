import numpy as np
import matplotlib.pyplot as plt

def Function(x):
    return np.exp(-x)-x

x = np.linspace(-1,1, 200)
y=Function(x)
plt.plot(x,y)
plt.axhline(y=0, color='r')
plt.show()

def muller(x):
    x0 = x[125]
    x1 = x[175]
    x2 = x[150]
    x3 = 99999999 

    i=0

    while (i < 100) and abs((Function(x3)) < 1*(10**-10)):

        difx0x1 = (Function(x1)-Function(x0))/(x1-x0)
        difx1x2 = (Function(x2)-Function(x1))/(x2-x1)
        segunda = (difx1x2-difx0x1)/(x2-x0)
        a = segunda
        b = difx0x1-(x0+x1)*a
        c = Function(x0)-(x0*difx0x1)+(x0*x1*a)

        if b < 0:
            x3=(-2*c)/(b-(np.sqrt((b**2)-(4*a*c))))
        else:
            x3=(-2*c)/(b-(np.sqrt((b**2)+(4*a*c))))
        print(x3)
        if x3 > 0:
            x0 = np.argmin(np.abs(Function(x) - x3))
            x3 = np.argmin(np.abs(Function(x) - x3))
        else:
            x1 = np.argmin(np.abs(Function(x) - x3))
            x3 = np.argmin(np.abs(Function(x) - x3))
            
        if x2 > x0 or x2 < x1:
            x2 = (x0+x1)/2
        
        i += 1
        print(i)
              
    
    return x3

print(x[muller(x)])