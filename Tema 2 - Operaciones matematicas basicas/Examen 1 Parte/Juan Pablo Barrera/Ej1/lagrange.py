## module lagrange
def intlagrange(n,x0,x,f):
    evaluacion=[]
    k=x0
    yres=0
    for i in range(0,n+1):
        z=1.0
        for j in range (0,n+1):
            if i != j:
                z=z * (k-x[j]) / (x[i]-x[j])
        yres=yres+z*f[i]
    evaluacion.append(yres)
        
    return evaluacion
