# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.5

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pf/TEST/SLAM/chapter3/project2

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pf/TEST/SLAM/chapter3/project2/build

# Include any dependencies generated for this target.
include CMakeFiles/useGeometry.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/useGeometry.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/useGeometry.dir/flags.make

CMakeFiles/useGeometry.dir/useGeometry.cpp.o: CMakeFiles/useGeometry.dir/flags.make
CMakeFiles/useGeometry.dir/useGeometry.cpp.o: ../useGeometry.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pf/TEST/SLAM/chapter3/project2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/useGeometry.dir/useGeometry.cpp.o"
	/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/useGeometry.dir/useGeometry.cpp.o -c /home/pf/TEST/SLAM/chapter3/project2/useGeometry.cpp

CMakeFiles/useGeometry.dir/useGeometry.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/useGeometry.dir/useGeometry.cpp.i"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/pf/TEST/SLAM/chapter3/project2/useGeometry.cpp > CMakeFiles/useGeometry.dir/useGeometry.cpp.i

CMakeFiles/useGeometry.dir/useGeometry.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/useGeometry.dir/useGeometry.cpp.s"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/pf/TEST/SLAM/chapter3/project2/useGeometry.cpp -o CMakeFiles/useGeometry.dir/useGeometry.cpp.s

CMakeFiles/useGeometry.dir/useGeometry.cpp.o.requires:

.PHONY : CMakeFiles/useGeometry.dir/useGeometry.cpp.o.requires

CMakeFiles/useGeometry.dir/useGeometry.cpp.o.provides: CMakeFiles/useGeometry.dir/useGeometry.cpp.o.requires
	$(MAKE) -f CMakeFiles/useGeometry.dir/build.make CMakeFiles/useGeometry.dir/useGeometry.cpp.o.provides.build
.PHONY : CMakeFiles/useGeometry.dir/useGeometry.cpp.o.provides

CMakeFiles/useGeometry.dir/useGeometry.cpp.o.provides.build: CMakeFiles/useGeometry.dir/useGeometry.cpp.o


# Object files for target useGeometry
useGeometry_OBJECTS = \
"CMakeFiles/useGeometry.dir/useGeometry.cpp.o"

# External object files for target useGeometry
useGeometry_EXTERNAL_OBJECTS =

useGeometry: CMakeFiles/useGeometry.dir/useGeometry.cpp.o
useGeometry: CMakeFiles/useGeometry.dir/build.make
useGeometry: CMakeFiles/useGeometry.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pf/TEST/SLAM/chapter3/project2/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable useGeometry"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/useGeometry.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/useGeometry.dir/build: useGeometry

.PHONY : CMakeFiles/useGeometry.dir/build

CMakeFiles/useGeometry.dir/requires: CMakeFiles/useGeometry.dir/useGeometry.cpp.o.requires

.PHONY : CMakeFiles/useGeometry.dir/requires

CMakeFiles/useGeometry.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/useGeometry.dir/cmake_clean.cmake
.PHONY : CMakeFiles/useGeometry.dir/clean

CMakeFiles/useGeometry.dir/depend:
	cd /home/pf/TEST/SLAM/chapter3/project2/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pf/TEST/SLAM/chapter3/project2 /home/pf/TEST/SLAM/chapter3/project2 /home/pf/TEST/SLAM/chapter3/project2/build /home/pf/TEST/SLAM/chapter3/project2/build /home/pf/TEST/SLAM/chapter3/project2/build/CMakeFiles/useGeometry.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/useGeometry.dir/depend

