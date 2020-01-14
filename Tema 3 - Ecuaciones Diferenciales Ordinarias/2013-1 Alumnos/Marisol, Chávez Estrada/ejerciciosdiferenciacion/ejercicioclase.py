# -*- coding: utf-8 -*-
"""
EJERCICIO EXTRA (PDF)

SI EL SEGMENTO AB GIRA CON VELOCIDAD ANGULAR CONSTANTE, CON EL METODO DE 
DIFERENCIAS FNITAS DE ORDEN O(h^2) CALCULA AL VELOCIDAD ANGULAR DEL SEGMENTO
BC CONTRA EL ANGULO ALFA

@author: marisolchavez
"""



ALFA = [0, 5, 10, 15, 20, 25, 30]  #en grados
BETA = [1.6595, 1.5434, 1.4186, 1.2925, 1.1712, 1.0585, 0.9561] #en radianes


"""
El incremento h=5 esta en grados, hay que pasarlo a radianes:
    
    h=5*PI/180=0.087266     
"""

h=0.087266


"""
DIFERENCIAS ORDEN O(h^2)

#hacia adelante (la usaremos para alfa=0)

f'(x) = (-f(x+2h) + 4f(x+h) - 3f(x)) /2h
_________________________________________

#central (la usaremos para 0<alfa<30)

f'(x) = (f(x+h) -f(x-h)) /2h
_________________________________________

#hacia atras (la usaremos para alfa=30)

f'(x) = (f(x-2h) - 4f(x-h) + 3f(x)) /2h
"""
print "*********************************************************"
print "POR EL METODO DE DIFERENCIAS, LA VELOCIDAD ANGULAR dB/dt:"
print "*********************************************************"

#la primera derivada en x=0 (hacia adelante)

primera_ad_0 = (-BETA[2]+4*BETA[1]-3*BETA[0] )/(2*h)

"""
B=Beta
A=Alfa
"primera_ad" es es el valor de dB/dA, pero queremos dB/dt:
    dB/dt=dB/dA * dA/dt
    con dA/dt=25    
"""
print "dB/dt para alfa=0 es", 25*primera_ad_0


#la primera derivada en x=5,10,15,20,25 (central)

primera_cen_5 = (BETA[2]-BETA[0])/(2*h)
primera_cen_10 = (BETA[3]-BETA[1])/(2*h)
primera_cen_15 = (BETA[4]-BETA[2])/(2*h)
primera_cen_20 = (BETA[5]-BETA[3])/(2*h)
primera_cen_25 = (BETA[6]-BETA[4])/(2*h)

print "dB/dt para alfa=5 es", 25*primera_cen_5
print "dB/dt para alfa=10 es", 25*primera_cen_10
print "dB/dt para alfa=15 es", 25*primera_cen_15
print "dB/dt para alfa=20 es", 25*primera_cen_20
print "dB/dt para alfa=25 es", 25*primera_cen_25

#la primera derivada en x=30 (hacia atras)

primera_at_30 = (BETA[4]-4*BETA[5]+3*BETA[6] )/(2*h)

print "dB/dt para alfa=30 es", 25*primera_at_30
