import numpy as np
import matplotlib.pyplot as plt
#FRANCISCO JAVIER RAMIREZ MORALES
k=1# el parametro que da dimenciones de fuerza a f
m=1#kg   es la masa de la gota
s=k/m
g=9.8#m/s gravedad 
vt=g/s
#las formulas usadas aqui estan justificadas en el correspondiente archivo de texto
#(g/s)*(1-np.exp(-s*t))
print s,vt
#.0098 
def v(t):
    return (g/s)*(1-np.exp(-s*t))
    
t1=np.arange(0.0,10.0,0.1)

def y(t):
    return (g/s)*(t-(1/s)*(1-np.exp(-s*t)))

t2=np.arange(0.0,10.0,0.1)
plt.plot(t1,v(t1),'bo',t2,y(t2),'r*')
plt.xlabel('tiempo')
plt.ylabel('velocidad( o ) , altura ( *) ')
plt.title('caida gota de agua con resistencia del aire para K=1')
plt.grid()
plt.show()


