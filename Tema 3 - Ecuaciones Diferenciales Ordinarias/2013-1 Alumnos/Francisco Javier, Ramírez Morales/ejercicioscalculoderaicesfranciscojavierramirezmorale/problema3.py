from math import*
import numpy as np
# con este codigo podemos encontrar  el valor de las raices reales de la funcion
#especificada solamente dando para cada raiz un valor aproximado
#el cual se obtiene por inspeccion del correspondiente grafico
def f(x):return sin(x)-0.1*x
def df(x):return cos(x)-0.1

z1=np.arange(0.0,10.1,2.5)# valores aproximados de cada raiz obtenidos por inspeccion [0,10]
z2=np.arange(-10.1,0.0,2.5)#[-10,0]
def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol:return x,i
    print 'son demasiadas iteraciones\n'

for i in range(5):# obtencion de las 4 raices correspondientes para cada intervalo
      raiz1 , numIter1 = newtonRaphson(z1[i])
      raiz2 , numIter2 = newtonRaphson(z2[i])

      print 'Raiz=', raiz1
      print 'Numero de iteraciones =',numIter1
      print 'Raiz=', raiz2
      print 'Numero de iteraciones =',numIter2


