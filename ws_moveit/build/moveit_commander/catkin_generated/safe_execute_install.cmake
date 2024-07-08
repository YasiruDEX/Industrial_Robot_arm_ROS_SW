execute_process(COMMAND "/home/sandun/ws_moveit/build/moveit_commander/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/sandun/ws_moveit/build/moveit_commander/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
