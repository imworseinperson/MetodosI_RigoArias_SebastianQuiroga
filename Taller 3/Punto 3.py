import numpy as np

#Funciones

def normalise(vector1, vector2):
    return vector2/np.sqrt(np.dot(vector1,vector2))

def solucion(matriz, iters, vector1, vector2):
    v0 = normalise(vector1,vector2)
    i=0
    while i < iters:
        vf = normalise(np.dot(matriz,v0),np.dot(matriz,v0).T)
        v0 = vf
        i += 1
    return v0

#Parámetros
#m1=m2=m3=1
#Matriz con los valores k dados

m = np.array([[-2,1,0],
              [1,-2,1],
              [0,1,-2]])
im = np.linalg.inv(m)
random = np.random.rand(3)
randomT = random.T

#Resultados

v1 = solucion(im, 10, random, randomT)
eMen = (1/(np.dot(np.dot(v1, im), v1.T))) * (-1)
v2 = solucion(m, 10, random, randomT)
eMay = (np.dot(np.dot(v2, m), v2.T)) *(-1)

print("Frecuencia mínima y vector propio respectivamente: ", '\n', eMen, '\n', v1)
print("Frecuencia máxima y vector propio respectivamente: ", '\n', eMay, '\n', v2)