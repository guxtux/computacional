from math import ln

x=eval(raw_input('ingrese el valor inicial de x'))
xf=eval(raw_input('ingrese el valor final del intervalo a evaluar'))
delta=eval(raw_input('ingrese el valor del intervalo entre cada valor'))

if x=1:
 print 'para x=1 la función no está definida'
else:
 while x <= xf:
 y=ln(1/(1-x))
 x=x+delta
 print y
