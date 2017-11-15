#include <iostream>
#include <memory>
using namespace std;

int main(void)
{
    unique_ptr<int[]> up2(new int[1000]);
    up2[1]=10;
    return 0;
}
