#Josue Ruiz Martinez
from math import*
h1=1.
i1=(cos(2*acos(-1.))+4*cos(2*acos(0.))+cos(2*acos(1.)))*((h1)/(3))
h2=0.5
i2=(cos(2*acos(-1.))+4*cos(2*acos(-0.5))+cos(2*acos(0.)))*((h2)/(3))
i3=(cos(2*acos(0.))+4*cos(2*acos(0.5))+cos(2*acos(1.)))*((h2)/(3))
ii2=i2+i3
h3=1./3.
i4=(cos(2*acos(-1.))+4*cos(2*acos(-2./3.))+cos(2*acos(-1./3.)))*((h3)/(3))
i5=(cos(2*acos(-1./3.))+4*cos(2*acos(0.))+cos(2*acos(1./3.)))*((h3)/(3))
i6=(cos(2*acos(1./3.))+4*cos(2*acos(2./3.))+cos(2*acos(1.)))*((h3)/(3))
ii3=i4+i5+i6
print "El valor de la integral en el bloque 2 es:", i1
print "El valor de la integral en el bloque 4 es:", ii2
print "El valor de la integral en el bloque 6 es:", ii3
