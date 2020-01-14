from pylab import*
import matplotlib.pyplot as plt
#constantes
# comportamiento de temperatura de pieza metalica que se calienta uniforme a tasa constante
#constantes
p=300.0#[k/m^3] densidad del metal
c=900.0#[j/kg*K]calor especifico del metal
v=0.001#[m^3]volumen del metal
A=0.25#[m^2] area de la superficie del metal
hc=30.0#[j/m^2*k]coeficiente de transferencia de calor
h=6# valor del incremento
s=5.67e-8#cte de stefan-boltzman
e=0.8#emisividad del metal
T=298.0#[k]temperatura inicial
q=3000.0#[w] tasa de transferencia de potencia electrica

def f(T,t): return (A/(p*c*v))*(q + e*s*(298.0**4.0 - T**4.0 )+hc*(298.0- T ))

tf=eval(raw_input('a que tiempo  despues quieres saber la temperatura ,en minutos'))
tseg=tf*60# convertimos a segundos el tiempo 

# metodo RK4 - con regla simpson 3/8
t=arange(0,tseg,6.0)# intervalo en el que se va acalcular la temperatura
temp=[]
temp.append(298.0)
for i in range(len(t)-1):
    k1 =h*f(T,t[i])
    k2 =h*f(T+ k1/3,t[i]+h/3)
    k3 =h*f(T+(k1/3)+(k2/3),t[i]+2*h/3)
    k4 =h*f(T+k1-k2+k3,t[i]+h)
    T = T +(0.125)*(k1+(3*k2)+(3*k3)+k4)
    temp.append(T)
    

print' tiempo[s]   temperatura[k] '
print'*************************'
for i in range(len(t)-1):
    print ' %5.6f      %5.6f' %(t[i],temp[i])

plt.plot(t,temp,'ro')
plt.xlabel('tiempo[s]')
plt.ylabel('temperatura[k]')
plt.title('aumento de temperatura de una barra metalica')
plt.show()
plt.grid()

