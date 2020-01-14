       program edolinealf
        dimension A(20),B(20),C(20),D(20)
       print*
         print*,'problema de edo lineal con valores en la frontera'
        !N= nùmero de puntos en la retìcula
         N=10
         open(unit=20,file='cable.txt',status='unknown')
         do  i=1,N
       x=i
           !coeficientes tridiagonales
        A(i)=-1.
          B(i)=2.
           C(i)=-1.
             !tèrmino fuente (no homegeneo)
         D(i)=20*(1+exp(x/25.)) /5000.
        !140 continue
        enddo
           !ajuste con la condiciòn en la frontera
          D(1)=D(1)
          D(N)=D(N)
          B(N)=0.
          call TRDG(A,B,C,D,N)
         !definiciòn de D(0)
         !D(0)=1
         print*,'punto de la reticula soluciòn'
          print 171, 0, 0.
          write(20,171) 0, 0.
        do  i=1,N
           !Impresion de la soluciòn
         print 171, i, D(i)
         write(20,171) i,D(i)
         end do
171     format (2X, I5,7X,F15.6)
         print*
         stop
        close(20)
          end

          subroutine TRDG(A,B,C,D,N)
          !subrutina tridiagonal
          Dimension A(1),B(1),C(1),D(1)
          do  i=2,N
           R=A(i)/B(i-1)
          B(i)=B(i)-R*C(i-1)
          D(i)=D(i)-R*D(i-1)
         enddo
          D(N)=D(N)/B(N)
         do  i=N-1,1,-1
         D(i)=(D(i)-C(i)*D(i+1))/B(i)
         enddo
        return
         end
