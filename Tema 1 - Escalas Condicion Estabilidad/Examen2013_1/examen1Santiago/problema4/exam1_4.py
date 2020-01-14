import math
i=3.
Sin_n=1.
j=3.
p_n=0.
while i <= 20:
	Sin_n =(math.sin(i))/(math.sqrt(2*(1 + (1 -math.sqrt((math.sin(i)))))))
	i=i+1
	print i,Sin_n
while j <= 20:
	p_n = 2**(i-1)*math.sin(i)
	i = i+1
	print i,p_n
