# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
x = eval(raw_input("ingrese el numero en base decimal: "))
y = int(x)

while y>1:
    y = y//2
    w = y%2
    print w  