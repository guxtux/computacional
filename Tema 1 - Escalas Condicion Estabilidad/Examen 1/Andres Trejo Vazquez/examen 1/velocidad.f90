program velocidadterminal
integer i,n
real:: g, m, a,d, dt
real:: z, y, vz, vy, v, az, ay, k 
real, parameter:: pi = 3.1416   

print *, 'Dame n'
read*, n 

print *, 'Dame altura inicial'
read*, y

print *, 'Dame el area'
read*, a


! asignando los valores a las constantes
     d= 1000  !kg/m³
     g = 9.80 !m/s²
     vterm=sqrt(g/k)
     m = 1
!Aqui declaramos la dt, puesto que queremos ver la caida para cierto tiempo pequeño, suponemos que  como no hay componente vx  la velocidad, la caida del cuerpo solo la tiene vy 
     dt= (vterm)/(g*n) 
     k = (a*d)/(2.*m)
       


! n*dt=tmax, n: pasos en dt 

!Variables estan de la siguiente forma:
!C=1 coeficiente de arrastre del objeto-aire kg/m^3
!Vo velocidad inicial m/s²
!angulo	Angulo en radianes con respecto la horizontal
!masa	Masa del conjunto en kg
!dt incremento de tiempo en segundos
!tiempo maximo hasta el cual calcular la posicion, en segundos
 
!asignando valores al punto inicial 
   	 y=0.0
    	 vy  = 0.0
	 ay = g
          v=vy
open (unit=6, file= 'gota.dat', status='replace')

 ! Calcula la posicion,velocidad y aceleracion recursivamente
      do i= 1,n

      y = y-((vterm**2)/g)*log(cosh(g*dt/vterm))
      vy= vy - vterm*(tanh(dt*g/vterm))
      ay = -(k*vterm*vy)-g
	!t = (vy/g)
      
write (6,100) i, y 
100 format (I10.5,2X,F15.5)
end do

!solo para renombrar a las velocidad, posiciones y aceleraciones, para la caida de la gota sin resistencia, se  

z = 0.0
vz  = 0.0
az = g

 dt= (vz)/(g*n) 
! calculo trayectoria en caida libre 
open (unit=9, file= 'libregota.dat', status='replace')
	do j= 1,n 

      z = z+(dt*vz)-(0.5*(az*(dt)**2.))
      vz= vz - (dt*az)


write (9,200) dt, z  
200 format (F10.5,2X,F15.5)

!print*, x,y 

	end do

 close (6)
 close (9)
end program  velocidadterminal
