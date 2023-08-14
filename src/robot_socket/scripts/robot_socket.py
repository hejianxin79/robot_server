#! /usr/bin/env python

"""
    Python 版 HelloWorld

"""
import rospy

if __name__ == "__main__":
    rospy.init_node("robot_socket")
    rospy.loginfo("机器人socket通信服务")
