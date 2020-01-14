#fibonacci
import numpy as num

a=[] #arrglo donde se guarda la secuencia
a.append(1)
a.append(1)
formula=[]
formula.append(1)
formula.append(1)

n=50 #n-esimo termino
i=2 #contador

#para la formula
raiz=5.**.5

rpos=(1+raiz)*.5 #termino suma de raiz
rneg=(1-raiz)*.5 #termino resta de raiz
    #las potencias empiezan en 2 igual que la serie
fnpos=rpos*rpos
fneg=rneg*rneg

while i<n:
    #serie
    an=a[i-1]+a[i-2]
    a.append(an)
    
    #formula 
    fnpos=fnpos*rpos #potencia n de termino suma
    fneg=fneg*rneg    #potencia n de termino resta
    fn=(fnpos-fneg)/raiz
    formula.append(fn)
    i=i+1
    
print(a)
print(formula)
# a partir de cierto numero de fibonaccio en la formula empezamos a ver como se empiezan a aumentar
#numeros decimales a los terminos de la serie. Esto se debe a los errores de redondeo que se van acumulando al
#ir construyendo las potencias de los terminos que se usan en la suma final. 
