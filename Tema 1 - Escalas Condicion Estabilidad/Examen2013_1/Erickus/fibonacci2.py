# -*- coding: utf-8 -*-

import math

n=3


for i in range ( 3 , 50 ):
    
    n=(1/math.sqrt(5))*(((0.5*(1+math.sqrt(5)))**n)-((0.5*(1 - math.sqrt(5)))**n))
    
    print n