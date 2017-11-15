cmake_minimum_required(VERSION 2.8)
project(joinMap)

find_package(PCL REQUIRED COMPANENT common io)
include_directories(${PCL_INCLUDE_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(joinMap joinMap.cpp)
target_link_libraries(joinMap ${PCL_LIABRARIES})