# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 15:48:21 2013

@author: IIFCES
"""

from scipy import integrate,pi,sin
import matplotlib.pyplot as plt
from imprimeDatos import *
from integraEDO import *

def F(x,y):
    F = zeros(2)
    F[0] = y[1]
    F[1] = -sin(y[0])
    return F

x = 0.0
y = array([1.0,0.0])
xAlto = 20
h = 0.01
freq=10

X, Y = integra(F,x,y,xAlto,h)
#imprimeSoln(X,Y,freq)
plt.plot(X,Y[:,0],label=r'$\theta_{0}= 1 rad$')
plt.xlabel('tiempo [s]')
plt.ylabel(u'Posición [radianes]')
plt.title(u'Solución del péndulo')
plt.axhline(y=0.0, color='k', linestyle='-')
plt.axis([0.0,20.,-1.5,1.5])
#plt.xticks([0, pi, 2*pi, 3*pi, 4*pi,5*pi],[r'$0$',r'$\pi$',r'$2\pi$',r'$3\pi$', r'$4\pi$',r'$5 \pi$'], fontsize=16)


#x = 0.0
#y = array([0.0,0.3490])
#xAlto = 5.0*pi
#h = 0.01
#
#X, Y = integra(F,x,y,xAlto,h)
#imprimeSoln(X,Y,freq)
#plt.plot(X,Y[:,0],label=r'$\theta_{0}= 0.3490 rad$')
#plt.legend(loc='upper right')
#l = plt.axhline(y=0.0, color='k', linestyle='-')
#plt.show()

#PA = []
#aA = []
#a = 0
#da = 0.01
#
#while (a < 0.999*pi):
#    a = a + da
##    b=a*180/pi
#    k= ((4.0/sqrt(2.0))*sqrt(1/9.81))
#    P = integrate.quad(lambda x: (k*(1.0/sqrt(cos(x)-cos(a)))),0,a )
#    print a, P[0]
##    lineadedatosP='Angulo = %1.1f\xb0=%1.2f rad PERIODO = %1.3f s \n' % (b,a,P[0])
#   # print >> datosP, lineadedatosP
#    
#    PA.append(P[0])
#    aA.append(a)
#
#
#    
#plt.plot(aA,PA)
#plt.xlabel('Angulo (radianes)')
#plt.ylabel('Periodo (s)')
#plt.axis(ymin=0.0)
#plt.axhline(y=2.006409, color='k', linestyle='--')
#plt.title(u'Relación entre período y ángulo inicial',position=(0.5,1.05))
#plt.plot(1,2.1391, 'bo')
#plt.plot(0.3490,2.0215, 'ro'P = integrate.quad(lambda x: (k*(1.0/sqrt(cos(x)-cos(a)))),0,a ))
#plt.plot(0.05,2.00638,'go')
#plt.legend(loc='upper left')
#ax2 = plt.twiny()
#ax2.set_xlim(0, pi)
#ax2.set_xticks([0, pi/4, pi/2, 3*pi/4, pi])
#ax2.set_xticklabels([r'0',r'$\pi/4$',r'$\pi/2$',r'$3\pi/4$', r'$\pi$'])

plt.show()
def P(x):
    k= ((4.0/sqrt(2.0))*sqrt(1/9.81))
    return k*(1.0/sqrt(1 - (sin(1./2.)**2)*(sin(x)**2)))
    
print u'El período del péndulo es = ', integrate.quad(P,0.0,pi/2.0)[0]
