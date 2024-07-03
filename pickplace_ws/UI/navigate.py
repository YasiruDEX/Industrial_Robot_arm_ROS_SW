import rospy
from geometry_msgs.msg import Pose
import moveit_commander
import sys
import random

class SimpleMover:
    def __init__(self):
        # Initialize the moveit_commander
        moveit_commander.roscpp_initialize(sys.argv)
        rospy.init_node('simple_mover', anonymous=True)

        # Instantiate a `MoveGroupCommander` for the arm
        self.arm = moveit_commander.MoveGroupCommander("arm")

        # Set the reference frame for pose targets
        self.arm.set_pose_reference_frame("base_link")

        # Allow replanning to increase the odds of a solution
        self.arm.allow_replanning(True)

        # Set the goal position and orientation tolerances
        self.arm.set_goal_position_tolerance(0.05)
        self.arm.set_goal_orientation_tolerance(0.05)

        # Increase the planning time
        self.arm.set_planning_time(4)

    def move_to_pose(self, x, y, z, ox=0, oy=0, oz=0, ow=1):
        # Define the target pose
        target_pose = Pose()
        target_pose.position.x = x
        target_pose.position.y = y
        target_pose.position.z = z
        target_pose.orientation.x = ox
        target_pose.orientation.y = oy
        target_pose.orientation.z = oz
        target_pose.orientation.w = ow

        # Set the target pose for the arm
        self.arm.set_pose_target(target_pose)

        # Plan and execute the motion
        plan = self.arm.go(wait=True)

        if not plan:
            print("Planning failed")
            print("Current pose:", self.arm.get_current_pose().pose)
            print("Target pose:", target_pose)

        # Clear the target pose
        self.arm.stop()
        self.arm.clear_pose_targets()

        # Return whether the plan was successful
        return plan

    def move_to_random_poses(self, bound_x, bound_y, bound_z):
        #while not rospy.is_shutdown():
        x = random.uniform(-bound_x, bound_x)
        y = random.uniform(-bound_y, bound_y)
        z = random.uniform(0, bound_z)  # Assuming the z-axis is vertical

        print(f"Trying to move to random position: x={x}, y={y}, z={z}")

        if self.move_to_pose(0.5,0,0.4,0,1,0,0):
            print("Moved to the target location successfully!")
        else:
            print("Failed to move to the target location.")

if __name__ == '__main__':
    # Initialize the SimpleMover class
    simple_mover = SimpleMover()

    # Define the bounds for random points
    bound_x = 0.7
    bound_y = 0.7
    bound_z = 1

    # Move to random points within the specified bounds
    simple_mover.move_to_random_poses(bound_x, bound_y, bound_z)

    # Shut down the moveit_commander
    moveit_commander.roscpp_shutdown()
    rospy.signal_shutdown("Done")

