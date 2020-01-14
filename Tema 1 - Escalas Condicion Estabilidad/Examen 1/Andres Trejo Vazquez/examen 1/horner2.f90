!evaluacion de un polinomio mediante la regla de horner 
program horner
!declarando las variables
integer :: k,l
real :: dx, p, cotainf, cotasup, w

!se declara el intervalo en el que va a estar evaluada x 
cotainf=-1
cotasup=-4
!l sera el numero de intervalos que existen
l=6
!se declara el tamaño del paso dx, que va de 0.5 en 0.5
dx=(cotainf-cotasup)/float(l)  


OPEN (UNIT=6, FILE= 'horner2.dat', STATUS='replace')

!se abre un ciclo do para evaluar el polinomio
DO k=0,l
w=cotasup + float(k)*dx
p = (((2.0*w -20.0)*w +70.0)*w + 100.0)*w + 48.0
WRITE (6,100) w, P
100 FORMAT (F14.1,2X,F14.3)
END DO
	CLOSE (6)
END PROGRAM horner


