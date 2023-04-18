#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtle_follow.msg import show_vel

def callback(msg):
    global pub
    velocity = show_vel()
    velocity.robot_name = "Universe"
    velocity.linear_vel_x=msg.linear.x
    velocity.angular_vel_z=msg.angular.z
    pub.publish(velocity)
    print(velocity)
    
def vel():
    global pub
    rospy.init_node("show_vel")
    rospy.Subscriber("/turtle1/cmd_vel",Twist,callback)
    pub = rospy.Publisher("custom_topic",show_vel,queue_size=10)
    rospy.spin()

if __name__=='__main__':
    try:
        vel()    
    except rospy.ROSInterruptException:
        pass