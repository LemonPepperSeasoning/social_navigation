
def calculateWeight(x,y):
    return ( (x.position[0]-y.position[0])**2+(x.position[1]-y.position[1])**2 ) *0.001

def calculateWeight(x,y):
    x1 = x.position[0] / 200
    x2 = x.position[1] / 200
    y1 = y.position[0] / 200
    y2 = y.position[1] / 200

    return ( (x1-y1)**2+(x2-y2)**2 ) **4 *0.001