#!/usr/bin/env python
import rospy
import rospkg

from body_tracker_msgs.msg import BodytTracker
from message_filters import ApproximateTimeSynchronizer, Subscriber

def gotimage( input1, input2 , input3, input4):
    print ("INPUT : {}, {}, {}, {}".format(input1,input2,input3,input4))
    

if __name__ == "__main__" :
    rospy.init_node('socialApproach')    

    sub1 = Subscriber("/realsense1/body_tracker/position", BodytTracker)
    sub2 = Subscriber("/realsense2/body_tracker/position", BodytTracker)
    sub3 = Subscriber("/realsense3/body_tracker/position", BodytTracker)
    sub4 = Subscriber("/realsense4/body_tracker/position", BodytTracker)

    ats = ApproximateTimeSynchronizer([sub1, sub2, sub3, sub4], queue_size=5, slop=0.05)
    ats.registerCallback(gotimage)