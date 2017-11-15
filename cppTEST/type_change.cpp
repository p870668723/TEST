#include <iostream>
#include <memory>
using namespace std;

class CLpoint
{
    public:
    double x;
    double y;

    CLpoint(double x, double y):x(x),y(y){};
    CLpoint(){};
};
class CLx
{
    public:
    double x;
    int *pt;
    CLx(double x): x(x){ pt = new int(10);};
    operator CLpoint()
    {
        CLpoint newp(x,x);
        return newp;
    }
};

int main(void)
{
    CLx clx(10.1);
    cout<<clx.pt<<endl;
    delete clx.pt;
    *clx.pt =123;
    cout<<clx.pt<<endl;
    CLpoint p = CLpoint(clx);
    cout<<CLpoint(clx).x<<endl;
    cout<<p.y<<endl;
    return 0;
}
