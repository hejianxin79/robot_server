#! /usr/bin/env python

"""
    Python 版 HelloWorld

"""
import rospy

if __name__ == "__main__":
    rospy.init_node("robot_heartbeat")
    rospy.loginfo("机器人心跳功能")
