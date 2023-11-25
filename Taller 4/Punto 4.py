import numpy as np

#Variables

T = np.array([[0.4,0.2,0.2,0.2],
              [0.25,0.25,0.25,0.25],
              [0.3,0.3,0.1,0.7],
              [0.1,0.1,0.1,0.7]])
E = np.array([[0.8,0.,0.,0.2],
              [0.05, 0.9, 0.1, 0.1],
              [0.05, 0.1,0.9,0.],
              [0.1,0.,0.,0.7]])
pi = np.array([0.25,0.,0.5,0.25])

#Probabilidad de obtener el gen g = [T, G,C, T,C, A, A,A]

gen = (pi[3])*(T[3,2])*(T[2,1])*(T[1,3])*(T[3,1])*(T[1,0])*(T[0,0])*(T[0,0])
print(gen)

#Si un gen traducido está dado por gT = [A,C, G, A, G,U,U,U], 
#¿cuál es la probabilidad de que venga del gen g anterior?

anterior = gen*(E[3,3])*(E[2,2])*(E[1,1])*(E[3,3])*(E[1,1])*(E[0,0])*(E[0,0])*(E[0,0])
print(anterior)