from math import exp, cos

V=eval(raw_input('ingrese la amplitud de oscilación, V'))
alfa=eval(raw_input('ingrese el valor del factor de amortiguamiento'))
omega=eval(raw_input('ingrese la velocidad angular'))
t=eval(raw_input('ingrese un valor en el tiempo'))

v=V*(exp(-alfa*t))*cos(omega*t)

print 'el valor de la amplitud de la onda al tiempo', t , 'es:' , v
