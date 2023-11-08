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
func = [f0,f1]
M = sp.zeros(2,2)

for i in range(2):
    for j in range(2):
        if j==0:
            M[i,j] = sp.diff(func[i],x,1)
        else:
            M[i,j] = sp.diff(func[i],y,1)

fn = sp.lambdify([x,y],func,'numpy')
Mn = sp.lambdify([x,y],M,'numpy')
N = 300
x = np.linspace(-1,1,N)
y = np.linspace(-1,1,N)
a = np.array([-0.5,np.sqrt(3)/2])
b = np.array([-0.5,-np.sqrt(3)/2])
c = np.array([1,0])

Image = np.zeros((N,N), np.int64)
for i in range(N):
    for j in range(N):
        k = NewtonRapshon(fn,Mn,np.array([x[i],y[j]]))
        a2 = np.max(np.abs(a-k))
        b2 = np.max(np.abs(b-k))
        c2 = np.max(np.abs(c-k)) 
        mn = min(a2,b2,c2)
        if a2  == mn:
            Image[i][j] = 20
        elif b2 == mn:
            Image[i][j] = 100
        else:
            Image[i][j] = 255
         
plt.imshow(Image, extent=[-1,1,-1,1])
plt.show()