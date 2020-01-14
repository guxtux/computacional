# module ruku2


def rk2(f,x,tmax,h):
    y=[]
    t=[]
    y.append(x)
    t.append(0)
    i=0
    for i in range(1000):
        F1=f(y[i],t[i])
        F2=f(y[i]+F1,t[i]+h)
        r=[]
        r.append(y[i][0]+.5*(F1[0]+F2[0]))
        r.append(y[i][1]+.5*(F1[1]+F2[1]))
        y.append(r)
        t.append(t[i]+h)
        #i=i+1
    return y,t

def rk4(f,h,ii,qq):
    k1,I1=f(ii,qq,i*h,h)
    k2,I2=f(ii+k1/2,qq+I1/2,i*h,h)    
    k3,I3=f(ii+k2/2,qq+I2/2,i*h,h)
    k4,I4=f(ii+k3,qq+I3,i*h,h)
    qq=qq+(1.0/6.0)*(I1+2*I2+2*I3+I4)
    ii=ii+(1.0/6.0)*(k1+2*k2+2*k3+k4)
    return ii,qq

