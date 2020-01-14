        PROGRAM  problema_1b

        real :: t, x, y, k1, k2, l1, l2

        data t, x, y, c, u, v , h/ 0.0, 0.0, 0.0, 0.005, 150, 150, 0.1/

        print *, '     t        u           v         x          y'

        open(1, file="datprobl_1b.dat", status="unknown")



	DO n=1,200
		
		t = t+h
		v1=sqrt(u**2+v**2)

!Metodo de RK3
		k1 = -c*v1*u*h
		l1 = (-9.81-c*v1*v)*h

		v2=sqrt((u+(0.5)*k1)**2+(v+(0.5)*l1)**2)

		k2 = -c*v2*(u+k1)*(3./2)*h
		l2 =(-9.81-c*v2*(v+l1))*(3./2)*h

		v3=sqrt((u-k1+2*k2)**2+(v-l1+2*l2)**2)

		k3=-c*v3*(u-k1+2*k2)*2*h
		l3 = (-9.81-c*v3*(v-l1+2*l2))*2*h

		UU=u+(1./6)*(k1+4*k2+k3)
		VV=v+(1./6)*(l1+4*l2+l3)

!Calculamos la trayectoria

		x= x+ 0.5*(u+UU)*h
		y= y+ 0.5*(v+VV)*h

	        u=UU
		v=VV



		print*, t, x, y, UU, VV

	        write(1,*)t,x,y
	        
           if(y .LT. 0) stop

        END DO
	
	close(1)

       END PROGRAM problema_1b

