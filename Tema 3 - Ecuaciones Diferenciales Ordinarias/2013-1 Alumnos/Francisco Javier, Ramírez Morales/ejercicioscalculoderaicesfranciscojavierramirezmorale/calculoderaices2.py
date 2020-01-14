from math import*
import numpy as np
# con este codigo podemos encontrar  el valor de las raices reales de la funcion
#especificada solamente dando para cada raiz un valor aproximado
#el cual se obtiene por inspeccion del correspondiente grafico
def f(x):return x**4 +2*x**3 -7*x**2 +3
def df(x):return 4.0*x**3 + 6*x**2-14*x

z=[-4,-0.5,0.8,1.6]# valores aproximados de cada raiz obtenidos por inspeccion

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol:return x,i
    print 'son demasiadas iteraciones\n'

for i in range(4):# obtencion de las 4 raices correspondientes
      raiz , numIter = newtonRaphson(z[i])

      print 'Raiz=', raiz
      print 'Numero de iteraciones =',numIter


