#ifndef _PTR_H
#define _PTR_H

class point2d
{
private:
    double _x,_y;
public:
    point2d(double x, double y):_x(x),_y(y){};
    point2d(){};
public:
    void get_xy(double &x, double &y);
    void set_xy(double x, double y);
    point2d operator + (const point2d &sr_obj);
    point2d operator - (const point2d &sr_obj);
};
#endif