## module RK2SYST3
def RK2SYST3(f,g,I,a,b,x0,y0,z0,h):
    n=int(float(b-a)/h)
    t=a
    w1=y0
    w=x0
    w11=z0
    N=range(0,n)
    T=[t]
    x=[w]
    y=[w1]
    z=[w11]
    for k in N:
        K11=h*f(t,w,w1,w11)
        K12=h*g(t,w,w1,w11)
        K13=h*I(t,w,w1,w11)
        K21=h*f(a+(k+1)*h,w+K11,w1+K12,w11+K13)
        K22=h*g(a+(k+1)*h,w+K11,w1+K12,w11+K13)
        K23=h*I(a+(k+1)*h,w+K11,w1+K12,w11+K13)
        w=w+(K11+K21)/2
        w1=w1+(K12+K22)/2
        w11=w11+(K13+K23)/2
        t=a+(k+1)*h
        T.append(t)
        x.append(w)
        y.append(w1)
        z.append(w11)
    return T,x,y,z 
