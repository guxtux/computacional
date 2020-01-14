        PROGRAM  problema_1a

        real :: t, x, y, k1, k2, l1, l2

        data t, x, y, c, u, v , h/ 0.0, 0.0, 0.0, 0.005, 150, 150, 0.1/

        print *, '     t        u           v         x          y'

        open(1, file="datprobl_1a.dat", status="unknown")  !creamos el archivo datprobl para guardar datos
        !posteriormente usando la sentencia write(1,*) dentro del ciclo Do



	DO n=1,200

        !M+etodo de Runge Kuta 2
		t = t+h
		v1=sqrt(u**2+v**2)
		
		k1 = -c*v1*u*h
		l1 = (-9.81-c*v1*v)*h
		
		v2=sqrt((u+k1)**2+(v+l1)**2)
		
		k2 = -c*v2*(u+k1)*h
		l2 = (-9.81-c*v2*(v+l1))*h
		
		UU=u+(k1+k2)/2
		VV=v+(l1+l2)/2


!Calculamos la trayectoria del proyectil:

		x= x+ 0.5*(u+UU)*h
		
		y= y+ 0.5*(v+VV)*h

		u=UU
		v=VV

         	write(1,*)t,x,y
		
        	print*,t,UU,VV,x,y

         if(y .LT. 0) stop


       END DO

       close(1)

       END PROGRAM problema_1a
