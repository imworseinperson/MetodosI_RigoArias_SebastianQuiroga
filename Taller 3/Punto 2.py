import numpy as np

def eliminacion_gaussiana(A,B): 
     
     M  = np.concatenate((A,B),axis=1)
     tamano = np.shape(AB)
     n = tamano[0]
     m = tamano[1]
     
     for i in range(0,n-1,1):
          
          columna  = abs(M[i:,i])
          max = np.argmax(columna)
          
          if (max !=0):
               
               temporal = np.copy(M[i,:])
               M[i,:] = M[max+i,:]
               M[max+i,:] = temporal
               
     for i in range(0,n-1,1):
          
          pivote   = M[i,i]
          adelante = i + 1
          for k in range(adelante,n,1):
               factor  = M[k,i]/pivote
               M[k,:] = M[k,:] - M[i,:]*factor
               
     ultfila = n-1
     ultcolumna = m-1
     x = np.zeros(n,dtype=float)
     
     for i in range(ultfila,-1,-1):
          suma = 0
          for j in range(i+1,ultcolumna,1):
               suma = suma + M[i,j]*x[j]
          b = M[i,ultcolumna]
          x[i] = (b-suma)/M[i,i]
          
     x = np.transpose([x])
     
     print('solución: ',x)




A1 = np.array([[3,1,-1],
               [1,-2,1],
               [4,-1,1]])

A2 = np.array([[2],
               [0],
               [3]])

B1 = np.array([[1, 1, 1],
               [0,-1,10],
               [4,-8, 0]])

B2 = np.array([[0],
               [0],
               [6]])

x = eliminacion_gaussiana(A, B)
print("Solución x:", x)