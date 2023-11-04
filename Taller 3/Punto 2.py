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

def eliminacion_gaussiana(A,B):
     
     # PROCEDIMIENTO
     casicero = 1e-15 # Considerar como 0

     # Evitar truncamiento en operaciones
     A = np.array(A,dtype=float) 

     # Matriz aumentada
     AB  = np.concatenate((A,B),axis=1)
     AB0 = np.copy(AB)

     # Pivoteo parcial por filas
     tamano = np.shape(AB)
     n = tamano[0]
     m = tamano[1]

     # Para cada fila en AB
     for i in range(0,n-1,1):
          # columna desde diagonal i en adelante
          columna  = abs(AB[i:,i])
          dondemax = np.argmax(columna)
          
          # dondemax no está en diagonal
          if (dondemax !=0):
               # intercambia filas
               temporal = np.copy(AB[i,:])
               AB[i,:] = AB[dondemax+i,:]
               AB[dondemax+i,:] = temporal
     AB1 = np.copy(AB)

     # eliminación hacia adelante
     for i in range(0,n-1,1):
          pivote   = AB[i,i]
          adelante = i + 1
          for k in range(adelante,n,1):
               factor  = AB[k,i]/pivote
               AB[k,:] = AB[k,:] - AB[i,:]*factor
               
     # sustitución hacia atrás
     ultfila = n-1
     ultcolumna = m-1
     X = np.zeros(n,dtype=float)
     
     for i in range(ultfila,0-1,-1):
          suma = 0
          for j in range(i+1,ultcolumna,1):
               suma = suma + AB[i,j]*X[j]
          b = AB[i,ultcolumna]
          X[i] = (b-suma)/AB[i,i]
          
     X = np.transpose([X])
     # SALIDA
     print('Matriz aumentada:')
     print(AB0)
     print('Pivoteo parcial por filas')
     print(AB1)
     print('eliminación hacia adelante')
     print(AB)
     print('solución: ')
     print(X)




A = np.array([[3,1,-1],
               [1,-2,1],
               [4,-1,1]])

B = np.array([[2],
               [0],
               [3]])

B1 = np.array([[1, 1, 1],
               [0,-1,10],
               [4,-8, 0]])

B2 = np.array([[0],
               [0],
               [6]])

#Ans = gauss(A1,A2)

# Mostrar la solución



x = eliminacion_gaussiana(A, B)
print("Solución x:", x)