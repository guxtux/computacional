# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:30:20 2013

@author: est5
"""

import math
suma=1.0
k=1
l=range(5)
for i in l:
   x=float(10**(i-1))
   term=x   
   while math.fabs(term) > 0.00001:
       suma=suma-term
       k=k+1
       term=term*(-x/k)
   print "La aproximacion para x=",x,"es:",suma   
   print "El error absoluto es:",math.fabs(math.exp(-x)-suma)   
       
   
   