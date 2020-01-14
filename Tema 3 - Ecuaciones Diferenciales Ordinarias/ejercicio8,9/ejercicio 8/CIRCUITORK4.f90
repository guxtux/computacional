PROGRAM CIRCUITORK4
REAL :: K1, K2, K3, K4, L, C, E, R, H, I, A,B, L1, L2, L3, L4, Y,Z,T,Y0 
COMMON L,C,E,R

 A=0.0 !INICIO INTERVALO
 B=5.0 !'FIN DE INTERVALO'
	 I=B-A ! INTERVALO

PRINT *, 'NUMERO DE PUNTOS A EVALUAR'
READ *, N


!EL PASO QUE VA A DAR ENTRE CADA PUNTO
H=I/N
PRINT *, 'H= ', H
!PRINT *,'--------------------------------------------'
!PRINT *,'	T	   Z		Y'
!PRINT *,'--------------------------------------------'
!INICIALIZANDO LAS VARIABLES
T=0
Y=0  !CONDICIONES INICIALES "y" EN CERO
Z=0  !CONDICIONES INICIALES "Z" EN CERO

!SE HACE LA CUENTA PARA TENER EN TERMINOS DE LAS COORDENADAS CANONICAS

OPEN (UNIT=6, FILE='CIRCUITOR300.dat', STATUS='replace')
DO J= 1,N

T=T+H  !el paso en el tiempo

K1=H*FUN(Y,Z,T)
L1=H*FUN2(Y,Z,T)

K2=H*FUN(Y+ K1/2.,Z+ L1/2., 3*H/2.)
L2=H*FUN2(Y+ K1/2.,Z+ L1/2., 3*H/2.)

K3=H*FUN(Y+ K2/2., Z+ L2/2., 3*H/2.)
L3=H*FUN2(Y+ K2/2., Z+ L2/2., 3*H/2.)

K4=H*FUN(Y+K3, Z+L3, 2*H)
L4=H*FUN2(Y+K3, Z+L3,2*H)

!EXPRESION CANONICA
Y=Y+(K1+K2*2.0+K3*2.0+K4)/6.0 !valor de la derivada parcial 
Z=Z+(L1+L2*2.0+L3*2.0+L4)/6.0

PRINT 82, T, Z, Y
82 FORMAT (1X, F10.6,7X, 1PE15.6, 7X, 1PE15.6)
END DO
 CLOSE(6)
END PROGRAM CIRCUITORK4
!+++++++++++++++++++++++++++++++++++++
FUNCTION FUN(Y,Z,T)  !se introduce la funcion de interes, ES DECIR LA DERIVADA PARCIAL
FUN = Z     !Y'= F(Y,Z,T) = Z     Y(0)=0
RETURN
END 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FUNCTION FUN2(Y,Z,T)  !se introduce la funcion de interes
REAL :: L,C,E,R
L=200.0 !henry AUTOINDUCTANCIA 
 C= 0.001 !faradio CAPACITANCIA
E= 1.0 ! voltS   VOLTAJE
R=300.0 !!!VALORES DE LA RESISTENCIA 0.0, 50,100,300
FUN2 = -(R/L)*Z - (1.0/(L*C))*Y + E/L   !Z'=G(Y,Z,T)   Z(0)=0
RETURN
END 

!PARA VER COMO ES LA CORRIENTE EN EL TIEMPO PARA DISTINTOS VALORES DE R TENGO QUE GRAFICAR LA VARIABLE Z  CONTRA EL TIEMPO T  

!En la terminal debemos poner para graficar gnuplot> plot 'CIRCUITOR0.dat' u 1:2, 'CIRCUITOR50.dat' u 1:2, 'CIRCUITOR100.dat' u 1:2, 'CIRCUITOR300.dat' u 1:2


!para hallar el factor de amortuguamiento se utiliza la siguiente expresion a = R/2C y para la frecuencia de osilacion del circuio w=1/sqrt(LC)
!R=0, a=0 y w=2.2360 hz
!R=50, a=25,000 ohm/F y w=2.2360 hz
!R=100, a=50000 ohm/F y w=2.2360 hz
!R=300, a=150000 ohm/F y w=2.2360 hz
