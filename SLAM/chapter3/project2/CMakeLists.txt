cmake_minimum_required(VERSION 2.8)

project(useGeometry)
add_definitions(-std=c++11)
include_directories("/usr/include/eigen3")
add_executable(useGeometry useGeometry.cpp)
#target_link_libraries(useGeometry)
