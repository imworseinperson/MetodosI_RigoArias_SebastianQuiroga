import numpy as np

def descenso(A, b, x, epsilon = 0.01):
    r0 = np.dot(A,x) - b
    p0 = -r0
    k = 0
    while np.linalg.norm(r0) >= epsilon and k <= 5:
        a = -(np.dot(r0.T, p0)/np.dot(p0.T, np.dot(A,p0)))
        x = x + np.dot(a, p0)
        r0 = np.dot(A,x) - b
        b = np.dot(r0.T, np.dot(A,p0))/np.dot(p0, np.dot(A,p0))
        p0 = -r0 + np.dot(b,p0)
        print(k)
        k += 1
    return x

m = np.array([[0.2, 0.1, 1, 1, 0], 
              [0.1, 4, -1, 1, -1], 
              [1, -1, 60, 0, -2], 
              [1, 1, 0, 8, 4], 
              [0, -1, -2, 4, 700]])
x = np.array([0, 0, 0, 0, 0])
b = np.array([1, 2, 3, 4, 5])
res = descenso(m, b, x)
print(res)