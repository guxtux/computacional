#calculo de una raiz por el metodo de biseccion
"""
@author: Calderon Apolinar Marco A.
"""

def biseccion(f,a,b):
    x1=a; f1=f(a)
    x2=b; f2=f(b)
    while f1*f2<0.0:
        if x1>=b: return None
        
        x3=(x1+x2)/2.
        f2=f(x3)
        x2=x2-1e-4
    else:
        return x1,x2,x3
        
def f(x): return x**3-10*x**2+5
a,b=(0.0,1.5)
print 'el punto es: '
x1,x2,x3=biseccion(f,a,b)
print x3