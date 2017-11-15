#include <iostream>
#include <cmath>
#include <Eigen/Core>
#include <Eigen/Geometry>

using namespace std;

int main(void)
{
    Eigen::Vector3d vct(1,2,3);
    Eigen::Vector3d vc(1,2,3);

    Eigen::AngleAxisd rotation_vector(M_PI/3, Eigen::Vector3d(0, 0, 1));
    Eigen::Matrix3d rotation_matrix = rotation_vector.matrix();         //translate the angle_axis to rotation matrix
    Eigen::Quaterniond q = Eigen::Quaterniond(rotation_vector);           //translate the angle_axis to quaternion
    cout<<"after rotation matrix: \n"<<rotation_matrix*vct<<endl;
    cout<<"after angle_axis: \n"<<rotation_vector*vct<<endl;
    cout<<"after quaternion: \n"<<q*vct<<endl;          //here the * is override while quaternion mutplying the 3d vector
    cout<<"the q is \n"<<q.coeffs()<<endl;

    Eigen::Quaterniond co = Eigen::Quaterniond(0,1,2,3);
    Eigen::Quaterniond q_inverse = q.inverse();
    Eigen::Quaterniond result = q*co*q_inverse;
    cout<<"direct calculate: \n"<<result.coeffs()<<endl;
    
    //construct the T matrix
    Eigen::Isometry3d T = Eigen::Isometry3d::Identity();
    T.rotate(rotation_vector);
    T.pretranslate(Eigen::Vector3d(1,3,4));
    cout<<"T :\n"<<T.matrix()<<endl;
    return 0;
}
