		program exaedo9
	dimension t(0:100000),y(0:100000),z(0:100000)
	   n=13000
	   h=0.001
	 open(1,file="exaedo9.dat",status="replace")
	 open (2,file="exaedo9b.dat",status="replace")
	y(0)=150.0
	z(0)=150.0
	     a1=1.0/2.0
	     a4=2.0
	     a5=1.0/6.0
	     b1=3.0
	     b2=3.0/8.0
	     yinte=0.0
	     zinte=0.0
	do i=0,n
	t(i)=h*i
	 w1=h*f1(y(i),z(i),t(i))
	 x1=h*f2(y(i),z(i),t(i))
	 w2=h*f1(y(i)+a1*w1,z(i)+a1*x1,t(i)+h*a1)
	 x2=h*f2(y(i)+a1*w1,z(i)+a1*x1,t(i)+h*a1)
	 w3=h*f1(y(i)-w1+a4*w2,z(i)-x1+a4*x2,t(i)+h)
	 x3=h*f2(y(i)-w1+a4*w2,z(i)-x1+a4*x2,t(i)+h)

	y(i+1)=y(i)+a5*(w1+4.0*w2+w3)
	z(i+1)=z(i)+a5*(x1+4.0*x2+x3)
	write(1,*)t(i),y(i),z(i)
	end do 
  
	do i=0,n-3,3
	yinte=yinte+(y(i)+b1*y(i+1)+b1*y(i+2)+y(i+3))*(b2*h)
	zinte=zinte+(z(i)+b1*z(i+1)+b1*z(i+2)+z(i+3))*(b2*h)
	if ( zinte>=0.0) then 
	write(2,*)t(i),yinte,zinte 
	end if 
	end do
	end program
	function f1(y,z,t)
! 	c=a2
	     a2=0.005
	     f1=-a2*sqrt(y**2+z**2)*y
	end function f1
	function f2(y,z,t)
	     a2=0.005
	     pi=2.0*asin(1.0)
!	g=a3
	     a3=pi**2
	     f2=-a3-a2*sqrt(y**2+z**2)*z
	end function f2
