from pylab import*

ec= raw_input('da la ecuaucion a evaluar')# en este caso (90e-3)*(cos(w*t)+sqrt((2.5)**2-(sin(w*t))**2))
h=eval(raw_input('da el valor del incremento'))# en este caso 0.01
w=523.6087#rad/s el valor de la velocidad angular
tetag=linspace(0,180,37)
tetar=linspace(0,pi,37)# angulos entre 0 y 180, de 5 en 5. en radianes
t0=tetar*(1/w)# la funcion de la posicion  esta expresada en funcion del tiempo y estos son los
#valores de t correspondientes a cada angulo


def f(t):
    return eval(ec)

def difcentral(t):
     return (f(t+h)-f(t-h))/2*h

dc=difcentral(t0)
    
      

print ' angulo en grados   aceleracion del piston en m/s^2'
print '***********************************************'
for i in range(len(t0)):
    print ' %4.2f  %9.9f' %(tetag[i],dc[i])



