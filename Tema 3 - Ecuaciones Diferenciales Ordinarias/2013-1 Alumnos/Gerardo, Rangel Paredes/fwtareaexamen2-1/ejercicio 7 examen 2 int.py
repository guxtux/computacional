from scipy import*
from math import*
from scipy.integrate import romberg
grados = eval(raw_input("ingrese los grados en los que quiere calcular h: "))
rad = (grados*pi)/180.
s = sin(rad)
s2 = s**2
def f(x): return 1/(sqrt(1-s2*((sin(x))**2)))
resultado = romberg (f, 0, pi/2., show = True)

r= abs((pi/2.)-resultado)
error = (r/(pi/2.))*100
print error
