import math
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon, LineString
import shapely.affinity

from Node import Node
from Person import Person
from A_star import a_star

from time import time

from CalculateWeight import calculateWeight
from A_star import checkValidPath

def main():
    # with open('test.txt','w') as file:
    #     file.write("==================\n")
        
    start = Node(position=[0,27])

    end = Node(position=[150,150])

    kevin = Person(x=30,y=50,velocity=0,direction=0)
    john = Person(x=10,y=90,velocity=0,direction=0)
    sam = Person(x=80,y=20,velocity=0,direction=0)
    mike = Person(x=10,y=-20,velocity=0,direction=0)
    
    adjacencyList, listOfShape = createAdjacencyList_new( nodes =[start,end], people=[kevin,john])
             
    for i,j in adjacencyList.items():
        i.cost += calculateWeight(end,i)
    
    # plotAllPath(adjacencyList, listOfShape)
    
    listOfPath = a_star( start, end ,adjacencyList, listOfShape)
    return listOfPath

def createAdjacencyList_new(nodes, people):
    listOfShape = []
    
    for p in people : 
        nodes.extend(p.getKeyNodes())
        p.makeSocialZone()
        for circle in p.listOfCicle:
            listOfShape.append(circle)
            for node in circle:
                nodes.append(node)
    
    # for o in obstacles:
    #     listOfShape.append(obstacles.makeSocialZone)
        
    adjacencyList = {}
    for i in nodes:
        adjacencyList[i] = []
        for j in nodes :
            if ( i!=j ):
                adjacencyList[i].append(j)
    
    return adjacencyList, listOfShape



