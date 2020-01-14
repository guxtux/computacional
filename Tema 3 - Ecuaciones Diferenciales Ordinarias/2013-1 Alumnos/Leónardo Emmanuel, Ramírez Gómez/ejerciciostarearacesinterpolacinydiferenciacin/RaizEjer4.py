# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 01:35:53 2012

@author: emmanuel
"""

#La velocidad v de un cohete Saturno V en vuelo vertical cercano a la superficie
#de la Tierra, puede aproximarse por

#v=u*ln(Mo/(Mo-mt))-g*t   ----(1)

#donde:
u=2510 #m/s velocidad de escape del cohete
Mo=2.8*10**6 #Kg masa del cohete al despegue
m=13.3*10**3 #Kg/s tasa de consumo de combustible
g=9.81 #m/s² aceleracion debida a la gravedad
#t= tiempo medido desde el despegue

#Calcula el tiempo en el cual el cohete alcanza la velocidad del sonido 
v=335 #m/s


#De (1) despejamos para igualar a 0, y sustituimos los datos dados, entonces:

#u*ln(Mo/(Mo-mt))-g*t-v=0
from math import*

def f(t): return u*log(Mo/(Mo-m*t))-g*t-v

def buscaraiz(f,a,b,dx):
    x1=a; f1=f(a)
    x2=a+dx; f2=f(x2)
    while f1*f2>0.0:
        if x1>=b: return None
        x1=x2; f1=f2
        x2=x1+dx; f2=f(x2)
    else:
        return x1,x2

#Dado que t>0 tomamos el intervalo (0,200) ya que para t>200 el polinomio se
#va a infinito
a,b,dx=(0.,200.,0.0001)
while a<b:
    print 'El intervalo es:'
    x1,x2=buscaraiz(f,a,b,dx)
    print '(',x1,',',x2,')'
    xmed=(x1+x2)/2.
    print 'tiempo en el que el cohete alcanza la velocidad del sonido es aprox:'
    print xmed,'s'
    print '---------------------'
    a=x2
    
#como comentario hay que notar que si tomamos el polinomio como tal hay otra
#raiz negativa cerca a 220, que carece de sentido físico