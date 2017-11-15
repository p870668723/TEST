#include "ptr.h"

void point2d::get_xy(double &x, double &y)
{
    x = _x;
    y = _y;
}

void point2d::set_xy(double x, double y)
{
    this->_x = x;
    this->_y = y;
}

point2d point2d::operator + (const point2d &sr_obj)
{
    point2d new_point;
    new_point._x = this->_x + sr_obj._x;
    new_point._y = this->_y + sr_obj._y;
    return new_point;
}

point2d point2d::operator - (const point2d &sr_obj)
{
    point2d new_point;
    new_point._x = this->_x - sr_obj._x;
    new_point._y = this->_y - sr_obj._y;
    return new_point;
}
