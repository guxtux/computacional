from numpy import *
from grafica import *

#Nota. copie las funciones que uso en cada modulo para este programa dentro de
#este codigo por simplicidad, pues modifique algunas de ellas y los demas programas no
#corren con el modulo modificado.

#dividi la funcion F en dos partes, una constante que es la que lleva el numero n
#y la otra en la parte de la integral que se evalua

#para evaluar las energias de h y o2 se hace la distincion a traves de la constante gamma (definida en F)
#al modificar el valor se escoge el elemento gamma(h)=21.7 gamma(o2)=150

#llas funciones se van llamando en orden, empezando con la de mas abajo (secante). Desde esa funcion se llama la que esta
#inmediatamente arriba y asi se siguen.

#para evaluar otros potenciales como el de yakawa se tiene que escribir la funcion potencial correspondiente en la funcion potencial de codigo
#tambien se tienen que modificar los limites de integracion correspondientes (romin y romax)
#en el potencial de yakawa, conservando las sustituciones de energia y radio en terminos de epsilon y ro
#tenemos que suponer que k=Vo*a para poder adimensionalizar bien la funcion que se integra.

def potencial(ro):  #se captura la funcion de potencial
    #potencial leonard jones
    v= 4*((1/ro)**12-(1/ro)**6)
    return v

def integrando(ro,delta):  #"crea" la funcion que se integra
    disc= delta-1-potencial(ro)
    if disc>0:
        fx=sqrt(disc)
    else:
        fx=0
    return fx

def trapecios(f,a,b,n,delta): #se hace la integracion por metodo del trapecio
    #aqui la f representa la funcion integrando
    h=(b-a)/float(n)
    x=a
    sum=0
    err=0
    for i in range (1,n):
        x=x+h
        sum=sum+f(x,delta)
    return (h/2.0)*(f(a,delta)+f(b,delta)+2*sum)

def F(eps,cte): #junta la funcion que se integra con la constante
    fn=0
    gamma=150 #aqui se pone gamma=21.7 para obtener el resultado con el hidrogeno
    delta=eps+1
    if (delta<1) and(delta>0):
        romin=((2.-2.*sqrt(delta))/(1.-delta))**(1./6)
        romax=((2.+2.*sqrt(delta))/(1.-delta))**(1./6)
        fn=gamma*trapecios(integrando,romin,romax,50,delta)-cte
    return fn

def secante(f,x0,x1,tol,cte): #encuentra los ceros, mantiene n constante y modifica el valor de epsilon
    y0=f(x0,cte)
    y1=f(x1,cte)
    x=x1-y1*((x1-x0)/(y1-y0))
    i=0
    while abs(f(x,cte))>tol:
        x0=x1;  y0=y1
        x1=x;   y1=f(x1,cte)
        x=x1-y1*((x1-x0)/(y1-y0))
        i=i+1
    return x,i
        

#comienza el programa.... 
print(" n      epsilon n    iteraciones        tolerancia")
n=0
tolerancia=.0000001 #para el metodo de la secante

#a y b son el intervalo por el que corre epsilon
a=-1+tolerancia
b=0-tolerancia


cte=pi*(n+.5)#termino que tiene los niveles
raiz,iteraciones=secante(F,a,b,tolerancia,cte)
while raiz<0:
    print("%2.0f     %2.7f        %2.0f            %0.10f"%(float(n),raiz,iteraciones,tolerancia) )
    grafpto(n,raiz)
    n=n+1
    cte=pi*(n+.5)#termino que tiene los niveles
    raiz,iteraciones=secante(F,a,b,tolerancia,cte)
muestra()

#el intervalo en el que esta la raiz es de epsilon 
#en el metodo secante se busca la raiz evaluando diferentes epsilon en la integral
#para encontrar el valor que la F se hace cero    

