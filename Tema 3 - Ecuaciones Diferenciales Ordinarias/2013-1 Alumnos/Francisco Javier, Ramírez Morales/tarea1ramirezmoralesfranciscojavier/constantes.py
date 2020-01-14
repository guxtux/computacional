# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 00:46:51 2012

@author: vaio
"""
#este programa calcula el valor de pi
#se usa el algoritmo (pi^2)/6= 1/1*1 + 1/2*2 +...+ 1/n*n +...
#el valor de pi es pi=3.1415926535897932384626433832795...

from math import sqrt,pi
b=[]
uno=1
j=1.0
while uno>0:
    b.append(1/(j*j))
    j=j+1
    if j==10000000:
        break
# el valor de iteraciones se fija para no saturar la memoria
h=sum(b)
p=sqrt(h*6)
print 'el valor de pi es pi=%1.18f'%p

#el error relativo verdadero de esta aproximacion es:
Er=((abs(pi-p))/pi)*100
print ' el error relativo verdadero es: Er=%e' %Er




#algoritmo para la constante de Euler (e)
#el valor de e es e = 2.71828182845904523536022874713527
#primero definimos una funcion que usaremos

def factorial(n):
    
    
     
     
     f = 1
     while (n > 0):
        f = f * n
        n = n - 1
        
     return f


b=[]
 
m=1.0
while m >0:
         b.insert(m,1/factorial(m))
         m=m+1
         if (1/factorial(m)) ==0: 
             break
# El cálculo se detiene cuando el valor acumulado de e, no se logra
# diferenciar (por la precisión del computador), del valor calculado
# en la iteración anterior.
e=sum(b)+1
c=range(len(b))   
print' el valor de la constante e=%1.22f'%e
print ' el numero de iteraciones fue:', len(c)
#este programa calcula e utilizndo el algoritmo
# e= 1 +1/1! + 1/2! +... + 1/n

# el error relativo es 
ex=2.71828182845904523536022874713527
Er=abs(((ex- e))/ex)*100
print ' el error relativo verdadero del calculo fue', Er 






# el valor exacto de gamma es: 0.577215664901532
from math import log
gamma=0

for i in range (1,100000):
  
    gamma = gamma + (1.0/i)-log(1.0 + 1.0/i)
h=0.577215664901532
Er=(abs(h-gamma)/h)*100
print "\n Para un numero i=", i+1, "El valor calculado de gamma es:", gamma
print ' el error relativo verdadero de nuestra aproximacion es Er=%1.3f'%Er
 
    
