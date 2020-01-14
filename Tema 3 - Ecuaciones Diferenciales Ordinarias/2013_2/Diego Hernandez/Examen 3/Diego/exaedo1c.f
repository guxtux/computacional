	program exaedo1c
!	implicit double precision (a-h,o-z)
	dimension t(0:10000),y(0:10000),g(0:10000)
	   n=500
	   h=0.01
	 open(1,file="exaedo1c.dat",status="replace")
	     y(0)=0.5
	do i=0,n
	t(i)=i*h
	g(i)=t(i)**2-2.0*t(i)-(3.0/2.0)*exp(-t(i))+2.0
	     y(i+1)=y(i)+h*f(y(i),t(i))
	error=abs(g(i)-y(i))
	write(1,*)t(i),y(i),error
	end do  
	end program  
	function f(y,t)
!	implicit double precision (a-h,o-z)
	     f=t**2-y
	end function f
