from math import COSH, exp

x=eval(raw_input('ingrese el valor x'))

coshiper=(exp(-x) - exp(-x))/2

print 'el coseno hiperbólico de', x , 'es:', coshiper
print 'el coseno hiperbólico de', x , 'con la función intrínseca en PYTHON es:' COSH(x)
