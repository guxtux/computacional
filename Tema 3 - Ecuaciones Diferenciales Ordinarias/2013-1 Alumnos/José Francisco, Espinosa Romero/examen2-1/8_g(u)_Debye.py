# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 17:44:11 2012

@author: pako
"""
import numpy as np
from scipy import *
import matplotlib.pyplot as plt

def f(x): return (x**4)/(1-exp(-x))

def iS(f,a,b,h):
    I=(f[a]+4*f[(a+b)/2]+f[b])*h/3.
    return I
    
def g(u,I):
    G=(u**3)*I
    return G

u=np.arange(0.0,1.025,0.025)
ub=[]
for j in range (41):
    ub.append(1./u[j])
F=[]
G=[]
i,n=0,0
while i<len(u):
    F.append(f(ub[i]))
    #print ub[i],F[i]
    i=i+1

for l in range (0,41,2):
    I,j=0.,2
    """if l==0:
        I=inf
        print "I(",ub[l],")=",I
        #print u[l],ub[l],I
        G.append(g(u[l],I))
        print "g(",u[l],")=",G[n],"\n"
    elif l==2:
        I=inf
        print "I(",ub[l],")=",I
        #print u[l],ub[l],I
        G.append(g(u[l],I))
        print "g(",u[l],")=",G[n],"\n"
    else:"""
    while j+2<=l:
        I=I+iS(F,j,j+2,0.025)
        #print F[j],F[j+1],F[j-1]
        j=j+2
    print "I(",ub[l],")=",I
    #print u[l],ub[l],I
    G.append(g(u[l],I))
    print "g(",u[l],")=",G[n],"\n"
    n=n+1

u=np.arange(0.0,1.05,0.05)
plt.plot(u,G)
plt.xlabel("Valores de u")
plt.ylabel("Valores de g(u)")
plt.title("u:= Temperatura absoluta / Temperatura de Debye")
plt.show()

"""
no pude encontrar un cambio de variable adecuado 
para que el llímite superior de la integral no se fuera a infinito
y por ello no pude utilizar la integral de romberg de la libreria scipy
asi que tuve que tomar los intervalos y utilizar eel método
de la integral de Simpson de 1/3
e ignorar 2 puntos para los cuales el punto f(1/u) se indeterminaba
sin embargo para que la gráfica concuerde con el experimento, 
y el cv se vaya a cero cuando T absoluta se va a cero,
g(u) debe valor cero en u=0,
y fijando esos puntos antes de integrar se puede obtener   
una grafica que asemeja el comportamiento de g(u)
"""