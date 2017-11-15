#include "point.h"

Point Point::operator + (const Point &rh_arg)
{
    Point new_point;
    new_point._x = _x + rh_arg._x;
    new_point._y = _y + rh_arg._y;
    return new_point;
}

Point Point::operator - (const Point &rh_arg)
{
    Point new_point;
    new_point._x = _x - rh_arg._x;
    new_point._y = _y - rh_arg._y;
    return new_point;
}
