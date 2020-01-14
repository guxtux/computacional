from pylab import*

ec= raw_input('da la ecuaucion a evaluar')# en este caso (6877.9433/(1+(4.66185e-2)*sin(t+0.501066)))
h=eval(raw_input('da el valor del incremento'))# en este caso 0.04

tetag=linspace(0,360,361)# angulos entre 0 y 360 de 1 en 1  en grados
tetar=linspace(0,2*pi,361)# angulos entre 0 y  360, de 1 en 1 en radianes



def f(t):
    return eval(ec)

def difcentral(t):#para la primer derivada
     return (f(t+h)-f(t-h))/2*h

def dif2central(t):# para la segunda derivada
     return (f(t+h)-2*f(t)+f(t-h))/(h*h)
dc=difcentral(tetar)
dc2=dif2central(tetar)   
     

print ' angulo en grados   primera derivada        segunda derivada'
print '***********************************************'
for i in range(len(tetar)):
    print ' %4.2f  %9.9f %9.9f' %(tetag[i],dc[i],dc2[i])


#obtenemos los siguientes valores reelevantes para una primera aproximacion
#angulo en grados   primera derivada        segunda derivada
#***********************************************
#61.00      -0.002378446                 292.680328519
#62.00       0.005793893                 292.666675110  tenemos  un minimo entre estos valores
#63.00       0.013964939                 292.587682875


#240.00     0.012712203                  -352.586726879
#241.00     0.002865964                  -352.696627864 tenemos un maximo entre estos valores
#242.00    -0.006981403                  -352.667593557




#  CALCULO DEL VALOR MINIMO


tg=linspace(61,63,21) # de 61 a 63 en saltos de 0.1  en grados
tr=tg*((2*pi)/360) #  lo mismo pero en radianes 

dcfina=difcentral(tr)

print ' angulo en grados        primera derivada '
print '***********************************************'
for i in range(len(tr)):
    print ' %4.2f   %9.9f  '   %(tg[i],dcfina[i])


# OBTENEMOS UNA MEJOR APROXIMACION  Y EL VALOR QUE TOMAMOS COMO VALOR MINIMO ES

# angulo en grados   primer derivada

#       61.30         0.000073283  valor del angulo para el que se tiene el minimo
