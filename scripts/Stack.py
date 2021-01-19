
class Stack:
    def __init__(self):
        self.list = []
        
    def pushNode(self, node):
        #Currently this is normal forloop. 
        #Its fine for small list but for scalability, might be better to do binary search to find insertion index.
        for i in range(0,len(self.list)):
            if ( node.totalWeight < self.list[i].totalWeight ):
                self.list.insert(i,node)
                return
        self.list.append(node)
            
    def pushEdge(self, Edge):
        #Currently this is normal forloop. 
        #Its fine for small list but for scalability, might be better to do binary search to find insertion index.
        for i in range(0,len(self.list)):
            if ( Edge.weight < self.list[i].weight ):
                self.list.insert(i,Edge)
                return
        self.list.append(Edge)
        
    def push_v2(self,Edge): 
        l = 0
        r = len(self.list)-1
        while l<=r:

            mid = l + (r-l) // 2;
            if self.list[mid].weight < Edge.weight:
                l = mid + 1
            elif self.list[mid].weight >= Edge.weight:
                r = mid - 1
                
        self.list.insert(r+1, Edge)
        
    def pop(self):
        return self.list.pop(0)
        
    # def print(self):
    #     # print("stack.print() is called")
    #     with open('test.txt','a') as file:
    #         file.write("==================\n")
    #         for i in self.list:
    #             file.write("__pos : {} ~ {}, weight : {} ".format(i.start.position,i.end.position,i.weight))
    #         file.write("\n")
    
    def print(self):
        # print("stack.print() is called")
        with open('test.txt','a') as file:
            file.write("==================\n")
            for i in self.list:
                file.write("__pos : {} ~ {}, weight : {} ".format(i.start.position,i.end.position,i.weight))
                file.write("\n")

