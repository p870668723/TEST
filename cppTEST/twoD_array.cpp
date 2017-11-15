#include <iostream>
#include <algorithm>
using namespace std;

void reset_m(double **p);

int main(void)
{
    double mat[3][3] = {{0,1,2},
                        {3,4,5},
                        {6,7,8}};

    reset_m((double **)mat);
    *( *(mat+2)+2)=111;
    cout<<"*************************"<<endl;
    for(int i=0; i<3; i++)
    {
        for(int j=0; j<3; j++)
        {
            cout<<*(*(mat+i)+j)<<" ";
        }
        cout<<endl;
    }
    return 0;
}

void reset_m(double **p)
{

    for(int i=0; i<4; i++)
    {
        for(int j=0; j<4; j++)
        {
            *( (double*)(p+i) +j )=10.0;
            //cout<<*(   ((double*)p+i)+j   )<<" ";
            //cout<<**(p+i)+j<<" ";
        }
        //cout<<endl;
    }

}

