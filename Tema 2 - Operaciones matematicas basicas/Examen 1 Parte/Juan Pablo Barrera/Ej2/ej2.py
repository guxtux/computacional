#Encontrar la raiz de y(x) a partir de los siguientes datos

#aunque el problema se puede resolver en picas lineas seleccionando los puntos "a mano"
#hice un metodo mas general para la seleccion de los puntos

from numpy import *
from lagrange import *



def buscaraiz(y):
    j=1
    while j<len(y):
       i=j-1
       if y[i]*y[j]<0:
           return i,j
       else:
            j=j+1
    return None
    
def puntoscercanos(n,y,puntos,i,j,p,q):
    while len(puntos)<=n+1: #hace el ciclo hasta tener la cantidad de puntos deseados
        if (p>=0) and (q<len(y)):
            a=y[i]-y[p-1]
            b=y[j]-y[q+1]
            if abs(a)<abs(b):
                #el punto i-1 esta mas cerca
                puntos.insert(0,y[p-1])
                p=p-1
            else:
                #el punto j+1 esta mas cerca
                puntos.append(y[q+1])
                q=q+1
        return puntos,p,q
            
#definiciones para el metodo de lagrange
x=linspace(0,3,7)
y=[1.8241,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727]
x0=0
n=[2,3]

#busa el intervalo donde esta la raiz
#i y j ya no cambian... indican los indices de principio y fin del intervalo donde esta la raiz
i,j=buscaraiz(y)
intervalo=[y[i],y[j]]

#encuentra los puntos mas cercanos y evalua el metodo
p=i;q=j   #estas variables llevan la cuenta de los puntos que se van integrando al arreglo a evaluar
#p siempre tiene el menor indice del arreglo y donde empieza el arreglo puntos

for t in n: #t toma los valores de n para la cantidad de puntos que se van a evaluar
    #encuentra puntos cercanos
    puntos,p,q=puntoscercanos(t,y,intervalo,i,j,p,q)
    print("los puntos y en los que se evaluara el metodo son",puntos)

    #evalua el metodo
    xpuntos=linspace(x[p],x[q],len(puntos))
    raiz=intlagrange(t,x0,puntos,xpuntos) #cambio dominio por rango para encontrar un punto en x
    print("la raiz esta en x=%3.4f"%raiz)
    print(" este resultado se encontro usando ",len(puntos)," puntos")
    print("\n")

import matplotlib.pyplot as plt
plt.plot(x,y,raiz,0,"s")
plt.grid()
plt.show()
    
