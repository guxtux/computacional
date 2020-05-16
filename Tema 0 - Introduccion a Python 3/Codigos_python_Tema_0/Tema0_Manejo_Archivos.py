# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:38:16 2020

@author: gusto
"""

import numpy as np


#%%
#Primer modo para guardar datos en un archivo
archivo01 = open('potencias01.txt', 'w')
for i in range(1, 100):
    print(i, i**2, i**3, i**4, sep=',', file=archivo01)
archivo01.close()
#%%

#%%
#Segundo modo para guardar archivos con formato
archivo02 = open('potencias02.txt', 'w')
for i in range(1, 100):
    archivo02.write('{0:} \t {1:} \t {2:} \t {3:} \n'.format(i, i**2, i**3, i**4))
archivo02.close()
#%%

#%%
#Tercer modo para guardar archivos usando numpy
#archivo03 = open('potencias03.txt', 'w')
x = []
y = []
z = []
for i in range(1, 100):
    x.append(i)
    y.append(i**2)
    z.append(i**3)

#np.savetxt('potencias03.txt', (x, y,z), delimiter=',')
np.savetxt('potencias03.txt',np.transpose([x, y,z]), delimiter=',', fmt='%d')
#archivo03.close()
#%%

#%%
#Cuarto modo para guardar archivo, ahora con numpy
x = np.array([[1, 2, 3], 
              [4, 5, 6],
              [7, 8, 9]], np.int32)

np.savetxt("test.txt", x)
np.savetxt("test2.txt", x, fmt="%2.3f", delimiter=",")
np.savetxt("test3.txt", x, fmt="%04d", delimiter=" :-) ")
#%%

    
#%%
#Incorporando cabeceras en un archivo de datos

t = np.arange(0.1, 30., 0.5)
d = np.arange(0.1, 60., 1)

comentario1 ='#Este es un comentario sobre el archivo'
comentario2 = '#Sirve de ejemplo para diferenciar un comentario de una cabecera'
cabecera = 'Tiempo \t Velocidad'

with open('potencias05.txt', 'a') as f1:
    f1.write(comentario1 + '\n')
    f1.write(comentario2 + '\n')
    f1.write(cabecera + '\n')
    f1.close()
    
with open('potencias05.txt', 'a') as f2:
    for i in range(len(t)):
        v = d[i]/t[i] 
        f2.write('{0:} \t {1:1.4f} \n'.format(i, v))
    f2.close()
#%%