# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:29:34 2013

@author: acesimbrote
"""

import math

n=eval(raw_input('n = '))
g = 0
pi = 0
e = 0
i=0.0
j=0.0


while j < n:
    pi = 4.0 * (((-1)**j) / ( (2*j) +1)) + pi
    e = (1.0/(math.factorial(j))) + e
    j=j+1
while i < n:
    i=i+1
    g = (1/i) - math.log((i+1)/i) + g
    


print 'gamma = ',g ,'e = ', e, 'pi = ', pi   

pii = math.pi
ee = math.e

E1=(abs(pii-pi))/pii
E2=(abs(ee-e))/ee


print 'E1 =  ', E1, 'E2 = ',E2 






