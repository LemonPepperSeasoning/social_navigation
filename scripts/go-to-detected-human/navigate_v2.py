#! /usr/bin/env python

import rospy # the ROS api for python. We need it to create a node, 
             # a subscriber and access other ROS-specific program control
from body_tracker_msgs.msg import BodyTrackerArray # Python message class for Odometry
from geometry_msgs.msg import PoseStamped
from coordinateConverter import getParam

from simonpic_msgs.msg import Person, MultiPersons

class PublishThread():
	def __init__(self):
        	
                self.publisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size = 10)
                self.goalId = 1
           	self.goalMsg = PoseStamped()
           	self.goalMsg.header.frame_id = "/map"
           	self.goalMsg.header.stamp = rospy.Time.now()
   
           	self.goalMsg.pose.position.x = 0.0
           	self.goalMsg.pose.position.y = 0.0
           	self.goalMsg.pose.position.z = 0.0
   
           	self.goalMsg.pose.orientation.x = 0.0
           	self.goalMsg.pose.orientation.y = 0.0
           	self.goalMsg.pose.orientation.z = 0.0
           	self.goalMsg.pose.orientation.w = 1.0





def callback(msg):
	detected_person = msg.persons
	#position2d = detected_list.position2d
        if not detected_person:
		print("no person detected")
	else:	
		print("detected !")
		pub_thread = PublishThread()
                x_value = detected_person[0].location.x
		z_value = detected_person[0].location.z
                converted_x, converted_z = getParam(x_value, z_value)
               
        	pub_thread.goalMsg.pose.position.x = converted_x
		print ("x: {}, y : {}".format(x_value,z_value))
        	
        	pub_thread.goalMsg.pose.position.y = converted_z
                
        	pub_thread.publisher.publish(pub_thread.goalMsg)
		#rospy.loginfo("Initial goal published! Goal ID is: %d", 1)


    
    
    	#pub = rospy.Publisher('move_base_simple/goal geometry_msgs)

if __name__ == "__main__":

	rospy.init_node("navigate_v2")
	print("initialize")
	#sub = rospy.Subscriber('/tone_w/where', MultiPersons, callback)
	#msg = rospy.wait_for_message("/body_tracker_array/position", BodyTrackerArray)
	r = rospy.Rate(0.05) # 10hz

	while not rospy.is_shutdown():
		try:
    			msg = rospy.wait_for_message("/tone_w/where", MultiPersons, timeout=5)
			callback(msg)
		except:
			pass
    		r.sleep()




