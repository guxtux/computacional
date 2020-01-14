import numpy as np  
import matplotlib.pyplot as plt

def coeficientes(xdatos,ydatos):
    m=len(xdatos)
    a=ydatos.copy()

    for k in range(1,m):
        a[k:m]=(a[k:m]-a[k-1])/(xdatos[k:m]-xdatos[k-1])
    return a
def evaluapoli(a,xdatos,x):
    n=len(xdatos)-1
    p=a[n]
    for k in range(1,n+1):
        p=a[n-k] + (x-xdatos[n-k])*p
    return p


xdatos=np.array([-250.0,-200.0,-100.0,0.0,100.0,300.0])
ydatos=np.array([0.0163,0.3180,0.6990,0.8700,0.9410,1.0400])

a=coeficientes(xdatos,ydatos)
print 'x           yInterpol       '
print'_____________________________'

for x in np.arange(100,400.1,50):
    y=evaluapoli(a,xdatos,x)
    
    print '%3.1f  %9.5f '  %(x,y)
    



plt.plot(xdatos,ydatos,'ro',[200,400],[0.99333,0.98598],'b*')
plt.title('calor especifico del aluminio en funcion de T')
plt.xlabel('Temperatura ')
plt.ylabel('Calor especifico Cp')
plt.text(-200,1.1, 'o=valores conocidos *=valores interpolados')
plt.grid()
plt.show()
#100.0    0.94100 
#150.0    0.96662 
#200.0    0.99333 
#250.0    1.02032 
#300.0    1.04000 
#350.0    1.03682 
#400.0    0.98598
