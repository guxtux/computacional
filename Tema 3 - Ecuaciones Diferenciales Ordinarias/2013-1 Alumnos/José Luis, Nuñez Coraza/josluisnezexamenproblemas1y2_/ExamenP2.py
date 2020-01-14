import mathplotlib as plt
x=[-4.0,-3.5,-3.0,-2.5,-2.0,-1.5,-1.0]
a=[2.0,-20.0,70.0,100.0,48.0]
for m in range(len(x)):
	b=0
	n=len(a)
	while n>0:
		n=n-1
		b=a[n]+x[m]*b 
	print 'P(',x[m],')=', '%5f' %(b)	

plt.plot(x,b)
plt.show()