from newtonraphson import *
from numpy import *
from grafica import *

def f(x):
    fx=-x**3 +x+1
    return fx

def df(x):
    dfx= -3*x**2+1
    return dfx

a,b=-2,2
graffun(f,a,b)


raiz=[]
dx=.1
x1,x2=buscaraiz(f,a,b,dx)


i=1
while x1!=x2:
    raiz.append(newtonraphson(f,df,x1,x2,.0001))
    x1=raiz[i-1]+dx
    x1,x2=buscaraiz(f,x1,b,dx)
    i=i+1

print("la funcion tiene",len(raiz),"raices")
for i in raiz:
    print("La funcion tiene una raiz en x=%3.5f"%i)
    grafpto(i,0)
muestra()
