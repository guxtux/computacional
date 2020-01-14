from numpy import *
from newtonpoli import *
xd=array([-3.0,2.0,-1.0,3.0,1.0])
yd=array([0.0,-5.0,-4.0,12.0,0.0])
a=coeffts(xd,yd)
print "El polinomio es:P(x)=",a[0],"+",a[1],"*(x+3)","+",a[2],"*(x+3)(x-2)",a[3],"*(x+3)(x-2)(x+1)",a[4],"*(x+3)(x-2)(x+1)(x-3)"
