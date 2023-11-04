import numpy as np

def multiplicar_matrices(A, B):
    
    m = A.shape[0]
    n = A.shape[1]
    p = B.shape[1]
    
    C = np.zeros((m, p))
    
    if n != B.shape[0]:
        return "Las matrices no son multiplicables"
    
    for i in range(m):
        for j in range(p):           
            suma = 0       
            for k in range(n):            
                suma += A[i, k] * B[k, j]     
            C[i, j] = suma
    return C

# a ->
a1 = np.array([[5, -4, -2], [5, -5, 4], [2, 5, -4], [-5, 4, 3], [3, -4, -3]])
a2 = np.array([[5], [-2], [3]])
print(multiplicar_matrices(a1,a2))

# b ->
b1 = np.array([[0, -1, -1, 3], [5, -5, -2, 2], [1, 0, 4, 5]])
b2 = np.array([[0, -3], [-2, -1], [3, -3]])
print(multiplicar_matrices(b1,b2))

# c ->
c1 = np.array([[2, -5, 5, 1], [5, 2, -7, -6], [-6, -1, 7, -4], [5, 4, 1, -5]])
c2 = np.array([[0, 4, -7, 1, -6], [-1, -6, -5, 1, 1], [2, -1, -6, 5, -5], [-3, -6, 6, 3, 5]])
print(multiplicar_matrices(c1,c2))

# d Utilizando dos matrices cuadradas, demuestre que la multiplicación no es
# conmutativa ->

d1 = np.array([[1,2], [3,4]])
d2 = np.array([[5,6], [7,8]])

if (multiplicar_matrices(d1,d2) == multiplicar_matrices(d2,d1)).all():
    print("Las matematicas estan rotas")

else:
    print("La multiplicacion de matrices no es conmutativa")
