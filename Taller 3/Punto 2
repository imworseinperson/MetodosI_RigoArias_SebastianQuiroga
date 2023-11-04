import numpy as np

def gauss(A, b):
     
     M = np.hstack((A, b))
     n, m = M.shape
     x = np.zeros(n)
     print(M)
     # Recorrer cada fila de la matriz
     for i in range(n):
     # Buscar el pivote más grande en la columna i
          max_row = i
          max_val = abs(M[i, i])
          print(M)
          for j in range(i + 1, n):
               if abs(M[j, i]) > max_val:
                    max_row = j
                    max_val = abs(M[j, i])
          # Intercambiar la fila i con la fila del pivote
          M[[i, max_row]] = M[[max_row, i]]
          
          # Hacer ceros debajo del pivote usando operaciones elementales de fila
          
          for j in range(i + 1, n):
               factor = M[j, i] / M[i, i]
               M[j] = M[j] - factor * M[i]
               
               
          # Resolver el sistema usando sustitución hacia atrás
     for i in range(n - 1, -1, -1):
          
          x[i] = M[i, 3] / M[i, i]
          print(x)
          for j in range(i - 1, -1, -1):
               M[j, -1] -= M[j, i] * x[i]
               
     return x


A1 = np.array([[3,1,-1],[1,-2,1],[4,-1,1]])
A2 = np.array([[2],[0],[3]])

B1 = np.array([[1,1,1],[0,-1,10],[4,-8,0]])
B2 = np.array([[0],[0],[6]])

Ans = gauss(A1,A2)

# Mostrar la solución

print("La solución del sistema es:")
print(Ans)
