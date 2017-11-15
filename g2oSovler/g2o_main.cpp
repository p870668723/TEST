
#include<iostream>
#include<g2o/core/base_vertex.h>
#include<g2o/core/base_unary_edge.h>
#include<g2o/core/block_solver.h>
#include<g2o/core/optimization_algorithm_levenberg.h>
#include<g2o/core/linear_solver.h>
#include<g2o/solvers/dense/linear_solver_dense.h>
#include<eigen3/Eigen/Core>
#include<opencv2/core/core.hpp>
#include<cmath>
#include<chrono>

using namespace std;


//config my own vertex class
class myVertex :public g2o::BaseVertex<3, Eigen::Vector3d>
{
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
    virtual void setToOriginImpl(){
        _estimate<<0,0,0;
    }
    virtual void oplusImpl(const double* update){
        _estimate += Eigen::Vector3d(update);
    }
    virtual bool read(istream &in){}
    virtual bool write(ostream &out)const{}
};

//config my own edge class
class myEdge :public g2o::BaseUnaryEdge<1,double,myVertex>
{
public:
    EIGEN_MAKE_ALIGNED_OPERATOR_NEW
    myEdge(double x): BaseUnaryEdge(),_x(x){}
    void computeError(){
        const myVertex* v=static_cast<const myVertex*>(_vertices[0]);
        const Eigen::Vector3d abc = v->estimate();
        _error(0,0) = _measurement - abc(0,0)*std::exp(abc(1,0)*_x*_x+abc(2,0)*_x);
    }
    virtual bool read(istream &in){}
    virtual bool write(ostream &out)const{}
public:
    double _x;

};

int main(void)
{
    double a=.5,b=1.,c=1.0;
    double w_sigma = 0.1;
    int N=100;
    cv::RNG rng;
    vector<double> x_data,y_data;
    //generate the measure data
    for(int i=0;i<N;i++){
        double x=i/100.0;
        x_data.push_back(x);
        y_data.push_back(a*std::exp(b*x*x+c*x)+rng.gaussian(w_sigma));
    }

    std::ofstream outfile("./raw_data.txt");
    if(!outfile){
        cout<<"open failed..."<<endl;
        return -1;
    }
    for(int i=0; i<N; i++){
        outfile<<x_data[i]<<" "<<y_data[i]<<endl;
    }

    typedef g2o::BlockSolver<g2o::BlockSolverTraits<3,1>> Block;
    Block::LinearSolverType * linearSolver= new g2o::LinearSolverDense<Block::PoseMatrixType>();
    Block* solver_ptr = new Block(linearSolver);
    g2o::OptimizationAlgorithmLevenberg* solver = new g2o::OptimizationAlgorithmLevenberg(solver_ptr);
    g2o::SparseOptimizer optimizer;
    optimizer.setAlgorithm(solver);
    optimizer.setVerbose(true);

    myVertex *v = new myVertex();
    v->setEstimate(Eigen::Vector3d(0,0,0));
    v->setId(0);
    optimizer.addVertex(v);

    for(int i=0; i<N; i++){
        myEdge* e = new myEdge(x_data[i]);	//x_data[i] is using for calculate the "should be"
        e->setId(i);
        e->setVertex(0,v);
        e->setMeasurement(y_data[i]);	//y_data[i] is the "actually is"
        e->setInformation(Eigen::Matrix<double,1,1>::Identity()*1/(w_sigma*w_sigma));	//the covariance matrix of y_data[i]
        optimizer.addEdge(e);
    }

    optimizer.initializeOptimization();
    optimizer.optimize(1000);
    Eigen::Vector3d abc_estimated = v->estimate();
    cout<<"estimated model: "<<abc_estimated.transpose()<<endl;


    std::ofstream predict_file("./predict_data.txt");
    double a_p=abc_estimated(0,0);
    double b_p=abc_estimated(1,0);
    double c_p=abc_estimated(2,0);
    cout<<a_p<<"\n"<<b_p<<"\n"<<c_p<<endl;
    for(int i=0; i<N; i++){
        double x= i/100.0;
        predict_file<<a_p* std::exp(b_p*x*x + c_p*x)<<endl;
    }
    return 0;

}
