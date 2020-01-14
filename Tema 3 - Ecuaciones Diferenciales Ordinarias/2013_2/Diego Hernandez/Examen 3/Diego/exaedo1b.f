	program examedo1b
!	implicit double precision (a-h,o-z)
	dimension t(0:10000),y(0:10000),g(0:10000)
	   n=500
	   h=0.01
	 open(1,file="exaedo1b.dat",status="replace")
	     y(0)=1.0
	do i=0,n
	t(i)=i*h
	     g(i)=0.5*(exp(-t(i))+exp(-3*t(i)))
	     y(i+1)=y(i)+h*f(y(i),t(i))
	error=abs(g(i)-y(i))
	write(1,*)t(i),y(i),error
	end do  
	end program  
	function f(y,t)
!	implicit double precision (a-h,o-z)
	     f=exp(-t)-3.0*y
	end function f
