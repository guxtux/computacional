## module RK2
def RK2(f,a,b,y0,h):
    n=int(float(b-a)/h)
    t=a
    w=y0
    N=range(0,n)
    T=[t]
    y=[w]
    for k in N:
        w=w+(h)*(f(t+(h/2),w+(h/2)*f(t,w)))
        t=a+(k+1)*h
        T.append(t)
        y.append(w)
    return T,y 
    
