       program rk2
        real k1,k2
       dimension v(0:5), u(0:5), x(0:5), EK(0:4),y(0:5)
       dimension YK(5),YL(5)
         v(0)=150
       u(0)=150
       x(0)=0
       y(0)=0
        H=0.1
        C=0.005
        g=9.9
       open(unit=10,file='proyectil.txt',status='unknown')
       do k=1,40
           Ve=(u(0)**2+v(0)**2)**0.5
	EK(1) = u(0)
         EK(2) = -C*Ve*x(0)

	 YK(1) = EK(1)*H
                YL(1)=EK(2)*H

		YK(2) = H*(EK(1)+YL(1)/2)
         EK(2)=-C*Ve*(x(0)+YK(1)/2)
                YL(2) = H*(EK(2))
                x(0)=x(0)+(YK(1)+YK(2))*0.5
                u(0)=u(0)+(YL(1)+YL(2))*0.5
                
                EK(3) = v(0)
	EK(4) = -g-C*Ve*y(0)

	 YK(3) = EK(3)*H
                YL(3)=EK(4)*H

		YK(4) = H*(EK(3)+YL(3)/2)
		EK(4)=-g-C*Ve*(y(0)+YK(3)/2)
                YL(4) = H*(EK(4))
                y(0)=y(0)+(YK(3)+YK(4))*0.5
                v(0)=v(0)+(YL(3)+YL(4))*0.5

        write(10,*)x(0),y(0)
         end do
         close(10)
          end

