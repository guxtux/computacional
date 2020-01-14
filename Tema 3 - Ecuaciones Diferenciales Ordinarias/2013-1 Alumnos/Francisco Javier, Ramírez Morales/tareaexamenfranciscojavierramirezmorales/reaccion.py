from math import*
import numpy as np
# con este codigo podemos encontrar  el valor de las raices reales de la funcion
#especificada solamente dando para cada raiz un valor aproximado
#el cual se obtiene por inspeccion del correspondiente grafico
def f(x):return x*(3-2*x)**2-249.2*(1-x)**3 # funcion de la que se obtendran las raices
def df(x):return 759.6*x**2-1519.2*x+756.6

z1=np.arange(0.0,1.0,0.1)# valores aproximados de cada raiz obtenidos por inspeccion [0,10]

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol:return x,i
    print 'son demasiadas iteraciones\n'

for i in range(5):# obtencion de las 4 raices correspondientes para cada intervalo
      raiz1 , numIter1 = newtonRaphson(z1[i])
      

      print 'Raiz=', raiz1
      print 'Numero de iteraciones =',numIter1
      


