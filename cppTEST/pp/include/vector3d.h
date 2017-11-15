#ifndef _VECTOR3D_H
#define _VECTOR3D_H

class vector3d
{
private:
    double v[3]={0,0,0} ;
public:
    vector3d(){};
    vector3d(double a, double b, double c);
    void get_param(double &a, double &b, double &c );
    void set_param(double a, double b, double c );
    friend vector3d operator + (const vector3d &left_obj ,const vector3d &right_obj);
    //vector3d operator - (const vector3d &src_obj);
    //vector3d operator () (const vector3d &src_obj);
    //vector3d operator [] (const vector3d &src_obj);
};

#endif