      PROGRAM eliminagauss

        DIMENSION A(10,11),X(10),Y(10),XX(10)
        open(1, file="APROX2A.dat", status="unknown")
        PRINT*
        PRINT*,'METODO DE ELIMINACIONDE GAUSS'
        DATA N /4/
        DATA (XX(i), i=1,6) /0.1,0.4,0.5,0.7,0.9,0.9/
        DATA (Y(i), i=1,6) /0.61,0.92,0.99,1.52,1.47,2.03/

                L=6
        
        A(1,1)= 6.


        A(1,2)=0.0
        A(1,3)= 0.0
        A(1,4)=0.0
        A(1,5)=0.0

        A(2,1)=0.0 
        A(2,2)= 0.0
        A(2,3)= 0.0
        A(2,4)=0.0
        A(2,5)=0.0

        A(3,1)=0.0 
        A(3,2)= 0.0
        A(3,3)= 0.0
        a(3,4)= 0.0
        A(3,5)=0.0
       
        A(4,1)=0.0 
        A(4,2)= 0.0
        A(4,3)= 0.0
        a(4,4)= 0.0
        A(4,5)=0.0

        do i=1,6

       a(1,2)= a(1,2)+xX(i)
       a(1,3)= a(1,3)+sin(xX(i))
       a(1,4)= a(1,4)+ exp(xX(i))

        A(1,5)= A(1,5) + Y(i)
        A(2,5)= A(2,5)+XX(i)*Y(i)
        A(3,5)= A(3,5)+Y(i)*sin(xX(i))
        A(4,5)= A(4,5)+Y(i)*exp(xX(i))
       a(2,1)= a(2,1) + xX(i)
       a(2,2)= a(2,2)+  xX(i)*xX(i)
       a(2,3)= a(2,3)+  xX(i)*sin(xX(i))
       a(2,4)= a(2,4)+  xX(i)*exp(xX(i))
       a(3,1)= a(3,1) + sin(xX(i))
       a(3,2)= a(3,2)+  xX(i)*sin(xX(i))
       a(3,3)= a(3,3)+  sin(xx(i))*sin(xX(i))
       a(3,4)= a(3,4)+  sin(xX(i))*exp(xX(i))
       a(4,1)= a(4,1) + exp(xX(i))
       a(4,2)= a(4,2)+  xX(i)*exp(xX(i))
       a(4,3)= a(4,3)+  sin(xX(i))*exp(xX(i))
       a(4,4)= a(4,4)+  exp(xX(i))*exp(xX(i))
       end do

        PRINT*
        PRINT*,'MATRIZ AUMENTADA'
        PRINT*

        DO I=1,N

        PRINT 61,(A(I,J),J=1,5)
61      FORMAT(1X,1P6E12.4)
        END DO
        PRINT*

                 CALL GAUSS(N,A)

        PRINT*
        PRINT*, '    SOLUCION      '
        PRINT*, '--------------------------------'
        PRINT*, '      I       X(I)      '
        PRINT*, '--------------------------------'
        DO I= 1,6
        write(1,*) XX(I), Y(I),(-0.005433 +0.03729*XX(I)+0.9845*sin(xX(i)) +.3878*exp(xX(i)))
        END DO
        CLOSE(1)
        DO I= 1,N
        
72      FORMAT(5X, I5, 1PE16.6)
        PRINT 72, I,A(I,N+1)
        END DO

        PRINT*,'-----------------------------------------'
        PRINT*
        STOP
        END PROGRAM

        !+++++++++++++++++++++++++++++++++++++++++

        SUBRoUTINE GAUSS(N,A)
        INTEGER PV
        DIMENSION A(10,11)

        EPS=1.0
10      IF(1.0 + EPS .GT. 1.0 ) THEN
        EPS=EPS/2.0
        GOTO 10
        END IF

        EPS=EPS*2
        PRINT*,  '   epsilon de la maquina=   ', eps

        EPS2= EPS*2

        DET=1.0

        DO 1010 I=1,N-1

        PV=1
        DO J=I+1,N
        IF(ABS(A(PV,I)) .LT. ABS(A(J,I))) PV=J

        END DO

        IF(PV .EQ.I) GOTO 1050

        DO JC= 1, N+1
           TM =A(I,JC)
           A(I,JC)=A(PV,JC)
           A(PV,JC)=TM

           END DO

1045   DET=-1*DET
1050   IF(A(I,I) .EQ. 0) GOTO 1200

       DO JR= I+1,N
       IF(A(JR,I) .NE. 0) THEN
         R=A(JR,I)/A(I,I)
         DO KC= I+1,N+1
         TEMP= A(JR,KC)
         A(JR,KC)= A(JR,KC)-R*A(I,KC)
         IF (ABS(A(JR,KC)) .LT. EPS2*TEMP) A(JR,KC)=0.0
         end do
         end if
         end do
1010     CONTINUE

         DO I= 1,N
         DET=DET*A(I,I)
         END DO

         PRINT*
         PRINT*, ' DETERMINANTE=',  DET
         PRINT*

         IF(A(N,N) .EQ. 0) GOTO 1200
         A(N,N+1)= A(N,N+1)/A(N,N)

         DO NV= N-1,1,-1
         VA=A(NV,N+1)
         DO K=NV+1,N
         VA=VA-A(NV,K)*A(K,N+1)
         END DO
         A(NV,N+1)=VA/A(NV,NV)
         END DO
         RETURN

 1200    PRINT*,'LA MATRIZ ES SINGULAR'
         END 


        
