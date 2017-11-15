#include <iostream>
#include <iomanip>
using namespace std;

int main(void)
{
    string astring;
    cout<<"input some number, end with '#':";
    getline(cin,astring,'#');
    cout<<atof(astring.c_str())+1<<endl;
    return 0;
}
