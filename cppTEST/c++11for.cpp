#include <iostream>
#include <algorithm>
using namespace std;

float matrix[3][5]={{1,2,3,4,5},
                    {6,7,8,9,1},
                    {2,3,4,5,6}};

void reset_matrix(float **ptr)
{
    for(int i=0; i<3; i++)
        for(int j=0; j<5; j++)
        {
            *(*(ptr+i)+j)=0;
        }
}

int main(void)
{
    int arr[5] = {1,2,3,4,5};

    for(int i=0; i<5; i++ )
        *(arr+i)=0;
    cout<<arr[3]<<endl;
    cout<<"**********************************"<<endl;
    for(auto &mtx:matrix)
    {
        for(auto &element:mtx)
            cout<<element<<" ";
        cout<<"\n";
    }
    return 0;
}
