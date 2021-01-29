#!/usr/bin/env python
import threading

import roslib; roslib.load_manifest('social_navigation')
import rospy

from geometry_msgs.msg import PoseStamped

import math
import sys, select, termios, tty

class PublishThread(threading.Thread):
    def __init__(self):
        super(PublishThread, self).__init__()
        self.publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size = 10)
        self.goalId = 1
        self.goalMsg = PoseStamped()
        self.goalMsg.header.frame_id = "/map"
        self.goalMsg.header.stamp = rospy.Time.now()

        self.goalMsg.pose.position.x = 2.5
        self.goalMsg.pose.position.y = 4
        self.goalMsg.pose.position.z = 0.0

        self.goalMsg.pose.orientation.x = 0
        self.goalMsg.pose.orientation.y = 0
        self.goalMsg.pose.orientation.z = 0.0
        self.goalMsg.pose.orientation.w = 1.0

        self.condition = threading.Condition()
        self.done = False
        self.goalId += 1
        self.start()

    def wait_for_subscribers(self):
        i = 0
        while not rospy.is_shutdown() and self.publisher.get_num_connections() == 0:
            if i == 4:
                print("Waiting for subscriber to connect to {}".format(self.publisher.name))
            rospy.sleep(0.5)
            i += 1
            i = i % 5
        if rospy.is_shutdown():
            raise Exception("Got shutdown request before subscribers connected")

    def startPublish(self):
        self.publisher.publish(self.goalMsg)
        rospy.loginfo("Initial goal published! Goal ID is: %d", self.goalId)

    # def update(self, x, y, z, ori_x, ori_y, ori_z):
    #     self.condition.acquire()
    #     self.x = x
    #     self.y = y
    #     self.z = z
    #     self.ori_x = ori_x
    #     self.ori_y = ori_y
    #     self.ori_z = ori_z
    #     # Notify publish thread that we have a new message.
    #     self.condition.notify()
    #     self.condition.release()

    # def stop(self):
    #     self.done = True
    #     self.update(0, 0, 0, 0, 0, 0)
    #     self.join()

    # def run(self):
    #     pose = PoseStamped()
    #     pose.linear.x = self.x
    #     pose.linear.y = self.y
    #     pose.linear.z = self.z
    #     pose.orientation.x = 0
    #     pose.orientation.y = 0
    #     pose.orientation.z = self.ori_z

    #     self.condition.release()
    #     # Publish.
    #     self.publisher.publish(pose)


if __name__=="__main__":
    print ("starting")
    rospy.init_node('social_navigation')
    pub_thread = PublishThread()

    #msg = Path()
    # msg.header.frame_id = "/map"
    # msg.header.stamp = rospy.Time.now()

    # pose = PoseStamped()
    # pose.pose.position.x = 0
    # pose.pose.position.y = 0
    # pose.pose.position.z = 0

    # pose.pose.orientation.x = 0
    # pose.pose.orientation.y = 0
    # pose.pose.orientation.w = 0
    # msg.poses.append(pose)


    try:
        print ("trying")
        pub_thread.wait_for_subscribers()
        pub_thread.startPublish()
        print ("finished")
    except Exception as e:
        print(e)
