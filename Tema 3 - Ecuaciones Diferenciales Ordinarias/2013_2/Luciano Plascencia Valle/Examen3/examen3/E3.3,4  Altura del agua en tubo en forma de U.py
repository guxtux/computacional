# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "CÁLCULO DE LA ALTURA DEL AGUA EN UN TUBO EN FORMA DE U"
print "USANDO EL MÉTODO DE EULER (=RK1):"
print " Problema 3: SIN FRICCIÓN: B=0"
print " Problema 4: CON FRICCIÓN: B=0.8\n"
from ecdif import *

def dYa(Ya,t=0.):
    ya,dya=Ya
    d2ya=-2*g/L*ya-B/L*dya
    return np.array([dya,d2ya])

#Condiciones iniciales [CGS]: como ya(t)=-yb(t), entonces 
#ya(0)-yb(0) = 0.002m = 0.2 cn = 2*ya(0)=2*ya0. Luego:
ya0=0.1
dya0=0.
Ya0=[ya0,dya0]
t0=0.; tn=10.; h=0.001  #Extremos de t y paso h [horas]
g=981; L=100.           #Constantes [CGS].
#Duda: ¿Para que dan el valor del radio r=5 cm, si no se usa? 

#Problema 3: Caso sin fricción
B=0.            #Coef. de fricción [m/s]
ya_0,dya_0=rk(1,dYa,Ya0,t0,tn,h).T

#Problema 4: Caso con fricción
B=80            #Coef. de fricción [cm/s]
ya_B,dya_B=rk(1,dYa,Ya0,t0,tn,h).T

print "Tiempo (t) [s]  Altura ya(t) (B=0)  Altura ya(t) (B=0.8)"
print "--------------  ------------------  --------------------"
for t in np.arange(t0,tn+h,h*100):
    j=int(round(t/h))
    print "%6.3f" %t,"          %6.3f" %ya_0[j],"+ O(0.001)  %6.3f" %ya_B[j],"+ O(0.001)"
print "\nComo podemos apreciar en la gráfica:" 
print "3)-Para el caso sin fricción: el máximo se presenta en cada periodo"
print "   de oscilación y corresponde al valor inicial ya(0) = %.3f m." %ya0
print "  -El mínimo corresponde a este mismo valor, pero con signo menos."
print "   Por tanto, en este caso tenemos un oscilador armónico de amplitud"
print "   ya(0), como era de esperarse."
print "  -Notemos que los valores numéricos de los máximos van aumentando,"
print "   lo cual no sería posible físicamente, sino que se debe a errores"
print "   de cálculo de la máquina."
print "4)-Para el caso con fricción: tenemos un oscilador amortiguado,"
print "   como también era de esperarse."

t=np.arange(t0,tn+h,h)
plt.title(u"Altura del agua en un tubo con forma de U")
plt.plot(t,ya_0,label=u"Sin fricción: B=0 cm/s")
plt.plot(t,ya_B,label=u"Con fricción: B=80 cm/s")
plt.xlabel("Tiempo t [s]")
plt.ylabel(u"Altura del agua ya(t) [cm]")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()
