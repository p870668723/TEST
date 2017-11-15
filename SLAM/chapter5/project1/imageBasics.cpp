#include <iostream>
#include <chrono>
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
using namespace std;

int main(int argc, char** argv)
{
    cv::Mat image;
    image = cv::imread(argv[1]);
    cv::imshow("image", image);
    cv::waitKey(0);
    cout<<"test message"<<endl;
    return 0;
}
