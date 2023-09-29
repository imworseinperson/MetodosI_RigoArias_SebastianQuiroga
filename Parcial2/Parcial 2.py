import numpy as np
import sympy as sp

x = sp.Symbol('x', real=True)
n = 20
expression = ((sp.E**x)*(x**3))/((sp.E**x)-1)
h = 6.626*(10**-34)
k = 1.3806*(10**-23)
c = 3*(10**8)
T = 5772
expression2 = ((sp.pi*8)/(c**3))*((h*(x**3))/(sp.E**((h*x)/(k*T))-1))
liminf = (h*expression2.evalf(subs={x:1*(10**-7)}))/(k*T)
limsup = (h*expression2.evalf(subs={x:4*(10**-7)}))/(k*T)
print(limsup, liminf)


def GetLaguerre(n,x):
    
    if n==0:
        poly = sp.Number(1)
    elif n==1:
        poly = 1 - x
    else:
        poly = (((2*(n-1)+1-x)*GetLaguerre(n-1,x))-((n-1)*(GetLaguerre(n-2,x))))/n
   
    return sp.expand(poly,x)

def GetLegendre(n,x):
    
    y = (x**2 - 1)**n
    
    poly = sp.diff( y,x,n )/(2**n*np.math.factorial(n))
    
    return poly

def GetDLaguerre(n,x):
    Pn = GetLaguerre(n,x)
    return sp.diff(Pn,x)

def GetNewton(f,df,xn,itmax=10000,precision=1e-14):
    
    error = 1.
    it = 0
    
    while error >= precision and it < itmax:
        
        try:
            
            xn1 = xn - f(xn)/df(xn)
            
            error = np.abs(f(xn)/df(xn))
            
        except ZeroDivisionError:
            print('Zero Division')
            
        xn = xn1
        it += 1
        
    if it == itmax:
        return False
    else:
        return xn
    
def GetRoots(f,df,x,tolerancia = 10):
    
    Roots = np.array([])
    
    for i in x:
        
        root = GetNewton(f,df,i)

        if  type(root)!=bool:
            croot = np.round( root, tolerancia )
            
            if croot not in Roots:
                Roots = np.append(Roots, croot)
                
    Roots.sort()
    
    return Roots


def GetAllRootsGLag(n):

    xn = np.linspace(0,(n+((n-1)*np.sqrt(n))),100)
    
    Laguerre = []
    DLaguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerre(i,x))
        DLaguerre.append(GetDLaguerre(i,x))
    
    poly = sp.lambdify([x],Laguerre[n],'numpy')
    Dpoly = sp.lambdify([x],DLaguerre[n],'numpy')
    Roots = GetRoots(poly,Dpoly,xn)

    if len(Roots) != n:
        ValueError('El número de raíces debe ser igual al n del polinomio.')
    
    return Roots

def GetWeightsGLag(n):

    Roots = GetAllRootsGLag(n)

    Laguerre = []
    
    for i in range(n+1):
        Laguerre.append(GetLaguerre(i,x))
    
    poly = sp.lambdify([x],Laguerre[n],'numpy')
    Weights = (Roots)/(((n+1)**2)*(poly(Roots)**2))
    
    return Weights

GetWeightsGLag(20)