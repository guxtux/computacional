program serie

integer:: t,n, i, fact
real:: j,S, y,S2,S3
PRINT*, 'Numeros de terminos'
read*, n

print*, 'dame el valor a evaluar'

read*, y
!Nose como poner la sumatoria, si tomar el inverso de la expresion e^x, o buscar la sumatoria en serie de taylor para esta expresion 

OPEN (UNIT=6, FILE='ERROR.dat', STATUS='REPLACE')


!SUMATORIA 1
!S2=1.0
!DO k=1,n
!S2=S2 + ((y**n)/fact(n))
!S3= 1./S2
!END DO 


DO k=2,n
S2=fact(n)/(y**n)
S=1/s2
S3= 1./1.- 1./y + S
end do 
 



!s1= (abs(0.9048374-S3)/0.9048374)*100 


PRINT*,'el valor de S es ',S3 ,'con error relativo',error_rel_s1 ,'%'
end program serie

FUNCTION fact(x)
IMPLICIT NONE
INTEGER , INTENT(IN) :: x
INTEGER :: fact, i
fact=1
DO i= 1,x
fact=fact*i
END DO 
END FUNCTION fact


