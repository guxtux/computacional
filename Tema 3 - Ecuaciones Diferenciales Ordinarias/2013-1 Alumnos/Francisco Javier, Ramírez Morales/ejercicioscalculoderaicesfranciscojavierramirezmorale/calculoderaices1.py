from math import*
import numpy as np
# con este codigo podemos encontrar  el valor de las raices reales de la funcion
#especificada solamente dando el valor aproximado para cada una de las raices
#el cual se obtiene por inspeccion del correspondiente grafico
def f(x):return x**4+0.9*x**3-2.3*x**2+3.6*x-25.2# polinomio del cual se pretenden encontrar las raices
def df(x):return 4.0*x**3+2.7*x**2-4.6*x+3.6#derivada del polinomio
z=[-4.0,2.0]# valores de x aproximados para cada raiz
def newtonRaphson(x,tol=1e-05):# definicion del metodo de Newton-Raphson y tolerancia
    for i in range(50):#numero maximo de iteraciones
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol:return x,i#verificacion de tolerancia
    print 'son demasiadas iteraciones\n'

for i in range(2):# el numero de operaciones esta relacionado con el numero de raices
    
      raiz , numIter = newtonRaphson(z[i])# aqui se aplica el metodo a cada raiz
      print 'Raiz=', raiz # se muetra la raiz obtenida
      print 'Numero de iteraciones =',numIter#se muestra el numero de pasos para llegra a la raiz

