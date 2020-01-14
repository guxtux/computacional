## module Eulersystem
def Eulersystem(f,g,a,b,y0,z0,h):
    n=int(float(b-a)/h)
    t=a
    w=y0
    w1=z0
    N=range(1,n+1)
    T=[t]
    y=[w]
    z=[w1]
    for k in N:
        w=w+h*f(t,w,w1)
        w1=w1+h*g(t,w,w1)
        t=a+k*h
        T.append(t)
        y.append(w)
        z.append(w1)
    return T,y,z   
