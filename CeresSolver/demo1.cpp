#include<iostream>
#include <opencv2/core/core.hpp>
#include<ceres/ceres.h>
using namespace std;


struct CostFunctor
{
    const double _x, _y;
    CostFunctor(double x, double y): _x(x), _y(y){}

    template <typename T>
    bool operator() (const T* const mc, T* residual) const
    {
        residual[0] = T(_y) - ceres::exp(mc[0]*T(_x) + mc[1]);
        return true;
    }
};


int main(int argc, char** argv)
{
    google::InitGoogleLogging(argv[0]);

    double m=1.5, c=1.8;
    int N=200;
    double w_sigma =3.0;
    double mc[2]={0,0};
    vector<double> x_data, y_data;
    cv::RNG rng;

    cout<<"generating data..."<<endl;

    for(int i=0; i<N; i++)
    {
        double x = i/100.0;
        double y;
        x_data.push_back(x);
        y = ceres::exp(m*x+c)+rng.gaussian(w_sigma);
        y_data.push_back(y);
    }


    //construct the problem
    ceres::Problem problem;
    for(int i=0; i<N; i++)
    {
        ceres::CostFunction* cost_function= new ceres::AutoDiffCostFunction<CostFunctor, 1, 2>(new CostFunctor(x_data[i], y_data[i]));
        problem.AddResidualBlock(cost_function, NULL, mc);
    }

    ceres::Solver::Options options;
    options.linear_solver_type = ceres::DENSE_QR;
    options.minimizer_progress_to_stdout=true;

    ceres::Solver::Summary summary;

    ceres::Solve(options, &problem, &summary);

    cout<<summary.BriefReport()<<endl;
    cout<<"estimated m, c = ";
    for(auto item : mc) cout<<item<<"  ";
    cout<<endl;

    return 0;
}
