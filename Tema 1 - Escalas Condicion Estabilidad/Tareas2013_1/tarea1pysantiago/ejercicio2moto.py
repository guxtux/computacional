import math
T=input("ingresar angulo")
i=1.
x=0.0
y=0.0
b=30017.92
a=.223
c=4395.16298
f=448.0288
while i <= 1000:
	x=x+(-b*math.cos(T)*math.exp(-a*i)+b*math.cos(T))
	y=y+(-c*(i-f*math.exp(-a*i)) + b*math.exp(-a*i)*math.sin(T))
	i=i + 1
	print i,x,y
