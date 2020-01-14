import math
i=3
fibo=0
a,b=0,1
while b < 10000000000:
	print b
	a,b = b, a+b
while i < 50:
	fibo=(1/(5**0.5))*(0.5*(1+5**0.5)**i - (0.5*(1-5**0.5))**i)
	i=i+1
	print i,fibo
