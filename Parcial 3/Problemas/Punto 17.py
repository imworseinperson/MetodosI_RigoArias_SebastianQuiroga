import numpy as np
import matplotlib.pyplot as plt 
import sympy as sp 

#Funciones

def f(x,y):
    f = (x + sp.I*y)**3-1
    f = f.expand()
    return sp.re(f),sp.im(f)

def NewtonRapshon(Fn,Jn,p,itmax=1000,precision=1e-6):
    x = p
    error = 1
    it = 0
    while error > precision and it < itmax:
        IFn = Fn(x[0],x[1])
        IJ = Jn(x[0],x[1])
        Inv_Jn = np.linalg.inv(IJ)
        x1 = x - np.matmul(Inv_Jn,IFn)
        error = np.max(np.abs(x1-x))
        x = x1
        it += 1
    return x

#Variables

x = sp.Symbol('x',real=True)
y = sp.Symbol('y',real=True)

#Procedimiento

f0,f1 = f(x,y)
F = [f0,f1]
M = sp.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            M[i,j] = sp.diff(F[i],x,1)
        else:
            M[i,j] = sp.diff(F[i],y,1)

Fn = sp.lambdify([x,y],F,'numpy')
Mn = sp.lambdify([x,y],M,'numpy')
p = np.array([0.5, 0.5])
N = 300
x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)
z0 = np.array([-0.5,np.sqrt(3)/2])
z1 = np.array([-0.5,-np.sqrt(3)/2])
z2 = np.array([1,0])

Fractal = np.zeros((N,N), np.int64)
for i in range(N):
    for j in range(N):
        a = NewtonRapshon(Fn,Mn,np.array([x[i],y[j]]))
        d0 = np.max(np.abs(z0-a))
        d1 = np.max(np.abs(z1-a))
        d2 = np.max(np.abs(z2-a)) 
        minimo = min(d0,d1,d2)
        if d0  == minimo:
            Fractal[i][j] = 20
        elif d1 == minimo:
            Fractal[i][j] = 100
        else:
            Fractal[i][j] = 255
         
plt.imshow(Fractal, extent=[-1,1,-1,1])
plt.show()
#Se demora un poco en aparecer la gráfica