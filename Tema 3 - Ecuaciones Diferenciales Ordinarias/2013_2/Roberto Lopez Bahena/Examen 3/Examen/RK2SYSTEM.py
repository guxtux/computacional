## module RK2SYSTEM
def RK2SYSTEM(f,g,a,b,y0,z0,h):
    n=int(float(b-a)/h)
    t=a
    w1=z0
    w=y0
    N=range(0,n)
    T=[t]
    y=[w]
    z=[w1]
    for k in N:
        K11=h*f(t,w,w1)
        K12=h*g(t,w,w1)
        K21=h*f(a+(k+1)*h,w+K11,w1+K12)
        K22=h*g(a+(k+1)*h,w+K11,w1+K12)
        w=w+(K11+K21)/2
        w1=w1+(K12+K22)/2
        t=a+(k+1)*h
        T.append(t)
        y.append(w)
        z.append(w1)
    return T,y,z 
