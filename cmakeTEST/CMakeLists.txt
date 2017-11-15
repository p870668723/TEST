cmake_minimum_required(VERSION 2.8)
project(TE)

message(STATUS "this is BINARY: " ${TE_BINARY_DIR})
message(STATUS "this is SOURCE: " ${TE_SOURCE_DIR})

add_executable(te src/te.cpp)
