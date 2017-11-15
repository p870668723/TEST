#include <iostream>
using namespace std;
void set_matrix_other(double **a)
{
    *((double*)a + 2*10 + 5)= 30;
    cout<<"~~~~~~~~~~~"<<endl;
}

void set_matrix(double a[][10],int rows)
{
    for(int i=0; i<rows; i++)
        for(int j=0; j<10; j++)
        {
            a[i][j]=i+j;
        }
}

int main(void)
{
    double my_matrix[5][10];
    set_matrix(my_matrix, 5);
    cout<<my_matrix[2][5]<<endl;
    set_matrix_other( (double **)my_matrix);
    cout<<my_matrix[2][5]<<endl;

    return 0;
}
