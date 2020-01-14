## module newtonraphson

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

def newtonraphson(f,df,a,b,tol):

    fa=f(a)
    if fa== 0.0:
        return a

    fb=f(b)
    if f(b)==0.0:
        return b

    if fa*fb>0.0: print(" la raiz no es en el intervalo")
    x=0.5*(a+b)


    for i in range(30):
        fx=f(x)
        if abs(fx)<tol:
            return x
        if fa*fx<0.0:
            b=x
        else:
            a=x
            fa=fx

        dfx=df(x)
        try:dx=-fx/dfx
        except ZeroDivisionError: dx=b-a
        x=x+dx

        if(b-x)*(x-a)<0.0:
            dx=0.5*(b-a)
            x=a+dx

        if abs(dx)<tol*max(abs(b),1.0):
            return x

    print("demasiadas iteraciones")
    

