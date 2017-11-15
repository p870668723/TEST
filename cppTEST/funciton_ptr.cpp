#include <iostream>
#include <string>
using namespace std;
typedef int (*fptr)(int ,int);
class pf
{
    public:
        static int add(int a, int b)
        {
            return a+b;
        }
    private:
        string name;
};
int add(int a, int b)
{
    return a+b;
}

fptr call_f(void)
{
    return pf::add;
}

int main(void)
{
    fptr fp = call_f();
    cout<<"answer is: "<<(*fp)(4,7)<<endl;
    return 0;
}
