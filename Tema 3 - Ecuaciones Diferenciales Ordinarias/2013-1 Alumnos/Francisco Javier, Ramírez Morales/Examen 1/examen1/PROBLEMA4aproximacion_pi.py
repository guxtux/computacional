#RAMIREZ MORALES FRANCISCO JAVIER
from pylab import*
a=range(0,21)

for i in a:
    a[i]=(2**(i-1))*sin((2*pi)/(2**i))
    print a[i]
    
