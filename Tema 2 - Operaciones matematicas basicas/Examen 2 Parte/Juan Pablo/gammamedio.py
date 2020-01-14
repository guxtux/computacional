from integral import *
from numpy import *
from grafica import *

#hago el cambio de variable de t=p**2 , dt=2*dp
#entonces la integral queda como 2*exp(-(p**2))
#los limites de la integral se conservan

#nota: para mostrar la grafica quitar el comentario de graffun y muestra
def f(p):
    fp=2*exp(-(p**2))
    return fp

#graffun(f,0,10)
#muestra()


#como sabemos que esta funcion es positiva para todo t>0
#y tiende a cero cuando t--inf. buscamos un valor cercano al cero para evaluar la integral sobre ese intervalo
#en este caso la integral se hara hasta que el valor de la f(p)<=0.1
x=1
while f(x)>.1:
    while f(x)>1:
        while f(x)>10:
            x=x+10
        x=x+1
    x=x+.1

valorreal=sqrt(pi)
a=0
b=x


n=10
res=trapecios(f,a,b,n)
error=abs(res-valorreal)
tol=.05
#se integra hasta cumplir con la tol(erancia) indicada
while error>tol:
    n=n*2
    res=trapecios(f,a,b,n)
    error=abs(res-valorreal)

print("Se hace el cambio de variable t=(p**2)")
print("se usan %2.0f puntos para la discretizacio"%(float(n)))
print("Se integra por el metodo del trapecio")
print("gamma(1/2)=%0.6f con un error(absoluto)=%0.6f respecto al valor conocido"%(res,error))


