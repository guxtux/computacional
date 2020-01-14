## module RK3SIST3
def RK3SIST3(f,g,I,a,b,x0,y0,z0,h):
    n=int(float(b-a)/h)
    t=a
    w=x0
    w1=y0
    w11=z0
    N=range(1,n+1)
    T=[t]
    x=[w]
    y=[w1]
    z=[w11]
    for k in N:
        K11=h*f(t,w,w1,w11)
        K12=h*g(t,w,w1,w11)
        K13=h*I(t,w,w1,w11)
        K21=h*f(t+(h/2),w+(K11/2),w1+(K12/2),w11+(K13/2))
        K22=h*g(t+(h/2),w+(K11/2),w1+(K12/2),w11+(K13/2))
        K23=h*I(t+(h/2),w+(K11/2),w1+(K12/2),w11+(K13/2))
        K31=h*f(t+h,w-K11+2*K21,w1-K12+2*K22,w11-K13+2*K23)
        K32=h*g(t+h,w-K11+2*K21,w1-K12+2*K22,w11-K13+2*K23)
        K33=h*I(t+h,w-K11+2*K21,w1-K12+2*K22,w11-K13+2*K23)
        w=w+(K11+4*K21+K31)/6
        w1=w1+(K12+4*K22+K32)/6
        w11=w11+(K13+4*K23+K33)/6 
        t=a+k*h
        T.append(t)
        x.append(w)
        y.append(w1)
        z.append(w11)
    return T,x,y,z 
