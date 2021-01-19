from CalculateWeight import calculateWeight

class Edge:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        self.weight = self.getWeight(start,end)
        
    def getWeight(self,x,y):
        weight = calculateWeight(x,y)
        return weight+x.totalWeight+y.cost
    
        
    
    
        