import numpy as np

def gauss(A, b):
     
     M = np.column_stack((A, b))
     print(M)
     n, m = M.shape
     
     # Recorrer cada fila de la matriz
     for i in range(n):
     # Buscar el pivote más grande en la columna i
          max_row = i
          max_val = abs(M[i, i])
          
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
          x[i] = M[i, -1] / M[i, i]
          
          for j in range(i - 1, -1, -1):
               M[j, -1] -= M[j, i] * x[i]
     return x

# Ejemplo de uso de la función gauss
# Definir la matriz A y el vector b del sistema Ax=b
A = np.array([[3,1,-1],[1,-2,1],[4,-1,1]])
b = np.array([[2],[0],[3]])
# Llamar a la función gauss para resolver el sistema
x = gauss(A, b)
# Mostrar la solución
print("La solución del sistema es:")
print(x)
