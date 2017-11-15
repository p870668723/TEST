#include<iostream>
#include<boost/format.hpp>
#include<string>
#include<fstream>
using namespace std;

int main(void)
{
    boost::format fmt("./%s.%s");
    ifstream fin("./name.txt");
    string file;
    string word;
    while(1)
    {
        if(fin.eof()==true) break;
        fin>>file;
        cout<<fmt%file%"txt"<<endl;
        //ifstream sub_fin("./"+file+".txt");
        ifstream sub_fin( (fmt%file%"txt").str() );
        if(!sub_fin) cout<<"err..."<<endl;
        sub_fin>>word;
        cout<<word<<endl;
        sub_fin.close();   
    }
    cout<<"...end..."<<endl;
    return 0;
}