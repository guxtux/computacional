	program examedo1a
!	implicit double precision (a-h,o-z)
	dimension t(0:10000),y(0:10000)
	dimension g(0:10000),fx(0:10000)
	   n=500
	   h=0.01
	 open(1,file="exaedo1a.dat",status="replace")
	     y(0)=1.0
	xinte1=0.0
	do i=0,n
	t(i)=i*h
	 fx(i)=exp((t(i)**2)/2.0)
	xinte1=xinte1+h*fx(i)
	g(i)=exp(-(t(i)**2)/2.0)*(xinte1-1.0)
	     y(i+1)=y(i)+h*f(y(i),t(i))
	error=abs(g(i)-y(i))
	write(1,*)t(i),y(i),error
	end do  
	end program  
	function f(y,t)
!	implicit double precision (a-h,o-z)
	     f=-t*y+1.0
	end function f
