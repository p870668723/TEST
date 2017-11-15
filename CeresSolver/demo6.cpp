#include<iostream>
#include<stdlib.h>
#include<random>
#include<cmath>
#include "ceres/ceres.h"
using ceres::AutoDiffCostFunction;
using ceres::CostFunction;
using ceres::Problem;
using ceres::Solver;
using ceres::Solve;
using namespace std;

struct CostFunctor{
    CostFunctor(double x, double y): _x(x),_y(y){}

    template<typename T> bool operator()(const T* const ab, T* residual) const{
        residual[0] = _y - ab[0]*pow(_x-ab[1],2);
        return true;
    }
    private:
    const double _x;
    const double _y;
};

int main(void){
    double x[50],y[50];
    double ab[2];
    //generate the measured data
    default_random_engine e;
    normal_distribution<double> normal(0,0.5);
    for(int i=0; i<50; i++){
        //double rnd = (rand()/double(RAND_MAX))*2-1;
        double rnd = normal(e);

        x[i]=i/10;      //x is in [0,5)
        y[i]=0.5*pow(x[i]-2,2)+rnd;
        //cout<<rnd<<endl;
    }
    cout<<"*********************************"<<endl;

    Problem probelm;
    for(int i=0; i<50; i++)
        probelm.AddResidualBlock(
            new AutoDiffCostFunction<CostFunctor,1,2>(new CostFunctor(x[i],y[i])),
            new ceres::CauchyLoss(0.8),
            ab
        );

    Solver::Options options;
    options.linear_solver_type = ceres::DENSE_QR;
    options.minimizer_progress_to_stdout = true;

    Solver::Summary summary;
    Solve(options, &probelm, &summary);

    cout<<summary.BriefReport()<<endl;
    cout<<"a="<<ab[0]<<"\nb="<<ab[1]<<endl;
    return 0;
}