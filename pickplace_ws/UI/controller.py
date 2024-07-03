#! /usr/bin/python3
# -*- coding: utf-8 -*-

import sys, copy
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from controller_window import Ui_Form
# ROS
import rospy
from geometry_msgs.msg import Pose
import moveit_commander

block_pose = Pose()

class GUI(QDialog):

    def __init__(self,parent=None):
        super(GUI, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.arm = moveit_commander.MoveGroupCommander("arm")
        self.gripper = moveit_commander.MoveGroupCommander("gripper")

    def Place_on_red(self):
        waypoints = []

        arm_current_pose = Pose()
        arm_current_pose = self.arm.get_current_pose()
        self.arm.clear_pose_targets()
        self.arm.set_goal_tolerance(0.01)

        target_pose = Pose()
        target_pose.position.x = arm_current_pose.pose.position.x
        target_pose.position.y = arm_current_pose.pose.position.y
        target_pose.position.z = 0.2
        target_pose.orientation.x = 0.2
        target_pose.orientation.y = 1
        target_pose.orientation.z = 0
        target_pose.orientation.w = 0  
        waypoints.append(copy.deepcopy(target_pose))

        print("target pose")
        print(target_pose)
        (plan, fraction) = self.arm.compute_cartesian_path(waypoints, 0.005, 0.0)  # waypoints to follow  # eef_step
        self.arm.execute(plan, wait=True)

    def Grab(self):
        print(str(self.gripper.get_current_state()))
        self.gripper.set_goal_tolerance(0.005)
        self.gripper.set_named_target("close")
        self.gripper.go()

    def Open(self):
        print(str(self.gripper.get_current_state()))
        self.gripper.set_goal_tolerance(0.005)
        self.gripper.set_named_target("open")
        self.gripper.go()

    def Pick_up_the_block(self):
        global block_pose    
        waypoints = []
        arm_current_pose = Pose()
        arm_current_pose = self.arm.get_current_pose()
        self.arm.clear_pose_targets()
        self.arm.set_goal_tolerance(0.01)

        waypoint1 = Pose()
        waypoint1.position.x = block_pose.position.x
        waypoint1.position.y = block_pose.position.y
        waypoint1.position.z = arm_current_pose.pose.position.z
        waypoint1.orientation = arm_current_pose.pose.orientation  

        waypoints.append(copy.deepcopy(waypoint1))

        target_pose = Pose()
        target_pose.position.x = block_pose.position.x
        target_pose.position.y = block_pose.position.y
        target_pose.position.z = block_pose.position.z
        target_pose.orientation = arm_current_pose.pose.orientation  

        waypoints.append(copy.deepcopy(target_pose))

        print("target pose")
        print(target_pose)
        (plan, fraction) = self.arm.compute_cartesian_path(waypoints, 0.005, 0.0)  # waypoints to follow  # eef_step
        self.arm.execute(plan, wait=True)

    def Move_to_initial_position(self):
        for i in range(5):
            self.arm.set_goal_tolerance(0.01)
            self.arm.set_named_target("ready")
            self.arm.go()

def block_pose_callback(data):
    global block_pose
    block_pose = data

rospy.init_node('controller')
rospy.Subscriber("/block_pose", Pose, block_pose_callback)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GUI()
    window.show()
    sys.exit(app.exec_())
