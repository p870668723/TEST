#ifndef _POINT_H
#define _POINT_H
class Point
{
    public:
    double _x,_y;
    Point(){};
    Point(double x, double y):_x(x),_y(y){};
    Point operator + (const Point &rh_arg);
    Point operator - (const Point &rh_arg);
};
#endif