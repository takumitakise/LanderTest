#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback_scan(msg):
	print(msg.ranges[0])

if __name__ == '__main__':
    rospy.init_node('scan_values')
    rate = rospy.Rate(1/1000) 
    
    while not rospy.is_shutdown():     
        rospy.Subscriber('/scan', LaserScan, callback_scan)
        rate.sleep()
