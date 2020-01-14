##module newtonpoli

#con el doble gato python interpreta como archivo de modulo
#los llamo con import.... es como numpy

def evalpoli(a,xdatos,x):
    n=len(xdatos)-1 #grado del polinomio
    p=a[n]
    for k in range(1,n+1):
        p=a[n-k]+(x-xdatos[n-k])*p
    return p

def coefs(xdatos,ydatos):
    m=len(xdatos)   #numero de puntos
    a=ydatos #algoritmo que calcula los coeficientes del polinomio
    for k in range (1,m):
        for i in range(k,m): #el doble ciclo hace que me quede los elementos de la diagonal
           a[i]=(a[i]-a[k-1])/(xdatos[i]-xdatos[k-1])
        #a[k:m]=(a[k:m]-a[k-1])/(xdatos[k:m]-xdatos[k-1])   #sustituye ese ciclo for
    return a
