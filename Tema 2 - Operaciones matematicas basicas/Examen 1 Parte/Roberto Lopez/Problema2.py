from numpy import *
n=2
f=array([0.0,2.0,2.5])
x=array([1.8421,0.8509,-0.4112])
x0=[0.0]
for k in x0:
    yres=0
    for i in range(0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i != j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i] 
    print 'a) Utilizando el metodo de Lagrange en tres puntos:',x[0],',',x[1],',',x[2],'la raiz es:',yres
n=3
f=array([0.0,2.0,2.5,3.0])
x=array([1.8421,0.8509,-0.4112,-1.5727])
x0=[0.0]
for k in x0:
    yres=0
    for i in range(0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i != j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i] 
    print 'a) Utilizando el metodo de Lagrange en cuatro puntos:',x[0],',',x[1],',',x[2],',',x[3],'la raiz es:',yres

