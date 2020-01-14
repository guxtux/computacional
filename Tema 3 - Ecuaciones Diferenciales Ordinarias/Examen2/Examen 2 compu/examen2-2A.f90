PROGRAM MINIMOS
REAL::F,DF,H,X,D2F,H2,A,B,DL,DX,X0,X1,INF
INTEGER::I,J,K
H=0.001
H2=0.05
!DF=(F(X+H)-F(X))/H con esto se calcula el valor de la  derivada de f
!D2F=(((F(X+H+H2)-F(X+H2))/H)-(F(X+H)-F(X))/H)/H2 con esto calculo el valor de la segunda derivada de f
PRINT*, ' La funcion de prueba de este ejemplo es f(x)=(x-2)**2' !en el archivo examen2-2B.f90 se encuentra otro ejemplo con la funcion f(x)=-sin(x)
!ya que se tiene calcu lado el valor de las derivadas de f hay que buscar el minimo de f por medio del criterio de la primera derivada, esto es, cuando f'(x)=0 entonces f(x) sera minimo o maximo, para esto habra que hallar una raiz de f'(x) y esto se hara por medio del metodo de Newton. Esto se realiza a continuacion:
20 PRINT*, 'Da el valor de a del intervalo [a,b]'
READ(*,*), A
PRINT*, 'Da el valor de b del intervalo [a,b]'
READ(*,*), B
DL= 0.0000001 
DX=B-A
X0= (A+B)/2.0
I=0
DO WHILE (ABS(DX) .GT. DL)
         X1 = X0 - ((F(X0+H)-F(X0))/H)/((((F(X0+H+H2)-F(X0+H2))/H)-(F(X0+H)-F(X0))/H)/H2)
         DX = X1-X0
         X0 = X1
         I = I +1
END DO
DF=(F(X0+H)-F(X0))/H
!D2F=((F(X+2*H)-2*F(X+H)+F(X))/(H*H))
D2F=(((F(X0+H+H2)-F(X0+H2))/H)-(F(X0+H)-F(X0))/H)/H2
IF (D2F.GT.0) THEN ! aqui se hace uso de el criterio de la segunda derivada para saber si es un maximo o un minimo el punto x0.
PRINT*, 'El minimo de la funcion es: f(x0)=', F(X0), 'con x0=', x0
ELSE
PRINT*, 'El maximo de la funcion es: f(x0)=', F(X0), 'con x0=', x0
PRINT*, 'Si desea encontrar un minimo y no un maximo ajuste el intervalo [a,b]'
PRINT*, 'para reajustar el intervalo presione 0, presione 1 si desea salir'
READ (*,*), INF
IF (INF.EQ.0) THEN
GOTO 20
ELSE
STOP
END IF
END IF
PRINT*, ' Donde: f`(x0)=', DF, 'f``(x0)=',D2F
END PROGRAM MINIMOS
!++++++++++++++++++++++++++++++++++++++++++++++++++++++++
FUNCTION F(X)
	F= (x-2)**2
END


