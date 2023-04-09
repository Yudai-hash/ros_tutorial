#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def callback(message):
    print(message.data)

#Pythonのプログラムでは、インポートされた場合、関数を自動で実行するが、
#if文内で書いた関数は自動で実行されなくなる
if __name__ == "__main__":
    rospy.init_node('time_sub')
    sub = rospy.Subscriber('UnixTime', Float64 , callback)
    rospy.spin()