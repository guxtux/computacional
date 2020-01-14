# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "TIEMPO QUE TARDARÁ EN VACIARSE UN DEPÓSITO CÓNICO"
print "LLENO DE AGUA DESDE UNA ALTURA y0=50 cm HASTA UN"
print "ORIFICIO EN EL FONDO QUE VA DE yn=8 cm A yf=0 cm.\n"
from ecdif import *
import numpy as np

def dt_dy(t,y): return -1/sqrt(2*g*(y0-y))
def t(y): return sqrt(2*(y0-y)/(g))
def v(y): return sqrt(2*g*(y0-y))

#Constantes y condiciones iniciales [CGS]:
g=981           #Constante g
r=2             #Radio del orificio del fondo
yn=r/.25        #Altura donde "inicia" el orificio: yn=8 cm
yf=0.           #Altura donde "termina" el orificio
t0=0.; y0=50.    #Condiciones iniciales
#Altura del cilindro de radio r y volumen equivalente al cono truncado
y0=(y0**3-yn**3)/3/yn**2    
h=0.1          #Paso

print "Calcularemos el tiempo que toma en salir el agua"
print "en ambas alturas: al inicio y al final del orificio,"
print "en donde el agua tiene velocidades de salida:"
print "v(yn=8 cm) = %.0f cm/s" %v(yn)
print "v(yf=0 cm) = %.0f cm/s" %v(yf)

print "\na) Usando el método de Euler (=RK1):"
tn=rk(1,dt_dy,t0,y0,yn,h)[-1]
tf=rk(1,dt_dy,t0,y0,yf,h)[-1]
print "   t(yn=%i cm) = %.2f + O(%.1f) s = %.3f + O(%.3f) min." %(yn,tn,abs(h),tn/60,abs(h/60))
print "   t(yf=%i cm) = %.2f + O(%.1f) s = %.3f + O(%.3f) min." %(yf,tf,abs(h),tf/60,abs(h/60))
print "\nb) Solución analítica: t(y) = sqrt(2*(y0-y)/(g))"
tn=t(yn)
tf=t(yf)
print "   t(yn=%i cm) = %.4f s = %.6f min." %(yn,tn,tn/60)
print "   t(yf=%i cm) = %.4f s = %.6f min." %(yf,tf,tf/60)

"""
print 6/sqrt(g)

print "Tiempo (t) [s]  Altura ya(t) (B=0)  Altura ya(t) (B=0.8)"
print "--------------  ------------------  --------------------"
for y in np.arange(y0,yn+h,h):
    j=int(round(y/h))
    print "%6.3f" %y,"          %6.3f" %t[j],"+ O(0.001)"

y=np.arange(y0,yn+h,h)
plt.title(u"Altura del agua en un tubo con forma de U")
plt.plot(t,ya_0,label=u"Sin fricción: B=0 cm/s")
plt.plot(t,ya_B,label=u"Con fricción: B=80 cm/s")
plt.xlabel("Tiempo t [s]")
plt.ylabel(u"Altura del agua ya(t) [cm]")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()
"""