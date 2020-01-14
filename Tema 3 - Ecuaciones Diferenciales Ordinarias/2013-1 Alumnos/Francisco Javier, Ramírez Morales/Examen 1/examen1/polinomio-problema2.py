#RAMIREZ MORALES FRANCISCO JAVIER
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 18:28:54 2012

@author: vaio
"""
miarchivo=open('polinomio_2.dat','w')
import matplotlib.pyplot as plt
import numpy as np
A=[48,100,70,-20,2]
b=A[4]
z=[]
         #   p=48+x(100+x(70+x(-20+x*2)))
n=4
x=np.arange(-4,-.5,0.5)
#inicia el metodo de horner
while n >0:
       n=n-1
       b=A[n]+b*x
       
z.append(b)      

print 'el valor del polinomio evaluado en cada punto del intervalo es',z

miarchivo.write('z')
miarchivo.close()

plt.plot(x,[2560,1713.125,1080,626.125,320,133.125,40], 'r*')
x2=np.linspace(-4,1)
plt.plot(x2,48+x2*(100+x2*(70+x2*(-20+x2*2))),'b-')
plt.xlabel('x')
plt.ylabel('p(x)')
plt.title(' evaluacion de p=48+x(100+x(70+x(-20+x*2))) en algunos puntos')
plt.grid()
plt.show()

# este programa evalua el polinomio  p=48+x(100+x(70+x(-20+x*2)))  utilizando
# el metodo de horner dado el resultado grafico obtenido vemos que este es un metodo
#muy bueno para la evaluacion de polinomios con coeficientes no nulos
#pues reduce el tamaño del codigo y la eficiencia del mismo al hacer menos
#operaciones y nos da los resultados esperados...
#el valor del polinomio evaluado en cada punto del intervalo es [array([ 2560.   ,  1713.125,  1080.   ,   626.125,   320.   ,   133.125,     40.   ])]
