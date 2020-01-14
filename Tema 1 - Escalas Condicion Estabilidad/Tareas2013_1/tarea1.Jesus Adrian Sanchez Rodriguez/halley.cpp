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
    dt = 0.0001;
}

void Particula::verlet()
{
    double vtempx = vx + 0.5*ax*dt;
    double vtempy = vy + 0.5*ay*dt;
    x = x + vtempx*dt;
    y = y + vtempy*dt;
    ax = -x*50000/pow(x*x+y*y, 1.5);
    ay = -y*50000/pow(x*x+y*y, 1.5);
    vx = vtempx + ax*dt;
    vy = vtempy + ay*dt;
}

int main()
{
    Particula halley(-35.1,0,0,9.2);
    for(int i = 0; i < 20000; ++i)
    {
        halley.verlet();
        cout<<halley.x<<'\t'<<halley.y<<endl;
    }
}
