	program exaedo6
	dimension t(0:100000),y(0:1000000),z(0:1000000)
	   n=500
	   h=0.1
	     a1=1.0/2.0
	 open(1,file="exaedo6.dat",status="replace")
	 open(2,file="exaedo6b.dat",status="replace")
	y(0)=10.0e5
	z(0)=0.0
	do i=0,n
	t(i)=i*h
	y(i+1)=y(i)+h*f1(y(i),z(i),t(i))
	z(i+1)=z(i)+h*f2(y(i),z(i),t(i))
	w1=f1(y(i),z(i),t(i))+f1(y(i+1),z(i+1),t(i+1))
	y(i+1)=y(i)+h*a1*w1
	w2=f2(y(i),z(i),t(i))+f2(y(i+1),z(i+1),t(i+1))
        z(i+1)=z(i)+h*a1*w2
	write(1,*)t(i),y(i),z(i)
	end do 
	do i=0,n,20
	write(2,*)t(i),y(i),z(i)
	end do 
	end program
	function f1(y,z,t)
!	a1=const de decaimiento del yodo
	     a1=0.1044
	 f1=-a1*y
	end function f1
	function f2(y,z,t)
!       a2=const de decaimiente del xenon
	     a2=0.0753
	     f2=-a2*z+a1*y
	end function f2
