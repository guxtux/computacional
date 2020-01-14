#metodo de Horner
import matplotlib.pyplot as plt

an=(48.,100.,70.,-20.,2)
x=-4
xv=[]
pol=[]
while x<-0.9:
    n=4
    b=an[n]
    while n>0:
        n=n-1
        b=an[n]+x*b    
    
    xv.append(x)
    pol.append(b)
    x=x+.5
    

print(xv)
print(pol)

plt.plot(xv,pol)
plt.ylabel("polinomio")
plt.xlabel("x")
plt.show()


