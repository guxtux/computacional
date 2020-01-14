! Programa para un cuerpo callendo amarrado a un resorte.
module constants
integer, parameter :: np=2000, dbl=selected_real_kind(14,100)
real(dbl) :: g=9.807,dtmin=.001, kspg=10., mass = 100.0
end module constants
!    Se escribe un modulo aparte para las constantes:
!    np - Numero de elementos para los arreglos de solucion.
!    dbl - Tipo de variables reales, el primer número es la precisión desimal y el segundo es el rango para el exponente.
!    g  -  Gravedad
!    dtmin -  Intervlo de timpo mínimo
!    kspg  -  Constante del resorte.
!    mass -  Masa del cuerpo
      
program fall
use constants
implicit none

!   Arreglos:
!     v   -  Velocidad
!     z   -   Altura
!     t   -   Tiempo
!     zreal - Altura para t(i) para comparar
!     Se usan arreglos "allocatables", eso quiere decir que se dimensionan durante la ejecución del programa.

real(dbl), allocatable :: v(:),z(:),t(:), zreal(:)
real(dbl) dt
integer nsteps

allocate (v(np),z(np),t(np),zreal(np))
call input(z,dt)
call odesolve(v,z,t,dt,nsteps)
call realans(t,z,nsteps,zreal)
call output (t,z,zreal,v,nsteps)
stop
end !!! progam?? end program fall?


!Subrutina para ingresar datos
subroutine input (z,dt)
use constants
implicit none

!   Se pide al usuario la altura inicial y  el intervalo para cada paso de tiempo.
!  Asigna:
!     z(1)   -  Altura inicial
!     dt     -  Paso de tiempo

real(dbl) z(*),dt

write(6,'(a)',advance='no') ' Altura inicial (metros): '
read *, z(1)
write(6,'(a)',advance='no') 'Paso de tiempo (Segundos): '
read *, dt
if(dt.le.0.) dt=dtmin
return
end


!Subrutina para manejar la ecuación
subroutine odesolve(v,z,t,dt,nsteps)
use constants
implicit none
!   Se soluciona la ecuación diferencial ordinaria del movimiento del cuerpo.
!   Lee:
!     dt     -   paso de tiempo
!   Asigna:
!     v    -   velocidad
!     z    -   altura
!     t    -   tiempo
!     nsteps - # de pasos.

real(dbl) v(*),z(*),t(*),dt, c0, c1
integer i,nsteps

!   La ecuación en cuestión se separa para formar el siguiente sistema:
!
!     d v              k                      d z
!     ---    =  - g + --- ( z0 - z ) ,         ---   =  v
!     d t              m                      d t
!   Se asignan las condiciones iniciales:

t(1)=0.
v(1)=0.

!   Se asignan las constantes

      c1=dt*kspg/mass
      c0= c1*z(1)-g*dt

!   El ciclo se mantiene hasta que z es negativo o se termina el espacio


      do 100 i=2,np
         v(i)= v(i-1)+c0-c1*z(i-1)
         z(i)= z(i-1)+dt*.5*(v(i)+v(i-1))
         t(i)=t(i-1)+dt
         if(z(i).lt.0.) go to 200
 100     continue
      write(6,*) 'Se acabó el espacio para la integración'
      write(6,*) ' La ultima altura: ',z(np),' metros'
      i=np
 200  nsteps=i
      end

!Subrutina que compara con la solución analitica:
subroutine realans(t,z,nsteps,zreal)
use constants
Implicit none
real(dbl) t(*),z(*),zreal(*),c1,c2
integer i,nsteps
 c1=g*mass/kspg
 c2=sqrt(kspg/mass)
do 10 i=1,nsteps
	10  zreal(i)=c1*cos(c2*t(i)) + z(1)-c1
      return
      end

!Subrutina que imprime los resultados
subroutine output(t,z,zreal,v,nsteps)
use constants, only : dbl
implicit none

!c   Outputs the full results of the time integration
real(dbl) v(*),z(*),t(*), zreal(*)
integer nsteps,i
print *, 'Los resultados están en fall.output'
open (11,file='fall.output')
write(11,2000)
do 300 i=1,nsteps
write(11,2001) t(i),z(i),zreal(i),((z(i)-zreal(i))/zreal(i))*100
300  continue
 2000 format (18x,'S.Numerica',8x,'S.Analitica',/,6x,'Tiempo(s)',6x,'Altura(m)',6x,'Altura(m)',6x,'Error(%)')
 2001 format (1x,1p,4e15.7)
      return
      end

