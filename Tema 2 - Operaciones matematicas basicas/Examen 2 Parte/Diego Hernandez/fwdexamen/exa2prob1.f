	program exam2problema1
	implicit double precision (a-h,o-z)
        dimension x(0:10000000),fx(0:10000000),gx(0:100000)  
         n=1000
        h=100.0/n
	 pi=2.0*asin(1.0)
	 b=sqrt(pi)
         open(1,file="exam2problema1.dat",status="replace")
	 open(2,file="exam2problema1b.dat",status="replace")
        do i=0,n
        x(i)=i*h
	 fx(i)=(x(i)**9)/(exp(x(i)))
	 gx(i)=2.0*exp(-x(i)**2)
        write(1,*)i,x(i),fx(i)
	write(2,*)i,x(i),gx(i)
        end do
!        xinte=0
	xinte1=0
	xinte2=0
	xinte3=0
	xinte4=0
        xinte5=0
        xinte6=0
!        do i=0,n                        
!        xinte=xinte+fx(i)*h
!	end do 
	do i=0,n-1
	xinte1=xinte1+(h*(fx(i+1)+fx(i)))/2.0
!       print* ,xinte
        end do
	do i=0,n-2,2
	xinte2=xinte2+(fx(i)+4.0*fx(i+1)+fx(i+2))*(h/3.0)
	end do
	do i=0,n-3,3
	xinte3=xinte3+(fx(i)+3.0*fx(i+1)+3.0*fx(i+2)+fx(i+3))*(3.0*h/8.0) 
	end do
	do i=0,n-1
        xinte4=xinte4+(h*(gx(i+1)+gx(i)))/2.0
!       print* ,xinte
        end do
        do i=0,n-2,2
        xinte5=xinte5+(gx(i)+4.0*gx(i+1)+gx(i+2))*(h/3.0)
        end do
        do i=0,n-3,3
	xinte6=xinte6+(gx(i)+3.0*gx(i+1)+3.0*gx(i+2)+gx(i+3))*(3.0*h/8.0)
        end do
	print*,"el valor de la integral para x=10"
	print*,"con el metodo de trapecio"
        print*,xinte1
	print*,"con error",abs(362880.0-xinte1)/362880.0
	print*,"con el metodo de simpson"
	print*,xinte2
	print*,"con error",abs(362880.0-xinte2)/362880.0
	print*,"con el metodo de simpson 3/8"
	print*,xinte3
	print*,"con error",abs(362880.0-xinte3)/362880.0
	print*,"el valor de la integral para x=1/2"
        print*,"con el metodo de trapecio"
        print*,xinte4
	print*,"con error",abs(b-xinte4)/b
        print*,"con el metodo de simpson"
        print*,xinte5
	print*,"con error",abs(b-xinte5)/b
        print*,"con el metodo de simpson 3/8"
        print*,xinte6
	print*,"con error",abs(b-xinte6)/b
        end program
