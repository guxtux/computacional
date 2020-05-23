# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:51:55 2020

@author: gusto
"""


from modulo_gaussjordan import gaussjordan
from scipy.sparse import diags
import numpy as np


def exacta(t):
    valor = ((2*np.sqrt(3))/9)*np.exp(-4*t)*np.sin(4*np.sqrt(3)*t+(np.pi/3))
    return valor

def tamanoh(a, b, N):
    paso = (b - a)/N
    return paso

def coeficientes(h, p, q):
    aij_1 = 1 - (h/2)*p
    aij = q*h**2 - 2
    aij1 = 1 + (h/2)*p
    
    return aij_1, aij, aij1

def ecuacion(N, coeficientes):
    eclinea = []
    for i in range(len(coeficientes)):
        eclinea.append(coeficientes[i])
    return eclinea

a = 0
b = 1
N = 8
p = 8
q = 64
f = 0

#condiciones iniciales
y0 = 0.3333
yf = 0.007

h = tamanoh(a, b, N)
valores = coeficientes(h, p, q)
print('Coeficientes')
print(valores)

puntos = np.arange(a, b+0.001, h)


matrizb = np.zeros(N-1)
matrizb[0] = -y0*valores[0]
matrizb[-1] = -yf*valores[-1]

k = np.array([valores[0]*np.ones(N-1), valores[1]*np.ones(N), valores[2]*np.ones(N-1)])
offset = [-1, 0, 1]
A = diags(k, offset).toarray()
print()
print('Matriz de coeficientes')
print(A)

print('\nMatriz de términos constantes')
print(matrizb)

X, MA = gaussjordan(A, matrizb)


nuevox = []
nuevox.append(matrizb[0])
for i in range(len(X)):
    nuevox.append(X[i])
nuevox.append(matrizb[-1])


nuevox[0] = exacta(0)
nuevox[-1] = exacta(1)

print(nuevox)
#print('\nSolución de la ED para los yi')
#print(X)
#
#print('\nLa matriz a transformada es: ')
#print(MA)

salida = open('Datos_N_'+str(N)+'.txt', 'w')

salida.write('N \t x \t y(x) \t yi\n')


print('\nTabla con los datos\n')
print('N \t x \t\t y(x) \t\t yi')

for i in range(len(puntos)):
    print('{0:} \t {1:1.4f} \t {2:1.4f} \t {3:1.4f}'.format(i, puntos[i], exacta(puntos[i]), nuevox[i]))
    salida.write('{0:} \t {1:1.6f} \t {2:1.6f} \t {3:1.6f}\n'.format(i, puntos[i], exacta(puntos[i]), nuevox[i]))

salida.close()