# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:29:42 2012
@author: Luciano Plascencia Valle
Conversión de base decimal a binaria
"""

a=[8.37,-4.12,27469.77898]
num=10.758
entero=int(num)
decimal=num%1

bin,i,j=0.,0,-1
while entero>0:
    bin=bin+entero%2*10**i
    entero=entero//2
    i=i+1
    print entero,bin

while decimal>0:
    bin=bin+int(decimal*2)*10**j
    decimal=decimal*2%1
    j=j-1
    print decimal,bin
print bin