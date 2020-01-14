## module euler
def euler(f,a,b,y0,h):
    n=int(float(b-a)/h)
    t=a
    w=y0
    N=range(1,n+1)
    T=[t]
    y=[w]
    for k in N:
        w=w+h*f(t,w)
        t=a+k*h
        T.append(t)
        y.append(w)
    return T,y    
