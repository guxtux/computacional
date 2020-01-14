## module RK4SYSTEM
def RK4SYSTEM(f,g,a,b,y0,z0,h):
    n=int(float(b-a)/h)
    t=a
    w=y0
    w1=z0
    N=range(1,n+1)
    T=[t]
    z=[w1]
    y=[w]
    for k in N:
        K11=h*f(t,w,w1)
        K12=h*g(t,w,w1)
        K21=h*f(t+(h/2),w+(K11/2),w1+(K12/2))
        K22=h*g(t+(h/2),w+(K11/2),w1+(K12/2))
        K31=h*f(t+(h/2),w+(K21/2),w1+(K22/2))
        K32=h*g(t+(h/2),w+(K21/2),w1+(K22/2))
        K41=h*f(t+h,w+K31,w1+K32)
        K42=h*g(t+h,w+K31,w1+K32)       
        w=w+(K11+2*K21+2*K31+K41)/6
        w1=w1+(K12+2*K22+2*K32+K42)/6
        t=a+k*h
        T.append(t)
        y.append(w)
        z.append(w1)
    return T,y,z 
