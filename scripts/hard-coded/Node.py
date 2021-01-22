import math
from CalculateWeight import calculateWeight

class Node:
    def __init__(self, parent=None, position=None, nodeCost=0):
        self.parent = parent
        self.position = position
        
        #Current weight in the stack, could be fine setting it to be infinity at the begging
        self.totalWeight = 100000.0

        #The heustic + social zone cost
        self.cost = nodeCost

    def __hash__(self):
        return hash((self.position[0],self.position[1]))
    
    # if weight does get updated return TRUE
    # else return false
    '''
    def updateWeight(self, parent):
        # When this is called, we also need to update the stack. 
        # (update the order.)
        
        weight = ( (parent.position[0]-self.position[0])**2+(parent.position[1]- self.position[1])**2)*0.001
        
        if ( parent.totalWeight + self.cost + weight < self.totalWeight ):
            self.parent = parent
            self.totalWeight = parent.totalWeight + self.cost + weight
            return True
        return False
    '''
    def updateWeight(self, parent):
        # When this is called, we also need to update the stack. 
        # (update the order.)
        
        weight = calculateWeight(parent,self)
        self.totalWeight = parent.totalWeight + self.cost + weight
        return

    