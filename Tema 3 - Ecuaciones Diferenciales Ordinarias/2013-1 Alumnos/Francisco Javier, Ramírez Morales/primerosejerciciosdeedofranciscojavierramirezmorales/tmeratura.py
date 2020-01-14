from pylab import*
import matplotlib.pyplot as plt
#constantes
p=300.0
c=900.0
v=0.001
A=0.25
hc=30.0
h=0.25
s=5.67e-8
e=0.8
T=473.0

def f(T,t): return (A/(p*c*v))*(e*s*(297.0**4.0 - T**4.0 )+hc*(297.0- T ))



t=arange(0,100.25,0.25)
temp=[]
temp.append(473.0)
for i in range(len(t)-1):
    k1 =h*f(T,t[i])
    k2 =h*f(T+ k1/2,t[i]+h/2)
    k3 =h*f(T+k2/2,t[i]+2*h/2)
    k4 =h*f(T+k3,t[i]+h)
    T = T +(0.166666)*(k1+2*k2+2*k3+k4)
    temp.append(T)
    

print' tiempo   temperatura '
print'*************************'
for i in range(len(t)-1):
    print ' %5.6f      %5.6f' %(t[i],temp[i])

plt.plot(t,temp,'b.')
plt.xlabel('tiempo[s]')
plt.ylabel('temperatura[k]')
plt.title('enfriamiento de una barra metalica')
plt.show()
plt.grid()

print len(t),len(temp)


