# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:29:42 2012
@author: Luciano Plascencia Valle
Conversión de base decimal a binaria
"""
def binario(num):
    if num<0:
        negativo=True
        num=-1*num
    else: negativo=False
    entero=int(num)
    decimal=num%1
    
    binent,bindec=[ ],[ ]
    i,j=0,-1
    while entero>0:
        binent.append(entero%2)
        entero=entero//2
        i=i+1
        #print entero,binent
    while decimal>0:
        bindec.append(int(decimal*2))
        decimal=decimal*2%1
        j=j-1
        #print decimal,bindec
        
    if negativo: binstr="-"
    else: binstr=""
    for i in range(len(binent)-1,-1,-1):
        binstr=binstr+str(binent[i])
        #print binstr
    binstr=binstr+"."
    for j in range(len(bindec)):
        binstr=binstr+str(bindec[j])
        #print binstr
    return binstr

print "Convertidor de base 10 a base 2\n"
a=[8.37,-4.12,27469.77898,10.7589,0.5,1,2,1.5,10000.125]
for k in range(len(a)):
    print a[k],"(base 10) =",binario(a[k]),"(base 2)"