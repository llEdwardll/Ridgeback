#!/usr/bin/env python

import rospy
import actionlib
from drone_control.msg import DroneControlAction, DroneControlFeedback, DroneControlResult

class DroneActionServer:
    def _init_(self):
        self.server = actionlib.SimpleActionServer('drone_action', DroneControlAction, self.execute, False)
        self.feedback = DroneControlFeedback()
        self.result = DroneControlResult()
        self.server.start()

    def execute(self, goal):
        rospy.loginfo("Received command: ", goal.command)
        r = rospy.Rate(1)  # 1 Hz

        if goal.command == "TAKEOFF":
            rospy.loginfo("Taking off")
            while not rospy.is_shutdown() and not self.server.is_preempt_requested():
                self.feedback.status = "Taking off"
                self.server.publish_feedback(self.feedback)
                r.sleep()
        elif goal.command == "LAND":
            rospy.loginfo("Landing")
            for _ in range(5):  # simulate landing time
                self.feedback.status = "Landing"
                self.server.publish_feedback(self.feedback)
                r.sleep()

        self.server.set_succeeded(self.result)

if _name_ == '_main_':
    rospy.init_node('drone_action_server')
    server = DroneActionServer()
    rospy.spin()
