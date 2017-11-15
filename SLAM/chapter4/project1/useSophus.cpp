#include<iostream>
#include<cmath>
#include<Eigen/Core>
#include<Eigen/Geometry>
#include "sophus/so3.h"
#include "sophus/se3.h"

using namespace std;

int main(void)
{
    Eigen::Matrix3d R = Eigen::AngleAxisd(M_PI/2, Eigen::Vector3d(0,0,1)).toRotationMatrix();
    Sophus::SO3 SO3_R(R);
    cout<<"test message!"<<endl;
}