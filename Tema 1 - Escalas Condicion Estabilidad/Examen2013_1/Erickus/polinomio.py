# -*- coding: utf-8 -*-

p=[48,100,70,-20,2]

x= float(raw_input('cual es el valor de x: '))

def grado(p):
    return len(p)-1
    
def evaluar (p,x):
    suma=0
    for i in range(0,len(p)):

        suma=suma+p[i]*(x**i)
   
# no puedo lograr que me enliste los valors para cada x dada
   
   return suma
print evaluar(p,x)

#no he podido graficarlo