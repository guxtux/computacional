program gota1 
dimension t(0:1000),yt(0:1000),v(0:1000),y2t(0:1000)
open(1,file="gota1.dat" ,status="new")
n=1000
H=1/5.0
g=9.81
write(*,*) "dame m/k"
read(*,*) q
do i=1,n
T(i)=I*H
Yt(i)=-(q)*g*(t(i)-(q)*exp(-(q)*t(i)))
Vt(i)=-(q)*g*(1-exp(-(q)*t(i)))
Y2t(i)=-g*(t**2)/2
write(1,*)t(i),yt(i),vt(i),y2t(i)
end do 
end program
