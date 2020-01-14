	PROGRAM RK4_SISTEMA
	DIMENSION YA(0:10), YN(0:10), EK(0:4), Y(0:10),Ka(5)
	DIMENSION Le(5),YK(5),YL(5)
        integer s
        real w
	PRINT *
	PRINT *, '      ESQUEMA DE RK4 PARA UN CONJUNTO DE ECUACIONES'
	PRINT *

        
       print*,'Solving y´´+2Cwy´+w**2y=0'

!se definen las condiciones iniciales
	IM = 2

	Y(1) = 0.3
	Y(2) = 0.1
               open(unit=20,file='rk4f.txt',status='unknown')

1        PRINT *
	PRINT *, '¿INTERVALO DE IMPRESIÓN DE T?'
	READ *, TD

	PRINT *, '¿NUMERO DE PASOS EN UN INTERVALO DE IMPRESIÓN DE T?'
	READ *, NS

	PRINT *, '¿T MAXIMO PARA DETENER LOS CALCULOS?'
	READ *, XL


!tamaño de la retícula
	H =  XL/NS

	PRINT *, '  H =  ', H
!xp=tiempo, es inicializar variables
	XP = 0
	HH = H/2

	PRINT *
!inicializa numero de linea
	LI = 0

	PRINT *, ' LINEA     T       Y(1),       Y(2), .....'
        
!intervalo de integracion
	DO N = 1, NS
!se redefine el tiempo	
		XB = XP
		XP = XP + H
		XM = XB + HH
		LI = LI + 1
		J =  1

		DO I = 1, IM
                     
			YA(I) = Y(I)

		END DO
                     
       k=3.2
        M=5
       F=0
       C=0.5
       w=(3.2/5)**2
       f0 =1


       If (XB .LT. 1 .or. XB .EQ. 1) then
	EK(1) =  YA(2)
	EK(2) = -2*C*w*YA(2)-(w**2)*YA(1)+2*f0*XB

               YK(1) = EK(1)*H
                YL(1)=EK(2)*H


		J = 2
		
		YK(2) = H*(EK(1)+YL(1)/2)
       EK(2)=-2*C*w*(YA(2)+YL(1)/2)-(w**2)*(YA(1)+YK(1)/2)+2*f0*(XB+H/2)
                YL(2) = H*(EK(2))


		J = 3
		YK(3) = H*(EK(1)+YL(2)/2)
	EK(2)=-2*C*w*(YA(2)+YL(2)/2)-(w**2)*(YA(1)+YK(2)/2)+2*f0*(XB+H/2)
		YL(3)=H*(EK(2))
		XA = XM
	
		J = 4
	YK(4) = H*(EK(1)+YL(3))
	EK(2)=-2*C*w*(YA(2)+YL(3))-(w**2)*(YA(1)+YK(3)/2)+2*f0*(XB+H)
		YL(4)=H*EK(2)
		

		
	Y(1) = Y(1) + (YK(1) + YK(2)*2 + YK(3)*2 + YK(4))/6
                Y(2) = Y(2) + (YL(1) + YL(2)*2 + YL(3)*2 + YL(4))/6
	WRITE(*,98) LI,XB,Y(1),Y(2)
	write(20,98) LI,XP,Y(1),Y(2)
98	FORMAT(1X,I2,F10.6,2X,1P4E16.6/(15X,1P4E16.6))
         endif
              If (XB .GT. 1 .and. XB .LT. 2) then
	EK(1) =  YA(2)
	EK(2) = -2*C*w*YA(2)-(w**2)*YA(1)+2*f0*(1-XB)

               YK(1) = EK(1)*H
                YL(1)=EK(2)*H


		J = 2

		YK(2) = H*(EK(1)+YL(1)/2)
      EK(2)=-2*C*w*(YA(2)+YL(1)/2)-(w**2)*(YA(1)+YK(1)/2)+2*(1-XB-H/2)
                YL(2) = H*(EK(2))


		J = 3
		YK(3) = H*(EK(1)+YL(2)/2)
	EK(2)=-2*C*w*(YA(2)+YL(2)/2)-(w**2)*(YA(1)+YK(2)/2)+2*(1-XB-H/2)
		YL(3)=H*(EK(2))
		XA = XM

		J = 4
		YK(4) = H*(EK(1)+YL(3))
	EK(2)=-2*C*w*(YA(2)+YL(3))-(w**2)*(YA(1)+YK(3)/2)+2*f0*(1-XB-H)
		YL(4)=H*EK(2)



	Y(1) = Y(1) + (YK(1) + YK(2)*2 + YK(3)*2 + YK(4))/6
        Y(2) = Y(2) + (YL(1) + YL(2)*2 + YL(3)*2 + YL(4))/6
	WRITE(*,97) LI,XB,Y(1),Y(2)
	write(20,97) LI,XP,Y(1),Y(2)
97     FORMAT(1X,I2,F10.6,2X,1P4E16.6/(15X,1P4E16.6))
         endif
        If (XB .GT. 2) then
         EK(1) =  YA(2)
	EK(2) = -2*C*w*YA(2)-(w**2)*YA(1)

               YK(1) = EK(1)*H
                YL(1)=EK(2)*H


		J = 2

		YK(2) = H*(EK(1)+YL(1)/2)
                EK(2)=-2*C*w*(YA(2)+YL(1)/2)-(w**2)*(YA(1)+YK(1)/2)
                YL(2) = H*(EK(2))


		J = 3
		YK(3) = H*(EK(1)+YL(2)/2)
		EK(2)=-2*C*w*(YA(2)+YL(2)/2)-(w**2)*(YA(1)+YK(2)/2)
		YL(3)=H*(EK(2))
		XA = XM

		J = 4
		YK(4) = H*(EK(1)+YL(3))
		EK(2)=-2*C*w*(YA(2)+YL(3))-(w**2)*(YA(1)+YK(3)/2)
		YL(4)=H*EK(2)



	Y(1) = Y(1) + (YK(1) + YK(2)*2 + YK(3)*2 + YK(4))/6
        Y(2) = Y(2) + (YL(1) + YL(2)*2 + YL(3)*2 + YL(4))/6
	WRITE(*,96) LI,XB,Y(1),Y(2)
	write(20,96) LI,XP,Y(1),Y(2)
96	FORMAT(1X,I2,F10.6,2X,1P4E16.6/(15X,1P4E16.6))
         endif
         
		
	END DO

            close(20)
200	PRINT *
	PRINT *, 'TECLEA 1 PARA CONTINUAR O 0 PARA TERMINAR'
	READ *, z
	IF (z .EQ. 1) GOTO 1
	PRINT *
	END
!++++++++++++++++++++++++++++++++++++++++++++++
	

