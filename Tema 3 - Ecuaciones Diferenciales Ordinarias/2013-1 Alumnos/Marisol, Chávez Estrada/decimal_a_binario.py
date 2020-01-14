# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 19:13:16 2012

@author: marisolchavez
"""

#Este programa convierte numeros a binario
# a)8.37
# b)-4.12
# c)27469.7798


a=8.37

parte_ent=int(a)
#residuo=parte_ent%2


while parte_ent>1:
    modulo=parte_ent%2
    parte_ent=parte_ent/2
    
    print modulo
    
    #y hasta aqui llegue, imprime todos los modulos, faltaria agregar el 1 que va al principio de todo binario
    #(8en binario es 1000, para probar otro numero por ejemplo 10 en bin =1010, entonces si probamos con a=10, el programa solo imprime 010)
  

