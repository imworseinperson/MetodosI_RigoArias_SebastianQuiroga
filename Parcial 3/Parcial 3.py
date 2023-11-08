import numpy as np

m = np.array([[0.2, 0.1, 1, 1, 0], 
              [0.1, 4, -1, 1, -1], 
              [1, -1, 60, 0, -2], 
              [1, 1, 0, 8, 4], 
              [0, -1, -2, 4, 700]])

x = np.array([7.4, 4.1, 169, 55, 3508])
b = np.array([1, 2, 3, 4, 5])

def descenso(A, b, v, epsilon = 0.01):
    r0 = np.dot(A,v) - b
    print(r0)
    p0 = -r0
    print(p0)
    k = 0
    while np.linalg.norm(r0) < epsilon:
        a = -(np.dot(r0.T, p0)/np.dot(p0.T, np.dot(A,p0)))
        v = v - np.dot(a, p0)
        r0 = np.dot(A,v) - b
        b = np.dot(r0.T, np.dot(A,p0))/np.dot(p0, np.dot(A,p0))
        p0 = -r0 + np.dot(b,p0)
        print(k)
        k += 1
    return v

descenso(m, b, x)
