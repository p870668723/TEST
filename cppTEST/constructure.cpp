#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

class Ctest
{
    public:
        static int num;
        Ctest(){num++;cout<<"默认构造函数"<<endl;};
        Ctest(double a);
        Ctest(double a, double b);
        Ctest(double a, int b);
        Ctest(const Ctest &t);
        const int &quote=m_private;
        ~Ctest();
    private:
        double x;
        double y;

        int m_private=12431;
};
int Ctest::num=0;

Ctest::Ctest(const Ctest &t)
{
    x=t.x;
    y=t.y;
    num++;
    cout<<"拷贝构造函数"<<endl;
}
Ctest::~Ctest()
{
    num--;
}
Ctest::Ctest(double a)
{
    x=a;
    num++;
    cout<<"单参数构造函数"<<endl;
}
Ctest::Ctest(double a, double b):x(a),y(b)//initializing parameter
{
    num++;
    cout<<"参数化列表"<<endl;
}

Ctest::Ctest(double a,int b):Ctest(a)//委托构造函数
{
    cout<<"委托构造函数"<<endl;
    y=b;
    //num++;
}



class Cchild: public Ctest
{
    public:
        using Ctest::Ctest;//启用基类的构造函数，
        Cchild(){};
        Cchild(double a, double b, double c, char *nm):Ctest(a,b)
        {
            strcpy(name,nm);
            z=c;
        }
    public:
        double z;
        char name[20];
};


int main(void)
{
    Ctest tt;
    Ctest t2(1.0);
    Ctest t3(0.1,0.3);
    Ctest t4(0.4,1);
    Ctest t5=t3;
    Ctest *p = new Ctest;
    cout<<"total:"<<Ctest::num<<endl;
    delete p;
    cout<<"total:"<<Ctest::num<<endl;
    char nm[]="child";
    Cchild obj_child(0.1, 1, 1,nm);
    cout<<obj_child.z<<endl;
    cout<<obj_child.name<<endl;

    return 0;
}
