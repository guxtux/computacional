from numpy import arctan
n = 3
senant = 1
while n <=20:
    senant /= (2*(1+(1-senant*senant)**0.5))**0.5
    print n, '\t', senant, '\t', senant*2.0**(n-1), '\t',4.0*arctan(1), '\t', senant*2.0**(n-1)-4.0*arctan(1),
    n +=1