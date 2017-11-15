#include <iostream>
using namespace std;

template<typename T>
void printv(T val)
{
    cout<<val<<endl;
}
//template<typename T, typename... Args>
template<typename... Args,typename T>
void printv(T val,Args... args)
{
    cout<<val;
    printv(args...);
}
int main(void)
{
    int m= 10;
    printv("this",9.2,m);
    return 0;
}
