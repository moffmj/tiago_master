cmake_minimum_required(VERSION 3.0.2)
project(matt_test_package)

find_package(catkin REQUIRED COMPONENTS
  dynamic_reconfigure
  actionlib
  actionlib_msgs
  aruco_ros
  geometry_msgs
  moveit_msgs
  rospy
  std_msgs
  std_srvs
)


generate_dynamic_reconfigure_options(
  cfg/SphericalGrasp.cfg
  )

add_action_files(
  FILES
  PickUpPose.action
)

generate_messages(
  DEPENDENCIES
  actionlib_msgs geometry_msgs
)

catkin_package(
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
