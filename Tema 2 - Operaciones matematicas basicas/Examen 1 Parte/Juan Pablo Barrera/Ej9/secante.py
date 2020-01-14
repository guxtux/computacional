## module secante

def buscaraiz (f,a,b,dx):
    x1=a
    f1=f(a)
    x2=a+dx
    f2=f(x2)
    while f1*f2>0.0:
        if x1>=b:
            return 0,0
        x1=x2
        f1=f2
        x2=x1+dx
        f2=f(x2)
    else:
        return x1,x2
    
def secante(f,x0,x1,tol):
    y0=f(x0)
    y1=f(x1)
    x=x1-y1*((x1-x0)/(y1-y0))
    while f(x)>tol:
        x0=x1;  y0=y1
        x1=x;   y1=f(x1)
        x=x1-y1*((x1-x0)/(y1-y0))
    return x
        
