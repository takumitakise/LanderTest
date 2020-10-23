#!/usr/bin/env python
import rospy 
from rospy import Time
from nav_msgs.msg import Odometry   
import tf
from tf import TransformBroadcaster

def callback_odom(msg):
    _odom_x = msg.pose.pose.position.x  
    _odom_y = msg.pose.pose.position.y  
    _odom_z = msg.pose.pose.position.z
    qx = msg.pose.pose.orientation.x
    qy = msg.pose.pose.orientation.y
    qz = msg.pose.pose.orientation.z
    qw = msg.pose.pose.orientation.w
    translation = (_odom_x, _odom_y, _odom_z)
    rotation = (qx, qy, qz, qw)
    b = TransformBroadcaster()
    b.sendTransform(translation, rotation, Time.now(), 'base_link', 'world')
   
if __name__ == '__main__':
    rospy.init_node('odometry')
    rate = rospy.Rate(1/1000) 
    
    while not rospy.is_shutdown():     
        rospy.Subscriber('/odom', Odometry, callback_odom)
        rate.sleep()
        
