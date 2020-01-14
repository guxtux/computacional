	program examenedo3
	dimension t(0:100000),y(0:1000000),z(0:1000000)
	   n=10000
	   h=0.001
	  pi=2.0*asin(1.0)
	     a1=2.0*(pi**2)
	 open(1,file="examenedo3.dat",status="replace")
	y(0)=0.001
	z(0)=0.0
	do i=0,n
	t(i)=i*h
	y(i+1)=y(i)+h*f1(y(i),z(i),t(i))
	z(i+1)=z(i)+h*f2(y(i),z(i),t(i))
	write(1,*)t(i),y(i),z(i)
	end do
	print*,"empezando en cero"
	print*,"el maximo se alcanza cada 1.41seg"
	print*,"si empezamos en o.7"
	print*,"el minimo se alcanza cada 1,41seg"
	end program
	function f1(y,z,t)
	f1=z
	end function f1
	function f2(y,z,t)
!	g=pi**2
	  pi=2.0*asin(1.0)
	     a1=2.0*(pi**2)
	     f2=-a1*y
	end function f2
