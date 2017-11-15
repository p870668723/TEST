#include <iostream>
#include <algorithm>
#include <vector>
#include <iterator>
using namespace std;

void prt(vector<int> vec)
{
    for_each(vec.begin(),vec.end(),[](int n){cout<<n<<",";});
    cout<<endl;
}
int main(void)
{
    vector<int> vec;
    static int count =1;

    vector<int>::iterator it;
    for(int i=0; i<5; i++)
        vec.push_back(i);

    random_shuffle(vec.begin(),vec.end());
    prt(vec);

    rotate(vec.begin(),vec.begin()+3,vec.end());
    prt(vec);

    iota(vec.begin(),vec.end(),11);
    prt(vec);

    while(next_permutation(vec.begin(),vec.end()))
    {
        prt(vec);
        count++;
    }
    cout<<"total: "<<count<<endl;

    cout<<accumulate(vec.begin(),vec.end(),0)<<ends;
    return 0;
}
