#include <iostream>
#include <cstdarg>
using namespace std;
void pp(int n ...)
{
    va_list(args);
    va_start(args, n);
    for(int i=0; i<n; i++)
    {
        cout<<va_arg(args, int)<<endl;
    }
    va_end(args);
}
int main(int argc, char *argv[])
{
    pp(7,2,3,4,5,6,7,8);
    return 0;
}
