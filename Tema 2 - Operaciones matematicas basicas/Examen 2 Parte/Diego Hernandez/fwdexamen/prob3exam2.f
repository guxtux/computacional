	program integracionproblema3
!	implicit double precision (a-h,o-z)
        dimension x(0:10000000),gx(0:10000000)
	dimension ene(0:10000),z(0:100000),y(0:100000) 
	dimension h(0:1000000),a(1000)
	  n=1000
	  m=10000
	  he=1.0/m
	 pi=2.0*asin(1.0)
	     a(1)=0.0
	     a(2)=1.0
	     a(3)=2.0
	 open(1,file="problema3.dat",status="replace")
	 open(2,file="problema3b.dat",status="replace")
	 open(3,file="problema3c.dat",status="replace")

	do k=1,3
	 b=pi*(a(k)+(1.0/2.0))
	   c1=150.0
	   c2=21.7
	do i=8000,m-1
	ene(i)=-i*he-.000000001
	  y(i)=((2.0-2.0*sqrt(1.0+ene(i)))/(-ene(i)))**(1.0/6.0)
	  z(i)=((2.0+2.0*sqrt(1.0+ene(i)))/(-ene(i)))**(1.0/6.0)
	     h(i)=(z(i)-y(i))/n
! 	xinte1=0.0
!	xinte2=0.0
!	xinte3=0.0
	xinte4=0.0
!	print*,ene(i),y(i),z(i),h(i)
        do j=1,n-1
        x(j)=y(i)+h(i)*j
	 gx(j)=sqrt((ene(i)-f(x(j))))
!	print*,x(j),gx(j),f(x(j))
!	print*,ene(i)-f(x(j)),gx(j),gx(j)*h(i)
!        xinte=0
!        do k=1,n                        
!        xinte1=xinte1+gx(j)*h(i)
!	print*,xinte
        end do
!	do j=1,n-1
!        xinte2=xinte2+(gx(j)+gx(j+1))*(h(i)/2.0)
!        end do
!	do j=1,n-1,2
!	xinte3=xinte3+(gx(j)+4*gx(j+1)+gx(j+2))*(h(i)/3.0)
!	end do
	do j=1,n-1,3
	xinte4=xinte4+(gx(j)+3*gx(j+1)+3*gx(j+2)+gx(j+3))*(3.0*h(i)/8.0) 
	end do
	write(k,*)i,ene(i),c1*xinte4-b
	   if(abs(c1*xinte4-b)<.01) then
	print*,"para n igual a",a(k)
	print*,"un valor aproximado  de la energia es"
	print*,ene(i)
	end if 
	end do 
	end do
        end program
	function f(x)
!	implicit double precision (a-h,o-z)
	  f=4*((1.0/x**12)-(1.0/x**6))
	end function f
	function f2(x)
!	implicit double precision (a-h,o-z)
	 f2= (.000010/x)*exp(-x/.15)
	end function f2
