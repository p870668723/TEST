#include <iostream>
#include <memory>
using namespace std;
class student
{
    public:
    student(string nm, int i, double sc):name(nm),id(i),score(sc){};
    student(){};
    string name;
    int id;
    double score;
};

int main(void)
{
    //student stu1("pengfei", 299, 98.4);
    shared_ptr<student> ip1(new student("pengfei", 229, 98.3));
    student stu1 = *ip1;
    cout<<stu1.score<<endl;
    cout<<ip1->name<<endl;
    try{
       int a=0,b=1;
       cout<<b/a<<endl; 
    }
    catch (exception e){
        cout<<e.what()<<endl;
    }
    return 0;
}
