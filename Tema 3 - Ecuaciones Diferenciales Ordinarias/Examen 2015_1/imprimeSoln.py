# -*- coding: utf-8 -*-
"""
Created on Tue Apr 01 20:29:14 2014

@author: InfoCabMoodle
"""

def imprimeSoln(X,Y,freq):
    def imprimeEncabezado(n):
        print'\n   x  ',
        for i in range (n):
            print '         y[',i,']    ',
        print 
        
    def imprimeLinea(x,y,n):
        print '%13.4e' %x,
        for i in range (n):
            print '%13.4e'%y[i],
        print
    m=len(Y)
    try: n=len(Y[0])
    except  TypeError: n=1
    if freq==0: freq=m
        
    imprimeEncabezado(n)
    for i in range (0,m,freq):
        imprimeLinea(X[i],Y[i],n)
    if  i!=m-1: imprimeLinea(X[m-1],Y[m-1],n)
    
        