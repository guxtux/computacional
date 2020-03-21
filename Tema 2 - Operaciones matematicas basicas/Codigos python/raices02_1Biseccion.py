# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:02:24 2012

@author: IIFCES
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from math import ceil, log, tan
import numpy as np
pi = np.pi

def rootsearch(f,a,b,dx):
    x1 = a; f1 = f(a)
    x2 = a + dx; f2 = f(x2)
    while f1*f2 > 0.0:
        if x1 >= b: return None
        x1 = x2; f1 = f2
        x2 = x1 + dx; f2 = f(x2)
    else:
        return x1,x2

def bisect(f,x1,x2,switch,epsilon=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    
    if f1*f2 > 0.0: print 'La raiz no se ha identificado en un intervalo'

    n = ceil(log(abs(x2 - x1)/epsilon)/log(2.0))

    for i in np.arange(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) \
                        and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0: return x3
        if f2*f3 < 0.0:
            x1 = x3; f1 = f3
        else:
            x2 =x3; f2 = f3
    return (x1 + x2)/2.0

#def f(x):return x - np.tan(x)
#def f(x): return x**3-10*x**2+5
def f(x): return np.tan(x)-x+1
a,b,dx = (0.0, 1.5, 0.2)
#a,b,dx = (-2.0,11.0,0.02)
ejer2=np.linspace(0,3*np.pi)


print 'Intervalo (x1,x2)   raiz'
while 1:
    try:
        x1, x2 = rootsearch(f,a,b,dx)
    except Exception, e:
        print e; break
    if x1 != None:
        a = x2
        root = bisect(f,x1,x2,1)
        if root != None: print '(%2.4f, %2.4f) %2.8f' %(x1, x2, root)
    else:
        print '\nDone'
        break

plt.plot(ejer2,f(ejer2))
plt.grid(True)
#plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(u'Función tan(x)-x+1')
#plt.axis([-1.0,1.5,-10.0,6.0])
l =plt.axhline(y=0.0 ,color='k', linestyle ='-')
s = plt.axvline(x=0, color= 'k', linestyle='-')
plt.plot(4.4283,0, 'ro')
plt.plot(7.7056,0, 'ro')
plt.text(2*pi,30,"x1=4.4283")
plt.text(2*pi,26,"x2=7.7056")
plt.xticks([0, pi/2, pi, 3*pi/2, 2*pi,5*pi/2,3*pi],
           ['$0$', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3\pi}{2}$', r'$2\pi$', r'$\frac{5\pi}{2}$',r'$3 \pi$'], fontsize=15)
plt.annotate(u'x1', xy=(4.4, 1),  xycoords='data',
                xytext=(3,8), arrowprops=dict(facecolor='black',shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
            )
plt.annotate(u'x2', xy=(7.7, 1),  xycoords='data',
                xytext=(9,8), arrowprops=dict(facecolor='black',shrink=0.05),
                horizontalalignment='right', verticalalignment='top',
            )

#plt.plot([0.0],[0.0],'ro')
#plt.plot([4.49340946],[0.0],'ro')
#plt.plot([7.72525184],[0.0],'ro')
#plt.plot([10.90412166],[0.0],'ro')
#plt.plot([14.06619391],[0.0],'ro')
#plt.plot([17.22075527],[0.0],'ro')
#plt.text(10,5,'Cada punto rojo es una raiz')
#plt.annotate('raiz 1', xy=(-0.7, -0.1), xytext=(-1.5, 20.0),
#            arrowprops=dict(facecolor='black', shrink=0.1,width=1),horizontalalignment='center')
#plt.annotate('raiz 2', xy=(0.7, -0.1), xytext=(1.5, 20.0),
#            arrowprops=dict(facecolor='blue', shrink=0.1,width=1),horizontalalignment='right')
#plt.annotate('raiz 3', xy=(10, -0.1), xytext=(9.5, 20.0),
#            arrowprops=dict(facecolor='blue', shrink=0.1,width=1),horizontalalignment='right')
plt.show()
