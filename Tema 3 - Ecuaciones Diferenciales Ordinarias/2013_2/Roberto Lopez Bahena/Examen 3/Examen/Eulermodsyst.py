## module Eulermodsyst
def Eulermodsyst(f,g,a,b,y0,z0,h):
    n=int(float(b-a)/h)
    t=a
    w=y0
    w1=z0
    N=range(0,n)
    T=[t]
    y=[w]
    z=[w1]
    for k in N:
        w=w+(h/2)*(f(t,w,w1)+f(a+(k+1)*h,w+h*f(t,w,w1),w1+h*g(t,w,w1)))
        w1=w1+(h/2)*(g(t,w,w1)+g(a+(k+1)*h,w+h*f(t,w,w1),w1+h*g(t,w,w1)))
        t=a+(k+1)*h
        T.append(t)
        y.append(w)
        z.append(w1)
    return T,y,z 
