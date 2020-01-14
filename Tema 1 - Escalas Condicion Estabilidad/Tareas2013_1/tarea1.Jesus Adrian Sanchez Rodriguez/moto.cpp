#include <iostream>
#include <cmath>

using namespace std;

class Particula
{
public:
    Particula(double xi, double yi, double vxi, double vyi);
    double x, y, vx, vy, ax, ay, dt;
    void verlet();
};

Particula::Particula(double xi, double yi, double vxi, double vyi)
{
    x = xi;
    y = yi;
    vx = vxi;
    vy = vyi;
    ax = 0;
    ay = 0;
    dt = 0.01;
}

void Particula::verlet()
{
    double vtempx = vx + 0.5*ax*dt;
    double vtempy = vy + 0.5*ay*dt;
    x = x + vtempx*dt;
    y = y + vtempy*dt;
    ax = -0.93*1.2/500*vx*vx/sqrt(vx*vx+vy*vy);
    ay = -0.93*1.2/500*vy*vy/sqrt(vx*vx+vy*vy)-9.8;
    vx = vtempx + ax*dt;
    vy = vtempy + ay*dt;
}

int main()
{
    double teta;
    double max = 0, max_teta = 0;
    for(teta = 0; teta < M_PI/3.5; teta+= 0.01)
    {
        Particula moto(0,0,67*cos(teta),67*sin(teta));
        while(moto.y>=0)
        {
            moto.verlet();
            //cout<<moto.x<<'\t'<<moto.y<<endl;
        }
        //cout<<teta<<' grados\t'<<moto.x<<endl;
        if(moto.x>max)
        {
            max = moto.x;
            max_teta = teta;
        }
    }
    cout<<max_teta*180/M_PI<<"° \t"<<max<<endl;
}
