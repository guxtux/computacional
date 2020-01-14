 PROGRAM exatreseje1a

   INTEGER::i,j
   REAL:: A11,A12,A21,A22,Z1,Z2,aa,bb,d,gx,ri
   DIMENSION A(10,4)

   OPEN (19,FILE='exatreseje1ai.dat' , STATUS='UNKNOWN')

	DATA N /6/

	DATA (A(1,J), J=1,2) /0.1, 0.61 /
	DATA (A(2,J), J=1,2) /0.4, 0.92 /
	DATA (A(3,J), J=1,2) /0.5, 0.99 /
	DATA (A(4,J), J=1,2) /0.7, 1.52 /
	DATA (A(5,J), J=1,2) /0.9, 1.47 /
	DATA (A(6,J), J=1,2) /1.1, 2.03 /
 
  L=6
  A11=L

     A12=0
          DO i=1,6
              A12=A12+A(i,1)
          END DO
          A21=A12
           
     Z1=0
          DO i=1,6
              Z1=Z1+A(i,2)
          END DO

     A22=0
          DO i=1,6
              A22=A22+( A(i,1)*A(i,1) )
          END DO

      Z2=0
          DO i=1,6
              Z2=Z2+( A(i,1)*A(i,2) )
          END DO

     d=(   (A11*A22) -(A12*A21)  )
    aa=(   ( (A22*Z1)-(A12*Z2)   ) / (d)  )
    bb=(   ( (A11*Z2)-(A21*Z1)-1 ) / (d)  )
     
        DO i=1,6

            gx=aa+bb*A(i,1)

            ri=A(i,2)-gx              

            PRINT*,A(i,1),gx,ri

      WRITE (19,*),A(i,1),A(i,2),gx,ri,0.0

        END DO

 END PROGRAM exatreseje1a
