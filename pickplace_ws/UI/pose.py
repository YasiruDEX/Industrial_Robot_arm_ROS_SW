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

arm = moveit_commander.MoveGroupCommander("arm")
arm.set_goal_tolerance(0.01)
arm.set_named_target("ready")
arm.go()

def block_pose_callback(data):
    global block_pose
    block_pose = data
    

rospy.init_node('controller')
rospy.Subscriber("/block_pose", Pose, block_pose_callback)

while True:
    print(block_pose)
