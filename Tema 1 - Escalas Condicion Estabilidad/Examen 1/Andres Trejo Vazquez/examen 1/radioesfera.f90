PROGRAM errorrela
 REAL :: e,ei
 REAL*4 :: E1,E2,E3   

ei=10E-3 ! error inherente a  las medidas cuando se tomo el radio con instrumentacion
 
n=23. ! son los elemntos en la mantisa que se pueden ocupar para cifras significativas

e=1./2.*(2.**(1.-n))! es la cota del error relativo que se cumple cuando el redondeo es por aproximacion, REAL*4 (SON 24 BITS PARA LA MANTISA Y UNO PARA EL SIGNO)

! se ponen los valores de los errores relativos maximos obtenidos para cada alternativa del medicion

E1 = ei + 2.*e
E2 = 1./2.*ei + 3.*e
E3 = 1./3.*(ei+8.*e)

! se puede notar que la tolerancia o el error relativo maximo no excede el 0.05%, debido a las condicion inicial de trabajar con REAL*4

write(*,100) E1,E2,E3
100 format (F10.8, 2X, F10.8,2X, F10.8)
! SE IMPRIMEN LOS ERRORES RELATIVOS MAXIMOS PARA CADA ALTERNATIVA DE MEDIR EL RADIO DE UNA ESFERA. 

end program errorrela
