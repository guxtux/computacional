	PROGRAM problema2

	DIMENSION YA(0:10), YN(0:10), EK(0:4,0:10), Y(0:10)
	PRINT *
	PRINT *, 'Esquema de RK4'
	PRINT *

	IM = 2

	Y(1) = 0
	Y(2) = 0

1	PRINT *
	PRINT *, 'Intervalo de impresion de T'
	READ *, TD

	PRINT *, 'Numero de pasos en impresion de T?'
	READ *, NS

	PRINT *, 'T maximo para detener los pasos?'
	READ *, XL

	open(1, file='datprobl2.dat', status='unknown')

	H =  TD/NS

	PRINT *, '  H =  ', H

	XP = 0
	HH = H/2

	PRINT *

	LI = 0
	PRINT *, ' LINEA     T       Y(1),       Y(2), .....'

	WRITE(*,98) LI, XP, (Y(I),I=1,IM)

28		LI = LI + 1
	DO N = 1, NS
		XB = XP
		XP = XP + H
		XM = XB + HH

		if (XP .le. 1) then !Con este if diferenciamos la fuerza que actua en el intervalo de tiempo

			J =  1
			DO I = 1, IM
				YA(I) = Y(I)
			END DO
			XA = XB
			CALL FUNCT1(EK,J,YA,H)
		
			J = 2
			DO I = 1, IM
				YA(I) = Y(I) + EK(1,I)/2
			END DO
			XA = XM
			CALL FUNCT1(EK,J,YA,H)

			J = 3
			DO I = 1, IM
				YA(I) = Y(I) + EK(2,I)/2
			END DO
			XA = XM
			CALL FUNCT1(EK,J,YA,H)

			J = 4
			DO I = 1, IM
				YA(I) = Y(I) + EK(3,I)
			END DO
			XA = XP
			CALL FUNCT1(EK,J,YA,H)

			DO I = 1, IM
				Y(I) = Y(I) + (EK(1,I) + EK(2,I)*2 + EK(3,I)*2 + EK(4,I))/6
			END DO


		else			
		
			J =  1
			DO I = 1, IM
				YA(I) = Y(I)
			END DO
			XA = XB
			CALL FUNCT2(EK,J,YA,H)
		
			J = 2
			DO I = 1, IM
				YA(I) = Y(I) + EK(1,I)/2
			END DO
			XA = XM
			CALL FUNCT2(EK,J,YA,H)

			J = 3
			DO I = 1, IM
				YA(I) = Y(I) + EK(2,I)/2
			END DO
			XA = XM
			CALL FUNCT2(EK,J,YA,H)

			J = 4
			DO I = 1, IM
				YA(I) = Y(I) + EK(3,I)
			END DO
			XA = XP
			CALL FUNCT2(EK,J,YA,H)

			DO I = 1, IM
				Y(I) = Y(I) + (EK(1,I) + EK(2,I)*2 + EK(3,I)*2 + EK(4,I))/6
			END DO

		end if

	end do	
	

	write (1,*) LI,XP,(Y(I), I=1, IM)
	WRITE(*,98) LI,XP,(Y(I),I=1,IM)
98	FORMAT(1X,I2,F10.6,2X,1P4E16.6/(15X,1P4E16.6))
	IF (XP .LT. XL) GOTO 28



	close(1)
200	PRINT *
	PRINT *, 'TECLEA 1 PARA CONTINUAR O 0 PARA TERMINAR'
	READ *, K
	IF (K .EQ. 1) GOTO 1
	PRINT *

	END PROGRAM

	SUBROUTINE FUNCT1(EK,J,YA,H)
	DIMENSION EK(0:4,0:10), YA(0:10)

	EK(J,1) =  YA(2)*H
	EK(J,2) = (-.8*YA(2)-0.64*YA(1)+0.2)*H
	RETURN
	END


	SUBROUTINE FUNCT2(EK,J,YA,H)
	DIMENSION EK(0:4,0:10), YA(0:10)

	EK(J,1) =  YA(2)*H
	EK(J,2) = (-.8*YA(2)-0.64*YA(1))*H
	RETURN
	END










