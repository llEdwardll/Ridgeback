#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

def callback(dist):
  twist = Twist()
  front = dist.ranges[180]
  left = dist.ranges[359]
  right = dist.ranges[0]
  	
  if front > 1.0:
    twist.linear.x=0.5
    twist.angular.z=0.0
  else:
    twist.linear.x=0.0
    twist.angular.z=0.5
  if right < 1.0:
    twist.linear.x=0.0
    twist.angular.z=0.5
  if left < 1.0:
    twist.linear.x=0.0
    twist.angular.z=-0.5
	
  pub.publish(twist)
  
  	

rospy.init_node('test')
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()

