import math
import matplotlib.pyplot as plt

import numpy as np

def robot_to_camera(rx, ry):
    R = [rx, ry]
    A = math.sqrt(R[0]**2 + R[1]**2) / ratio
    alpha = math.atan(R[1] / R[0])

    add_x = math.cos(diff_degree + alpha) * A
    add_y = math.sin(diff_degree + alpha) * A

    c_x = p0[0] - add_x
    c_y = p0[1] + add_y
    print("ROBOT : {}, {}".format(c_x, c_y))
    return c_x, c_y


def camera_to_robot(cx, cy, ratio, diff_degree):
    C = [cx, cy]
    add_x = p0[0] - C[0]
    add_y = C[1] - p0[1]

    r_distance = math.sqrt(add_x ** 2 + add_y ** 2) * ratio

    alpha = math.atan(add_y / add_x)

    theata = alpha - diff_degree

    r_x = math.cos(theata) * r_distance
    r_y = math.sin(theata) * r_distance
    print("CAMERA : {}, {}".format(r_x, r_y))
    return r_x, r_y


def plot():
    x_values = []
    y_values = []
    for i in range(0, 10):
        x_values.append(0)
        y_values.append(i)
        x_values.append(i)
        y_values.append(0)
    for i in range(1, 5):
        x, y = robot_to_camera(i, i)
        x_values.append(x)
        y_values.append(y)
    plt.scatter(x_values, y_values, s=5)
    plt.show()



def getParam(x,y):
    p0 = [0.23, 2.94]
    p1 = [-0.27, 3.52]
    q1 = [1, 1]
    # p2 = [-0.96,4.4]
    # q2 = [2,2]
    p3 = [-1.16, 6.64]
    q3 = [ 2.5 , 4]
    x = abs(p1[1]-p0[1])
    y = abs(p1[0]-p0[0])
    
    total_degree = math.atan(x / y)

    in_degree = math.atan(q1[1]/q1[0])
   
    diff_degree = total_degree - in_degree
 

    ratio = math.sqrt(q1[0]**2 + q1[1]**2) / math.sqrt(x**2 + y ** 2)
    
    C = [x, y]
    add_x = p0[0] - C[0]
    add_y = C[1] - p0[1]

    r_distance = math.sqrt(add_x ** 2 + add_y ** 2) * ratio

    alpha = math.atan(add_y / add_x)

    theata = alpha - diff_degree

    r_x = math.cos(theata) * r_distance
    r_y = math.sin(theata) * r_distance

    return r_x,r_y
