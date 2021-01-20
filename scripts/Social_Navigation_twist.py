#!/usr/bin/env python

from __future__ import print_function

import threading

import roslib; roslib.load_manifest('social_navigation')
import rospy

from geometry_msgs.msg import Twist

#from Main import main

import math
import sys, select, termios, tty


moveBindings = {
        'i':(1,0,0,0),
        'o':(1,0,0,-1),
        'j':(0,0,0,1),
        'l':(0,0,0,-1),
        'u':(1,0,0,1),
        ',':(-1,0,0,0),
        '.':(-1,0,0,1),
        'm':(-1,0,0,-1),
        'O':(1,-1,0,0),
        'I':(1,0,0,0),
        'J':(0,1,0,0),
        'L':(0,-1,0,0),
        'U':(1,1,0,0),
        '<':(-1,0,0,0),
        '>':(-1,-1,0,0),
        'M':(-1,1,0,0),
        't':(0,0,1,0),
        'b':(0,0,-1,0),
    }

speedBindings={
        'q':(1.1,1.1),
        'z':(.9,.9),
        'w':(1.1,1),
        'x':(.9,1),
        'e':(1,1.1),
        'c':(1,.9),
    }

class PublishThread(threading.Thread):
    def __init__(self, rate):
        super(PublishThread, self).__init__()
        self.publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 1)
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0
        self.th = 0.0
        self.speed = 0.0
        self.turn = 0.0
        self.condition = threading.Condition()
        self.done = False

        # Set timeout to None if rate is 0 (causes new_message to wait forever
        # for new data to publish)
        if rate != 0.0:
            self.timeout = 1.0 / rate
        else:
            self.timeout = None

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

    def update(self, x, y, z, th, speed, turn):
        self.condition.acquire()
        self.x = x
        self.y = y
        self.z = z
        self.th = th
        self.speed = speed
        self.turn = turn
        # Notify publish thread that we have a new message.
        self.condition.notify()
        self.condition.release()

    def stop(self):
        self.done = True
        self.update(0, 0, 0, 0, 0, 0)
        self.join()

    def run(self):
        twist = Twist()
        while not self.done:
            self.condition.acquire()
            # Wait for a new message or timeout.
            self.condition.wait(self.timeout)

            # Copy state into twist message.
            twist.linear.x = self.x * self.speed
            twist.linear.y = self.y * self.speed
            twist.linear.z = self.z * self.speed
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = self.th * self.turn

            self.condition.release()

            # Publish.
            self.publisher.publish(twist)

        # Publish stop message when thread exits.
        twist.linear.x = 0
        twist.linear.y = 0
        twist.linear.z = 0
        twist.angular.x = 0
        twist.angular.y = 0
        twist.angular.z = 0
        self.publisher.publish(twist)


def vels(speed, turn):
    return "currently:\tspeed %s\tturn %s " % (speed,turn)

def angle3pt(a, b, c):
    ab = math.sqrt( ( a[0] - b[0] )**2 + ( a[1] - b[1] )**2 )
    bc = math.sqrt( ( c[0] - b[0] )**2 + ( c[1] - b[1] )**2 )
    ac = math.sqrt( ( c[0] - a[0] )**2 + ( c[1] - a[1] )**2 )

    if (ab**2 + bc**2 - ac**2 == 0):
        return 0

    x = (ab**2 + bc**2 - ac**2 ) / ( 2*bc*ab )
    angle = math.acos( x )
    return 180 - round( angle*(180/math.pi) )

# x , y, z are all nodes with x.position[] = [ x_coordinate, y_coordinate]
# x : previus node
# y : current node
# z : destination node
def move(x,y,z,speed,turn,rate,pub_thread):
    print ("moving")
    angle = angle3pt(x,y,z)

    count_Rotation = abs(angle)/5.1

    distance = ( z[0] - y[0] )**2 + ( z[1] - y[1] )**2

    count_Distance = distance

    print ("Rotation :{}, Distance : {}".format(count_Rotation,count_Distance))
    counter = 0
    while count_Rotation > counter :
        counter += 1
        pub_thread.update(0, 0, 0, -1, speed, turn)
        rate.sleep()

    pub_thread.update(0,0,0,0,speed,turn)

    counter = 0
    while count_Distance > counter :
        counter += 1
        pub_thread.update(1, 0, 0, 0, speed, turn)
        rate.sleep()
    pub_thread.update(0,0,0,0,speed,turn)


if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('social_navigation')

    speed = rospy.get_param("~speed", 0.5)
    turn = rospy.get_param("~turn", 1.0)
    repeat = rospy.get_param("~repeat_rate", 0.0)
    key_timeout = rospy.get_param("~key_timeout", 0.0)
    if key_timeout == 0.0:
        key_timeout = None

    pub_thread = PublishThread(repeat)

    x = 0
    y = 0
    z = 0
    th = 0
    status = 0

    #listOfPath = main()
    p1 = [0,0]
    p2 = [0,5]
    p3 = [5,5]
    p4 = [5,0]
    listOfPath = [p1,p2,p3,p4]
    rate = rospy.Rate(10)

    loop = True
    try:
        pub_thread.wait_for_subscribers()
        pub_thread.update(x, y, z, th, speed, turn)

        print(vels(speed,turn))

        count = 0

        move([0,-1],listOfPath[0],listOfPath[1],speed,turn,rate,pub_thread)

        #move(listOfPath[0],listOfPath[1],listOfPath[2],speed,turn,rate,pub_thread)


        for i in range(1, len(listOfPath)-1):
            print ("moving from {} to {} to {}".format(listOfPath[i-1],listOfPath[i],listOfPath[i+1]))
            move(listOfPath[i-1],listOfPath[i],listOfPath[i+1],speed,turn,rate,pub_thread)

        move(listOfPath[2],listOfPath[3],[0,0],speed,turn,rate,pub_thread)
        pub_thread.update(0, 0, 0, 0, 0, 0)



    except Exception as e:
        print(e)

    finally:
        pub_thread.stop()

        #termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
