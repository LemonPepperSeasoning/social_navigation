#!/usr/bin/env python

# This module is to conduct data association with the human_roi detected from where position detection module(psn_unit)


""""This is where fusion module."""
import sys, os, time
import rospy
import rospkg
from math import *
import math
from cv_bridge import CvBridge, CvBridgeError
from decimal import Decimal # so i can round numbers

from simonpic_msgs.msg import Person, MultiPersons

import sys, cv2
from scipy.spatial import distance
from threading import Lock

human_mutex = Lock()
human_mutex_rcnn = Lock()
fusion_mutex = Lock()

publish_score_TH = 30.
vel_max = 0.
realsense_offset = 0.423

def callback(data):
    rospy.loginfo("HEADER :  %s",data.header)
    rospy.loginfo("TOTAL :  %s",data.total)
    rospy.loginfo("PERSON :  %s",data.person)

    for i in range(0, data.total):
        rospy.loginfo("LOOP : {}".format(i))


if __name__ == '__main__':
    rospy.init_node('test_listener')
    rospy.Subscriber("/tone_w/where" , MultiPersons, queue_size=1)
    
    try:
        rospy.spin()
    except rospy.ROSInterruptException:
        pass