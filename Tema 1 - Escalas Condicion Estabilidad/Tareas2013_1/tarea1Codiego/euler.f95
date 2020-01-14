program suma3
n=10000
do i=1,n
eul=eul+1.0/(i*1.0)
end do 
euler=eul+log(n*1.0)
Print*, euler
end program
