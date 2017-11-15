#include"line2d.h"

void line2d::get_line(double &a,double &b, double &c )
{
    a = _a;
    b = _b;
    c = _c;
}

void line2d::set_line(double a, double b, double c )
{
    _a = a;
    _b = b;
    _c = c;
}

bool line2d::parallel(const line2d &src_obj )
{
    if (this->_a ==0 && src_obj._b==0) return true;
    else if(this->_b ==0 && src_obj._a==0) return true;
    else
    return ( src_obj._a * this->_b == src_obj._b * this->_a );
}

bool line2d::vertical(const line2d &src_obj )
{
    return (true);
}