#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

import math

x=0
y=0
yaw=0

def poseCallback1(pose_message):
    global a
    global b
    a = pose_message.x
    b = pose_message.y
    yaw = pose_message.theta
    go_to_goal(a,b)

def poseCallback2(pose_message):
    global x
    global y, yaw
    x = pose_message.x
    y = pose_message.y
    yaw = pose_message.theta

def go_to_goal(x_goal, y_goal):
    global x
    global y, yaw

    velocity_message = Twist()
        
    while(True):
        k_linear=0.5
        distance=abs(math.sqrt(((x_goal-x)**2)+((y_goal-y)**2)))

        linear_speed = distance * k_linear

        k_angular = 4.0
        desired_angle_goal = math.atan2(y_goal-y, x_goal-x)
        angular_speed = (desired_angle_goal-yaw)*k_angular

        velocity_message.linear.x = linear_speed
        velocity_message.angular.z = angular_speed

        velocity_publisher.publish(velocity_message)

        if (distance<0.9):
                break

if __name__=='__main__':
    try:
        rospy.init_node('turtlesim_motion_pose',anonymous=True)

        velocity_publisher=rospy.Publisher("/turtle2/cmd_vel",Twist,queue_size=10)
        rospy.Subscriber("/turtle2/pose",Pose,poseCallback2)
        rospy.Subscriber("/turtle1/pose",Pose,poseCallback1)
        #rospy.sleep(1)

        
        rospy.spin()
        

    except rospy.ROSInterruptException:
         rospy.loginfo("node terminated")




        
