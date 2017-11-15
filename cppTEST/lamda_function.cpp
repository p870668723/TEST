#include <iostream>
#include <algorithm>
#include <iomanip>
#include <functional>
using namespace std;


function<float(int,int)> get_fun()
{
    int n=10;
    return [n](int a, int b){return a+b+n;};
}

void f3(int a){cout<<a<<" ";}

int main(void)
{
    int x=10;
    int sum=0;
    int arr[5] = {5,6,7,8,9};

    auto f=[&x] (int a, int b){
        x=3;
        return (a+b);
    };
    //for_each(arr, arr+6,f3);
    for_each(arr, arr+5,[&sum](int n) {sum=sum+n;});
    auto ff=get_fun();
    cout<<"sum:"<<sum<<endl;
    cout<<"ff:"<<setprecision(5)<<ff(2,3)+0.1<<endl;
    cout <<"f:"<<f(2,3)<<endl;
    cout <<"x:"<<x<<endl;
    return 0;
}
