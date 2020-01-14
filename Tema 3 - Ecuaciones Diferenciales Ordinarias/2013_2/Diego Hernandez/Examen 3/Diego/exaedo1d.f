	program examedo1d
!	implicit double precision (a-h,o-z)
	dimension t(0:10000),y(0:10000),g(0:10000)
	   n=500
	   h=0.01
	 open(1,file="exaedo1d.dat",status="replace")
	 open(2,file="exaedo1d2.dat",status="replace") 
	 open(3,file="exaedo1d3.dat",status="replace")
	     y(0)=1.0
	do i=0,n
	t(i)=i*h
	     g(i)=1.0/(1.0+t(i))
	     y(i+1)=y(i)+h*f(y(i),t(i))
	error=abs(g(i)-y(i))
	write(1,*)t(i),y(i),error
	end do  
	do i=0,n
	t(i)=i*h
	g(i)=1.0/(1.0-t(i))
	     y(i+1)=y(i)+h*f1(y(i))
	error=abs(g(i)-y(i))
	write(2,*)t(i),y(i),g(i),error
	if (y(i)<99.0) then
	write(3,*)t(i),y(i),g(i),error
	end if
	end do 
	end program  
	function f(y,t)
!	implicit double precision (a-h,o-z)
	     f=-y**2
	end function f
	function f1(y)
!	implicit double precision (a-h,o-z)
	     f1=y**2
	end function f1
