cmake_minimum_required(VERSION 3.0.2)
project(ros_tutorial)

find_package(catkin REQUIRED COMPONENTS roscpp rospy std_msgs )

catkin_package(DEPENDS roscpp)
include_directories(${catkin_INCLUDE_DIRS})

add_executable(talker src/talker.cpp)
target_link_libraries(talker ${catkin_LIBRARIES})
install(TARGETS talker RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

add_executable(listener src/listener.cpp)
target_link_libraries(listener ${catkin_LIBRARIES})
install(TARGETS listener RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})