#Josue Ruiz Martinez
h=1./5.
x0=0.0
x1=0.2
x2=0.4
x3=0.6
x4=0.8
x5=1.0
f0=(1)/(3*(1+x0**(4./3.)))
f1=(1)/(3*(1+x1**(4./3.)))
f2=(1)/(3*(1+x2**(4./3.)))
f3=(1)/(3*(1+x3**(4./3.)))
f4=(1)/(3*(1+x4**(4./3.)))
f5=(1)/(3*(1+x5**(4./3.)))
i=(f0+2*f1+2*f2+2*f3+2*f4+f5)*h/2.
print "La integral es:", i
e=(0.24375-i)*100
print " El error porcentual es:", er, "%"


    
