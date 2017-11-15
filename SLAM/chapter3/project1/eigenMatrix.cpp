#include <iostream>
#include <Eigen/Dense>
#include <Eigen/Core>
#include <ctime>
using namespace std;

int main(int argc, char *argv[])
{
    Eigen::Matrix<double, 50, 50> matrix_r;

    matrix_r = Eigen::MatrixXd::Random(50, 50);

    clock_t tim_st = clock();
    //cout<<matrix_r.inverse()<<endl;
    cout<<"cost: "<<1000*(clock()-tim_st)/(double)CLOCKS_PER_SEC<<" ms"<<endl;


    return 0;
}
