#include <iostream>
#include <cmath>

using namespace std;

class Particula
{
public:
    Particula(double yi, double vyi);
    double y, vy, ay, dt;
    void verlet(double k);
};

Particula::Particula(double yi, double vyi)
{
    y = yi;
    vy = vyi;
    ay = 0;
    dt = 0.01;
}

void Particula::verlet(double mk)
{
    double vtempy = vy + 0.5*ay*dt;
    y = y + vtempy*dt;
    ay = -9.8-vy*mk;
    vy = vtempy + ay*dt;
}

int main()
{
    double v=1;
    int i = 0;
    Particula gota(0,0);
    for(double mk = 0.1; mk < 10; mk+=0.1)
    {
        while(abs(gota.vy-v)>0.00000000001)
        {
            v=gota.vy;
            gota.verlet(mk);
            //cout<<++i<<"\t"<<gota.vy<<endl;
        }
        cout<<mk<<"\t"<<gota.vy<<endl;
    }
}
