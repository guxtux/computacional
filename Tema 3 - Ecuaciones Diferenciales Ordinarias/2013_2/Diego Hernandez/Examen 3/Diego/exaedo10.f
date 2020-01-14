	program exaedo10
	dimension t(0:10000),y(0:10000),z(0:10000)
	   h=0.01
	   n=1000
	 open(1,file="exaedo10.dat",status="replace")
	y(0)=0.0
	z(0)=1.0
             a4=1.0/2.0
             a5=1.0/6.0
	     m=5.0
	     f0=1.0
!	f=1.0/5.0
	  do i=0,n
	  t(i)=i*h
	if (t(i)<1.0) then 
	     f=f0/m
	 else if(t(i)>1.0) then 
	     f=0.0
	end if 
	 w1=h*f1(y(i),z(i),t(i))
	 x1=h*(f2(y(i),z(i),t(i))+f)
	 w2=h*f1(y(i)+w1*a4,z(i)+x1*a4,t(i)+h*a4)
	 x2=h*(f2(y(i)+w1*a4,z(i)+x1*a4,t(i)+h*a4)+f)
	 w3=h*f1(y(i)+w2*a4,z(i)+x2*a4,t(i)+h*a4)
	 x3=h*(f2(y(i)+w2*a4,z(i)+x2*a4,t(i)+h*a4)+f)
	 w4=h*f1(y(i)+w3,z(i)+x3,t(i)+h)
	 x4=h*(f2(y(i)+w3,z(i)+x3,t(i)+h)+f)
	  y(i+1)=y(i)+a5*(w1+a4*w2+a4*w3+w4)
	  z(i+1)=z(i)+a5*(x1+a4*x2+a4*x3+x4)
!	print*,t(i),f
	write(1,*)t(i),y(i),z(i),f
	end do 
!	end do 
	end program
	function f1(y,z,t)
	     f1=z
	end function f1
	function f2(y,z,t)
!	ca=const de amortiguamiento
	     ca=3.2
!	m=masa
	     m=5.0
           b2=ca/m
!	b3=frecuencia natural
           b3=b2**2
!	b4=factor de amortiguamiento
	     b4=0.5
           b5=b2*2.0*b4
	     f2=-b3*y-b5*z
	end function f2
