PROGRAM ejercicio9RK4
REAL :: K1, K2, K3, K4,K,M,W, E, H, I, A,B, L1, L2, L3, L4, Y,Z,T 
COMMON L,C,E,R

 A=0.0 !INICIO INTERVALO
 B=10.0 !'FIN DE INTERVALO'
	 I=B-A ! INTERVALO

PRINT *, 'NUMERO DE PUNTOS A EVALUAR'
READ *, N

!EL PASO QUE VA A DAR ENTRE CADA PUNTO
H=I/N
PRINT *, 'H= ', H
!--------------------------'
!INICIALIZANDO LAS VARIABLES
T=0
Y=0  !CONDICIONES INICIALES "y" EN CERO
Z=0  !CONDICIONES INICIALES "Z" EN CERO

!SE HACE LA CUENTA PARA TENER EN TERMINOS DE LAS COORDENADAS CANONICAS

OPEN (UNIT=6, FILE='ejercicio9.dat', STATUS='replace')
DO J= 1,N

T=T+H  !el paso en el tiempo

K1=H*FUN(Y,Z,T)
IF (T .LE. 1.0) THEN 
L1=H*FUN2(Y,Z,T)
ELSE 
L1=H*FUN3(Y,Z,T)
END IF

K2=H*FUN(Y+ K1/2.,Z+ L1/2., 3*H/2.)
IF (T .LE. 1.0) THEN 
L2=H*FUN2(Y+ K1/2.,Z+ L1/2., 3*H/2.)
ELSE
L2=H*FUN3(Y+ K1/2.,Z+ L1/2., 3*H/2.)
END IF

K3=H*FUN(Y+ K2/2., Z+ L2/2., 3*H/2.)
IF (T .LE. 1.0) THEN 
L3=H*FUN2(Y+ K2/2., Z+ L2/2., 3*H/2.)
ELSE 
L3=H*FUN3(Y+ K2/2., Z+ L2/2., 3*H/2.)
END IF

K4=H*FUN(Y+K3, Z+L3, 2*H)
IF (T .LE. 1.0) THEN 
L4=H*FUN2(Y+K3, Z+L3,2*H)
ELSE 
L4=H*FUN3(Y+K3, Z+L3,2*H)
END IF

!EXPRESION CANONICA
Y=Y+(K1+K2*2.0+K3*2.0+K4)/6.0 !valor de la derivada parcial 
Z=Z+(L1+L2*2.0+L3*2.0+L4)/6.0

PRINT 82, T, Z, Y
82 FORMAT (1X, F10.6,7X, 1PE15.6, 7X, 1PE15.6)
END DO
 CLOSE(6)

END PROGRAM ejercicio9RK4
!+++++++++++++++++++++++++++++++++++++
FUNCTION FUN(Y,Z,T)  !se introduce la funcion de interes, ES DECIR LA DERIVADA PARCIAL
FUN = Z     !Y'= F(Y,Z,T) = Z     Y(0)=0 !posicion inicial
RETURN
END 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FUNCTION FUN2(Y,Z,T)  !se introduce la funcion de interes 0<T<=1
REAL :: K,E,M,W	
K=3.2 !costante del resorte (kg/s^2)
E=0.5 !factor de amortiguamiento 
M= 5 !masa (kg)
W = sqrt(k/M)

FUN2 = 1.0/M  - 2.0*E*W*Z -(W**2.0)*Y   !Z'=G(Y,Z,T)   Z(0)=0
RETURN
END 

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
FUNCTION FUN3(Y,Z,T)  !se introduce la funcion de interes   T>1
REAL :: L,e,m,f
L=3.2 !costante del resorte (kg/s^2)
e=0.5 !factor de amortiguamiento 
m= 5 !masa (kg)
f = sqrt(L/m)
 
FUN3 = -2.0*e*f*Z -(f**2.0)*Y   !Z'=G(Y,Z,T)   Z(0)=0
RETURN
END 

!PARA VER COMO ES LA TRAYECTORIA EN EL TIEMPO PARA DISTINTOS VALORES DE R TENGO QUE GRAFICAR LA VARIABLE Z  CONTRA EL TIEMPO T  

