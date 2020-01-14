from math import log

P2=eval(raw_input('ingrese el nivel de potencia, P2, en Watts'))
P1=0.001

dB=10*log(P2/P1)

print 'la potencia, P2, en decibeles respecto a 1mW es:' , dB
