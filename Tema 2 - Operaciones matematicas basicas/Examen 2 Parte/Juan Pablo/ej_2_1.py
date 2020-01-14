from integral import *
from numpy import *
from scipy import *
from scipy.integrate import romberg

#cambio de variable de x=exp^-sqrt(t); dx=-(exp(-sqrt(t)))/(*sqrt(t))
def f(x):
    #fx=exp(-x)*log(x)
    t=sqrt(x)
    ex=exp(-t)+t
    fx=exp(-ex)/2
    return fx

n=100
print("la primera integral tiene un valor de",trapecios(f,-10,100,n))

a=-100
b=log(2)
n=1000
#cambio de variable de x=2exp(-t);dx=-2exp(-t)dt
def f2(x):
    fx=(x-log(2))*(1+2*exp(-x))*(2*exp(-x))/(1-8*exp(-3*x))
    return fx

print("la seguna integral tiene un valor de",trapecios(f2,a,b,n))
#resultado=romberg(f,1,1000000,show=False)
#print(resultado)
