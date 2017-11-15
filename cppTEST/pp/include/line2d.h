#ifndef _LINE_H
#define _LINE_H
class line2d
{
private:
    double _a,_b,_c;
public:
    line2d(){};
    line2d(double a, double b, double c):_a(a),_b(b),_c(c){} ;
    void get_line(double &a, double &b, double &c);
    void set_line(double a, double b, double c);
    bool parallel(const line2d &src_obj);
    bool vertical(const line2d &src_obj);
};

#endif