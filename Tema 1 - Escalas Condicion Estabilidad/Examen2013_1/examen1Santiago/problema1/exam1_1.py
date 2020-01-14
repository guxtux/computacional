import math

X=input ("ingrese x:")
i=1

e_x=0.

while i <= X:
	
	e_x=1-i**1+(i**2)/(1*2)+(i**3)/(1*2*3)*(i**4)/(1*2*3*4)+(i**5)/(1*2*3*4*5)
# 	e_x=(1)/((1 + 1/i)**i)     
	i = i + 1
else:
	eErr = math.exp(-X)-e_x
	ErrABS= (abs(eErr))
	print i,e_x,ErrABS
	
