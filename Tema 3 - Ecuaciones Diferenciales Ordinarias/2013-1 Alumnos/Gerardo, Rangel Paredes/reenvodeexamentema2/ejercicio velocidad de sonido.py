from math import*
def f(x): return 2510*log((2800000)/(2800000 - 13300*x)) - 9.81*x -335
def df(x): return (186.39*x + 8450.)/ (4000. - 19.*x)

def newtonRaphson(x, tol=1e-5):
    for i in range(50):
        dx = -f(x)/df(x)
        x = x + dx
        if abs(dx) < tol : return x, i
        print "son demasiadas iteraciones\n"

raiz, numlter = newtonRaphson(3)

print "Raiz =", raiz
print "Numero de iteraciones = ", numlter
