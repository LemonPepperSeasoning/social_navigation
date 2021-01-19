from shapely.geometry import Point, Polygon, LineString
from Node import Node
import shapely.affinity

class Person:
    def __init__(self, x,y, velocity,direction):
        self.x = x
        self.y = y
        self.velocity= velocity
        self.direction = direction
        
        
    def makeSocialZone(self):
        self.listOfCicle = []
        nodes = []
        
        circle = Point(self.x, self.y).buffer(1)  # type(circle)=polygon
        
        layer1Weight = 300
        count = 0
        layer1 = shapely.affinity.scale(circle, 10, 10)# type(ellipse)=polygo
        for i,j in list(layer1.exterior.coords):
            if (count % 4 == 0):
                nodes.append(Node(position=[i,j], nodeCost= layer1Weight))
            count += 1
        self.listOfCicle.append(nodes)
        
        nodes1 = []
        
        layer2Weight = 200
        count = 0
        layer2 = shapely.affinity.scale(circle, 20, 20)
        for i,j in list(layer2.exterior.coords):
            if (count % 4 == 0):
                nodes1.append(Node(position=[i,j], nodeCost= layer2Weight))
            count += 1
        self.listOfCicle.append(nodes1)
        
        nodes2 = []
        
        layer3Weight = 100
        count = 0
        layer3 = shapely.affinity.scale(circle, 30, 30)
        for i,j in list(layer3.exterior.coords):
            if (count % 4 == 0):
                nodes2.append(Node(position=[i,j], nodeCost= layer3Weight))
            count += 1
        self.listOfCicle.append(nodes2)
        
        
    def getKeyNodes(self):
        circle = Point(self.x, self.y).buffer(1)  # type(circle)=polygon
        
        nodes = []
        count = 0
        outerCircle = shapely.affinity.scale(circle, 32, 32)
        for i,j in list(outerCircle.exterior.coords):
            if (count % 4 == 0):
                nodes.append(Node(position=[i,j], nodeCost= 0))
            count += 1
        return nodes
    