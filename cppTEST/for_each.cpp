#include <iostream>
#include <algorithm>
using namespace std;

int main(void)
{
    int arr[]={100, 1, 23, 41, 53, 42, 41, 13, 43, 24,67};
    sort(arr,arr+sizeof(arr)/sizeof(arr[0]));
    for_each(arr,arr+11,[](int x){cout<<x<<" ";});  //from the header <algorithm>
    return 0;
}


