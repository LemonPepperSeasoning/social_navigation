from Stack import Stack
from shapely.geometry import Point, Polygon, LineString
from Edge import Edge

from myHelper import doIntersect

'''
need to add loop counter
If no path is found, this current version will run forever
'''
def a_star(start, goal, adjacencyList, listOfObstacle):
    visted = []
    
    notVisted = []
    for key,value in adjacencyList.items():
        notVisted.append(key)
            
    stack = Stack()
    
    #This represents the node that was last visted.
    start.totalWeight = 0
    justVisted = start
    
    foundGoal = False
    while (not foundGoal):
        # print (justVisted.position)
        if (justVisted.position == goal.position):
            foundGoal = True
            return returnPath(justVisted)
                 
        for i in adjacencyList[justVisted]:
            #check to see if the node is already in stack.
            # if yes update
            # if no push to stack with new weights.
            if ( i in visted ):
                continue
            if not (i in adjacencyList):
                continue
            
            # stack.pushEdge(Edge(justVisted,i))
            stack.push_v2( Edge(justVisted,i) )
        
        parent = justVisted
        visted.append(justVisted)
        
        # Use this to print out the stack, to see the weighting of each edge. 
        # stack.print()
        
        loop = True
        currentPath = stack.pop()
        while loop:
            if ( currentPath.end in visted):
                currentPath = stack.pop()
            elif not checkValidPath(currentPath.start,currentPath.end,listOfObstacle):
                currentPath = stack.pop()
            else:
                loop = False
        
        # print ("from : {} ~ {} ".format(currentPath.start.position,currentPath.end.position))
        justVisted = currentPath.end
        currentPath.end.parent = currentPath.start
        currentPath.end.updateWeight(currentPath.start)
        
        # print ("{}, {}  : {}".format(justVisted.position,parent.position, checkValidPath(parent,justVisted,listOfObstacle)) ) 
        
        # UNCOMMEND THIS LINE IF YOU JUST WANT TO SEE THE PATH
        # Having this next line will show the explored node.
        
        # justVisted.parent = parent

def returnPath(node):
    path = []
    current = node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path

def checkValidPath(x, y ,obstacles):
    doesNotCross = True
    for obstacle in obstacles:
        
        for i in range(0,len(obstacle)-1):
            if (doIntersect(x,y,obstacle[i],obstacle[i+1])):

            # if (checkIntersect(x,y,obstacle[i],obstacle[i+1])):
                return False       
    return True

# Line 1 = x1 to y1
# Line 2 = x2 to y2

# def checkIntersect ( x1, y1, x2, y2):

#     line1 = LineString([(x1.position[0],x1.position[1]),(y1.position[0],y1.position[1])])
#     line2 = LineString([(x2.position[0],x2.position[1]),(y2.position[0],y2.position[1])])
#     return (line1.intersects(line2))


# def checkIntersect_V2 ( x1, y1, x2, y2):
#     # y = a x + b
#     a1 = (x1.position[0] - y1.position[0]) / (x1.position[1] - y1.position[1])
#     b1 = x1.position[1] - a1 * x1.position[0]
    
#     a2 = (x2.position[0] - y2.position[0]) / (x2.position[1] - y2.position[1])
#     b2 = x2.position[1] - a2 * x2.position[0]
    
#     if (a1 == a2):
#         #Its parrarell
#         return False
    
