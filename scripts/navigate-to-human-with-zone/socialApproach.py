#!/usr/bin/env python
import rospy
import rospkg

if __name__ == "__main__" :
    rospy.init_node('socialApproach')

    rospy.Subscriber("/tone_w/where" , MultiPersons, queue_size=1)
    rospy.Subscriber("/tone_w/where" , MultiPersons, queue_size=1)
    rospy.Subscriber("/tone_w/where" , MultiPersons, queue_size=1)
    rospy.Subscriber("/tone_w/where" , MultiPersons, queue_size=1)

    Direction = "NORTH"
    
    