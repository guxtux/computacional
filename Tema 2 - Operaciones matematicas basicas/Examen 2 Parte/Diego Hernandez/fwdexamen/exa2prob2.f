	program exam2problema2
	implicit double precision (a-h,o-z)
        dimension x(0:10000000),fx(0:10000000)  
         n=1000
        h=100.0/n
         open(1,file="exam2problema2.dat",status="replace")
        do i=0,n
        x(i)=i*h-50.0
	 fx(i)=(x(i)*exp(x(i)))/(exp(exp(x(i))))
        write(1,*)i,x(i),fx(i)
        end do
!        xinte=0
	xinte1=0
	xinte2=0
	xinte3=0
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
	print*,"el valor de la integral  es"
	print*,"con el metodo de trapecio"
        print*,xinte1
	print*,"con el metodo de simpson"
	print*,xinte2
	print*,"con el metodo de simpson 3/8"
	print*,xinte3
        end program
