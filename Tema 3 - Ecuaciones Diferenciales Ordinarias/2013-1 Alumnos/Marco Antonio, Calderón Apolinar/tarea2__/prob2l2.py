# raices de x4+2x3-7x2+3
"""
@author: Calderon Apolinar Marco A
"""
def f(x): return x**4+2*x**3-7*x**2+3.0

def df(x): return 4*x**3+6*x**2-14*x

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
        
    print 'son demasiadas iteraciones\n'
    
y=[-4,-2,1,3]
for c in y:
    
  raiz, numiter=newtonRaphson(c)
  print 'Raiz=', raiz
  print 'numero de iteraciones=', numiter