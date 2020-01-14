from numpy import *
from newtonpoli import *
xd=array([-250.0,-200.0,-100.0,0.0,100.0,300.0])
yd=array([0.0163,0.318,0.699,0.870,0.941,1.04])
a=coeffts(xd,yd)
x=200.0
print "El calor especifico para T=200C es:",evalPoli(a,xd,x)
x=400.0
print "El calor especifico para T=400C es:",evalPoli(a,xd,x)
