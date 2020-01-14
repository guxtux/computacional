# raices x4+.9x3-2.3x2+3.6x-25.2
"""
@author: Calderon Apolinar Marco A.
"""

def f(x): return x**4+0.9*x**3-2.3*x**2+3.6*x-25.2

def df(x): return 4*x**3+2.7*x**2-4.6*x+3.6

def newtonRaphson(x,tol=1e-05):
    for i in range(50):
        dx=-f(x)/df(x)
        x=x+dx
        if abs(dx)<tol: return x,i
        
    print 'son demasiadas iteraciones\n'
    
y=[-5,5]
for c in y:
    
  raiz, numiter=newtonRaphson(c)
  print 'Raiz=', raiz
  print 'numero de iteraciones=', numiter