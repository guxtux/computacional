import math 
c=input ("Ingrese m/k:")
i=1.
vf=0.0
yr1=0.0
yr2=0.0
g=9.81
while i <= 1000:
	vf =vf + (-c*g*(1-math.exp(c*i)))
	yr1=yr1 +(-c*g*(i-c*math.exp(c*i)))
	yr2=yr2 +((-g*i**2)/(2))
	i=i+1
	print vf,yr1,yr2 
