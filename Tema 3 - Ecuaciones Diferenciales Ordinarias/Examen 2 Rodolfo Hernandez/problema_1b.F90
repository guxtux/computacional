	PROGRAM proyrk3

	DIMENSION YA(0:10), YN(0:10), EK(0:3,0:10), Y(0:10)
	PRINT *
	PRINT *, '      ESQUEMA DE RK3 PARA UN CONJUNTO DE ECUACIONES'
	PRINT *

	IM = 2

	Y(1) = 150
	Y(2) = 150

1	PRINT *
!	PRINT *, '¿INTERVALO DE IMPRESIÓN DE T?'
!	READ *, TD

!	PRINT *, '¿NUMERO DE PASOS EN UN INTERVALO DE IMPRESIÓN DE T?'
!	READ *, NS

!	PRINT *, '¿T MAXIMO PARA DETENER LOS CALCULOS?'
!	READ *, XL
	
	TD = 0.05
 	NS = 5
	XL = 1 

	H =  TD/NS

!	PRINT *, '  H =  ', H

	XP = 0
	HH = H/2

	PRINT *

	LI = 0
	PRINT *, 'LIN     T              U               V               X	       Y'
	WRITE(*,98) LI, XP, (Y(I),I=1,IM)
OPEN(1,FILE='problema_1b.dat',	STATUS='UNKNOWN')
28	LI = LI + 1
	DO N = 1, NS
		XB = XP
		XP = XP + H
		XM = XB + HH
		
		J =  1
		DO I = 1, IM
			YA(I) = Y(I)
		END DO
		XA = XB
		CALL FUNCT(EK,J,YA,H)
		
		J = 2
		DO I = 1, IM
			YA(I) = Y(I) + EK(1,I)/2
		END DO
		XA = XM
		CALL FUNCT(EK,J,YA,H)

		J = 3
		DO I = 1, IM
			YA(I) = Y(I) - EK(1,I) + EK(2,I)*2
		END DO
		XA = XM
		CALL FUNCT(EK,J,YA,H)


		DO I = 1, IM
			Y(I) = Y(I) + (EK(1,I) + EK(2,I)*4 + EK(3,I))/6
		END DO
	END DO
	
	WRITE(*,98) LI,XP,(Y(I),I=1,IM),(XP*Y(I),I=1,IM)
	WRITE(1,98) LI,XP,(Y(I),I=1,IM),(XP*Y(I),I=1,IM)
98	FORMAT(1X,I2,F10.6,2X,1P4E16.6/(15X,1P4E16.6))
	IF (XP .LT. XL) GOTO 28
!200	PRINT *
!	PRINT *, 'TECLEA 1 PARA CONTINUAR O 0 PARA TERMINAR'
!	READ *, K
!	IF (K .EQ. 1) GOTO 1
!	PRINT *

CLOSE(1)
	END PROGRAM
!++++++++++++++++++++++++++++++++++++++++++++++
	SUBROUTINE FUNCT(EK,J,YA,H)
	DIMENSION EK(0:3,0:10), YA(0:10)

	EK(J,1) = (0.005*(((YA(1)**2)+(YA(2)**2))**0.5)*YA(1))*H
	
	EK(J,2) = ((-9.9)-(0.005*(((YA(1)**2)+(YA(2)**2))**0.5)*YA(2)))*H
	
	RETURN
	END


