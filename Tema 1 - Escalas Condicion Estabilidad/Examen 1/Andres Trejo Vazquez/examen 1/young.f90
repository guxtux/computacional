program young
real:: l, a, b, F, E, k, d, er1, er2, er3, er4, er5, ert, j, er6, er7
double precision:: s
!la fuerza esta dada (Newton)
F= 140 !kp
!la longitud esta dada:
l=125 !cm
!la sección cuadrada:
a=2.5 !cm
b=2.5 !cm
!la flexión:
s=0.171 !cm

!Entonces el valor aproximado de E del modulo de Young, lo vamos a obtener despejando la E y sustituyendo los valores.
 
!despejamos de la ecuación s= (4*(l**3))*F)/((E*a)*b**3)
 
k= (4.*(l**3.)*F)
h= s*(a*b**3.)
d=(k/h)

!write(*,*) d

!Lo que entendi es que a cada dato de: l, a,b, s, F, vamos a truncarlo, obteniendo el error relativo para cada uno de ellos:
!Para la flexión (s) lo pase a centimetros y lo truncare en 0.17.


er1= abs((s-0.17)/s)

!Para a y b lo trucare en 2.0.

er2=abs(a-2.0)/a

er3=abs(b-2.0)/b

!Para la fuerza F no se puede trucar puesto que no tiene decimas. 

er4=abs(F-F)/F 

!Lo mismo sucede para l.
er5=abs(l-l)/l 
 
!print*, er1, er2, er3, er4, er5

! ahora por propagación de error, se suman cada uno de los errores  anteriores, multiplicado por el numero al que estan elevado, asi para  l y b que estan elevados al cubo, se multiplicara por 3 por que son las veces que se propaga el error, que es el error relativo total. 

ert= er1 + er2+ 3*er3 + er4 + 3*er5 

!print*, ert

!ahora sbemos que el error abosluto (en funcion de el modulo de Young) esta dado como la multiplicación del modulo de Young por el error relativo total.  

j= (d*ert)

!print*, j

!entonces el modulo de Young del hierro, con la cota de error encontrada viene dada como:

print*, 'el modulo de Young es de',d

print*, 'con la cota de error de: +/-',j 



print*, '--------------------------------------------------------------'
! ESTA MANERA DE OBTENER LA COTA NO SE SI ES LA  CORRECTA YA QUE EN EL PROBLEMA SE ENTIEDE QUE LOS QUE HAY QUE TRUNCAR SON LOS DATOS QUE NOS DA EL PROBLEMA.

!O esta el caso que puede ser que obtnegamos el error relativo directamente  del modulo de Young 

!Obtenemos el error relativo, poniendo como valor verdadero la obtenida sin truncar 

er6= abs (d-d)/d

!tambien el error relativo con el modulo de yooung truncado en 1.0 entonces:
N 
er7 = abs(d-1.0)/d

!print*, er6, er7 

!entonces el modulo de Young del hierro, con la cota de error encontrada viene dada como:

print*, 'el modulo de Young es de',d 

write(*,100) er7
100 format ('con la cota de error de: +/-',2X,E10.4)

!NOTA: MI DUDA ES SABER SI PRIMER METODO ESTA BIEN PLANTEADO.  
end program young 
