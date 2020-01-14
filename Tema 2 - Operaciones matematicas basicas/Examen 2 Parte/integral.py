## module integral
from diferenciasfinitas2 import*

def trapecios(f,a,b,n):
    h=(b-a)/float(n)
    x=a
    sum=0
    for i in range (1,n):
        x=x+h
        sum=sum+f(x)
        
    return (h/2.)*(f(a)+f(b)+2*sum)

def errores(f,a,b,n,area):
    h=(b-a)/float(n)
    x=[a]
    m=a
    while m<=b:
        m=m+h
        x.append(m)
    deriv=deriv2orden2(area,f,h)
    error=(h**3)*deriv/12
    return error

def simpson(f,a,b,n):
    n=n-n%2
    if n<=0:
        n=1
    h=(b-a)/n
    x=a
    suma=0
    for j in range(n/2):
        suma += f(x)+4*f(x+h)+f(x+2*h)
        x +=2*h
    return (h/3.)*suma

