#include <iostream>
#include <fstream>
#include <cstdlib>

using namespace std;

union Tst
{
    int ints[2];
    double dbl;
};
int main(void)
{
    Tst p,f;
    p.ints[0]=1;
    p.ints[1]=2;

    f.dbl = p.dbl;
    cout<<f.ints[0]<<endl;
    cout<<f.ints[1]<<endl;

    return 0;
}
