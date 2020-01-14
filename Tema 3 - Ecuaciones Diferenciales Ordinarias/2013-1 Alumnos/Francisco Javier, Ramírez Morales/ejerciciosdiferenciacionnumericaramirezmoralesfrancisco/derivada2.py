import numpy as np

def NewtonGregory(x1,deltax,f,xt):
    n=len(f)-1
    deltaF=np.zeros([n+1,n+1])
    deltaF[:,0]=f
    for j in range(1,n+1):
        for i in range(n-j+1):
            deltaF[i,j]=deltaF[i+1,j-1]-deltaF[i,j-1]
    deltaF=deltaF[0:n,1:n+1]

    s=(xt-x1)/deltax


    yt=[]
    for t in range(len(xt)):
        sum=f[0]
        for i in range(n):
            sum+=combinaciones(s[t],i+1)*deltaF[0,i]
        yt+=[sum]
    return yt
def combinaciones(s,k):
    res=1.0
    if k!= 0:
        for i in range(1,k+1):
            res*=(s-i+1)/i
    return res




# queremos la derivada en x=1.0 
x=np.array([0.84,0.92,1.00,1.08,1.16],float) # x[2]=1.0
f=np.array([0.431711,0.398519,0.367879,0.339596,0.312486],float)#f[2]=f(x)

h=eval(raw_input('dame el valor del incremento'))
xs=eval(raw_input('dame el valor donde se evalua la derivada'))

#Para valores centrales obtenemos g(h)


cdfx=(f[3]-f[1])/(2*h)# para la primer derivada
cd2fx=(f[3]-2*f[2]+f[1])/(h*h)#para la segunda derivada

print ' la primer derivada central en el punto elegido es:',cdfx
print' la segunda derivada central en el punto elegido es:',cd2fx
gh=cd2fx
# ahora obtenemos  g(h/2)

xt=np.array([0.92,0.96,1.00,1.04,1.08]) # estos son los puntos que no conocemos
ft=NewtonGregory(x[0],x[1]-x[0],f,xt)# asi que los interpolamos

h2=h/2
rd2fx=(ft[3]-2*ft[2]+ft[1])/(h2*h2)
gh2=rd2fx
print ' la segunda derivada central con h/2 es',rd2fx
# ahora implementamos extrapolacion de richardson
p=2
G=((2**p)*(gh2)-gh)/((2**p)-1)

print' el valor de interpolacion de richardson es',G


