#Josue Ruiz Martinez
from scipy import*
from math import*
from scipy.integrate import romberg
g=eval(raw_input("h= "))
rad=(g*pi)/180.
s=sin(rad)
s2=s**2
def f(x): return 1/(sqrt(1-s2*((sin(x))**2)))
r=romberg(f,0,pi/2.,show=True)
R=abs((pi/2.)-r)
e=(R/(pi/2.))*100
print e
