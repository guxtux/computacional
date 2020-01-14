##module newtonRaphson
def newtonRaphson(f,df,x,tol=0.0001):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
    print 'Son demasiadas iteraciones/n'
