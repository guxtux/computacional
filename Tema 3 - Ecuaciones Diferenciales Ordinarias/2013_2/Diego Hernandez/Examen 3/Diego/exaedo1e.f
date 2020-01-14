	program examedo1e
!	implicit double precision (a-h,o-z)
	dimension t(0:10000),y(0:10000)
	   n=500
	   h=0.01
	 open(1,file="exaedo1e.dat",status="replace")
	     y(0)=1.0
	do i=0,n
	t(i)=i*h
	     y(i+1)=y(i)+h*f(y(i),t(i))
	write(1,*)t(i),y(i)
	end do  
	end program  
	function f(y,t)
!	implicit double precision (a-h,o-z)
	     f=sin(t)-sqrt(abs(y))
	end function f
