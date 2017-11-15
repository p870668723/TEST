#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main(void)
{
    string article;
    fstream file_io("text.txt");
    file_io<<"第一个阶段，人的依赖关系阶段。第二个阶段，物的依赖阶段";
    getline(file_io, article);
    cout<<article.c_str()<<endl;
    file_io.close();
    return 0;
}
