#include<iostream>
#include<cstdlib>
#include "ptr.h"
using namespace std;

void ext(void);


int main(void)
{
    double x,y;
    point2d p1(1,3);
    point2d p2(2,4);
    point2d p3=p1+p2;
    point2d p4=p2-p1;

    p4.get_xy(x,y);
    cout<<"x = "<<x<<endl;
    cout<<"y = "<<y<<endl;
    atexit(ext);
    return 0;
}

void ext(void)
{
    cout<<"exting..."<<endl;
}