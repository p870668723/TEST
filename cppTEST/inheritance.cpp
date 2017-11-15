#include <iostream>
using namespace std;

class CLBasic
{
    public:
        int a;
        double b;
        CLBasic(){};
        CLBasic(int a,  double b):a(a),b(b)
        {
            cout<<"in CLBasic constructure!"<<endl;
        }
        virtual void say_sth(void)
        {
            cout<<"this is CLBasic!"<<endl;
        }
};
class CLDerivation: public CLBasic
{
    public:
        using CLBasic::CLBasic;
        char c;
        int* pt;
        CLDerivation(){};
        CLDerivation(int a, double b, char c):CLBasic(a,b)
        {
            this->c = c;
            cout<<"in CLDerivation constructre!"<<endl;
        }
        void say_sth(void) override
        {
            cout<<"this is CLDerivation!"<<endl;
        }
};

int main(void)
{
    CLDerivation obj(1, 1.0, 'm');
    CLDerivation obj2(1, 1.0);
    CLBasic *pt_basic=&obj;
    (*pt_basic).say_sth();
    CLDerivation *pt_derivation = (CLDerivation *) pt_basic;
    cout<<(*pt_derivation).c<<endl;

    return 0;
}
