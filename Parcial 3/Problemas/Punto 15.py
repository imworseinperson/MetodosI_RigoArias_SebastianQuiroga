import sympy as sp

#Función

def oper(A,B):
    return (A*B) - (B*A)

#Matrices

m1 = sp.matrices.Matrix([[0.,1.],[1.,0.]])
m2 = sp.matrices.Matrix([[0.,-1j],[1j,0.]])
m3 = sp.matrices.Matrix([[1.,0.],[0.,-1.]])

print(oper(m1,m2), "=", 2j*m3)
print(oper(m1,m3), "=", 2j*m2)
print(oper(m2,m1), "=", 2j*m3)
print(oper(m2,m3), "=", 2j*m1)
print(oper(m3,m1), "=", 2j*m2)
print(oper(m3,m2), "=", 2j*m1)