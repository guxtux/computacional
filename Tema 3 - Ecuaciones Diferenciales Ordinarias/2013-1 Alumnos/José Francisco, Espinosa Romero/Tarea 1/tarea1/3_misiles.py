# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:47:04 2012

@author: pako
"""
t=eval(raw_input("Tiempo en décimas de segundos: "))

def cambiobinario(N):
    
    #se obtienen las partes entera y decimal del real
    e=abs(int(N))
    d=abs(N-int(N))
    c=[]
    l=len(c)
    #el condicional determina el signo
    if N<=0:
        print "El tiempo es negativo"
    else:
        
        #el siguiente ciclo tranforma la parte entera
        while e!=1 and e!=0:
            m=e%2      
            e=e/2
            c.insert(0,m)
        c.insert(0,e)
        c.append('.')
    
        #el siguiente ciclo tranforma la parte decimal
        while d!=0 and l<26:
            v=d*2.0
            b=int(v)
            d=v-b
            c.append(b)
            l=len(c)
    return c
    
def cambioreal(l):
    n=0
    r=0
    while n<24:
        a=l[n]
        n=n+1
        d=1/(2.0**n)
        r=r+a*d
    return r

ptouno=cambiobinario(0.1)[2:]
lpu=len(ptouno)
real=cambioreal(ptouno)
tiempo=t*real
error=t*0.1-tiempo
    
print "El número 0.1 en código binario es:",ptouno
print "El número de bits es:",lpu
print "El valor de 0.1 guardado es:",real
print "El tiempo que calculaba el Patriot era de:",tiempo, "segundos"
print "La diferencia de tiempo es:",error,"segundos"