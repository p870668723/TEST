#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main(void)
{
    int elsments[] = {1,2,3,4};
    const size_t N = sizeof(elsments)/sizeof(elsments[0]);
    vector<int> vec(elsments, elsments+N);

    int count =0;
    do
    {
        cout<<++count<<": ";
        copy(vec.begin(), vec.end(), ostream_iterator<int>(cout, ", "));
        cout<<endl;
    }while(next_permutation(vec.begin(),vec.end()));
    return 0;
}
