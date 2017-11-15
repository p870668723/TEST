#include <iostream>
using namespace std;

class perents
{
    public:
        int p=20;
};
class child:public perents
{
    public:
        int c=10;

};

int main(void)
{
    int a=10;
    cout<<static_cast<double>(a);
    cout<<"*******************************"<<endl;

    perents *pp = new child;
    cout<<"class:"<<((child*)pp)->p<<endl;
    cout<<"class:"<<((child*)pp)->c<<endl;

    cout<<"*******************************"<<endl;

    child *ch = new child;
    cout<<((perents*)ch)->p<<endl;

    return 0;
}
