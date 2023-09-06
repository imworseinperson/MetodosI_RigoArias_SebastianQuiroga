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


## EJERCICIO DE LAGRANGE ##

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
import math

def Lagrange(x,X,i):
    
    L = 1
    
    for j in range(X.shape[0]):
        if i != j:
            L *= (x - X[j])/(X[i]-X[j])
            
    return L
def Interpolate(x,X,Y):
    
    Poly = 0
    
    for i in range(X.shape[0]):
        Poly += Lagrange(x,X,i)*Y[i]
        
    return Poly

# Lee los datos del archivo CSV
url = "https://raw.githubusercontent.com/asegura4488/Database/main/MetodosComputacionalesReforma/Parabolico.csv"
datos = pd.read_csv(url)

# Extrae los datos de X e Y
X = datos["X"].values
Y = datos["Y"].values

x = np.linspace(0.,7.,100)
y = Interpolate(x,X,Y)

a = sym.Symbol('x',real=True)

# Obtener la funcion
f = Interpolate(a,X,Y)
f = sym.simplify(f) 

plt.scatter(X,Y)
plt.plot(x,y)
plt.show()


# Calcular la derivada de f con respecto a x (df/dx)

f = sym.diff(f, a)
Vx = sym.solve(f, a)
Vx = float(Vx[0])
y_max = f.evalf(3,subs={x:Vx})

print(y_max)

