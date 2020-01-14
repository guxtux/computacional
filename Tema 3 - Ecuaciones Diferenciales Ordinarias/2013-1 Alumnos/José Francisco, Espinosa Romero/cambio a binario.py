# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/pako/.spyder2/.temp.py
"""

print "Este programa convierte un real a código binario"
N=eval(raw_input("¿Qué real deseas convertir?"))

#se obtienen las partes entera y decimal del real
e=abs(int(N))
d=abs(N-int(N))

#el condicional determina el signo
if N>=0:
    a=0
else:
    a=1
c=[a]

#el siguiente ciclo tranforma la parte entera
while e!=1 and e!=0:
    m=e%2      
    e=e/2
    c.insert(1,m)
c.insert(1,e)
c.append('.')
#el siguiente ciclo tranforma la parte decimal
while d!=0:
    v=d*2.0
    b=int(v)
    d=v-b
    c.append(b)

print "El número ",N,"en código binario es:",c


#LUDMILA: segun yo, ya transforma el real a binario 
#y lo deja en el orden correcto, con su sgno y el punto
#pero ya no se q más hacer para tener los 64 espacios
#ni como imprimir los elementos de la lista sin comas

