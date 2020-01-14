m=eval(raw_input('ingrese la masa, m'))
h=eval(raw_input('ingrese la altura, h'))
v=eval(raw_input('ingrese la velocidad, v'))

g=9.81

Ep=m*g*h
Ec=m*v*v*(1/2)

E=Ep + Ec

print 'La energía total es:' , E
