cmake_minimum_required(VERSION 2.8)

project(HelloSLAM)

include_directories("/usr/include/eigen3")

add_library(hello_shared libHelloSLAM.cpp)
add_executable(useHello helloSLAM.cpp)

target_link_libraries(useHello hello_shared)
