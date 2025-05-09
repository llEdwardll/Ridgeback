#! /usr/bin/env python

import rospy
from test2_rbt.srv import CustomServMess, CustomServMessResponse
from square_service_pkg.srv import Square, SquareResponse
from geometry_msgs.msg import Twist


def my_callback(request):

rospy.init_node('service_move_ridgeback_custom_server') 
 
 my_service = rospy.Service('/move_tb3_custom', CustomServMess, my_callback)
 my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
 move_square = Twist()
 rospy.loginfo("Service /move_tb3_custom Ready")
 rospy.spin()


 rospy.loginfo("Service move_ridgeback_custom")
 move_square.linear.x = 0.2
 move_square.linear.y = 0.2
    i = 0
    while i <= request.duration: 
        my_pub.publish(move_square)
        rate.sleep()
        i=i+1 
    move_sqaure.linear.x = 0
    move_square.linear.y = 0
    my_pub.publish(move_circle)
    rospy.loginfo("Finished service move_ridgeback_custom")
    response = CustomServMessResponse()
    response.success = True
   
    return EmptyResponse()  
