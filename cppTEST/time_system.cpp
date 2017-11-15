#include <ctime>
#include <time.h>
#include <iostream>
#include <cstdlib>
using namespace std;

void my_function()
{
    cout<<"leaving"<<endl;
}
int main()
{
    atexit(my_function);
    time_t right_now=time(NULL);
    long t1=clock();
    for(int i=0; i<100000; i++)
    {};
    long t2=clock();
    cout<<"time passed: "<<(t2-t1)<<"us"<<endl;
    cout<<"time passed: "<<(t2-t1)/(double)CLOCKS_PER_SEC<<"s"<<endl;       //CLOCKS_PER_SEC is include in the <ctime>
    cout<<ctime(&right_now)<<endl;

    cout<<"PATH = "<<getenv("PATH")<<endl;
    system("ls");       //shell cmd
    //system("vim time.cpp");
    exit(0);
    return 0;
}

