from numpy import *
from neville import *
xd=array([0.0,1.525,3.050,4.575,6.10,7.625,9.150])
yd=array([1,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])
print 'Utiizando el metodo de Neville P(10.5)=',neville(xd,yd,10.5)
