#This file creates the node class and creates all the node objects which will be used in the graph

class node:
    # Node object to store each node's name and location (coordinates)
    def __init__(self ,nodename, location):
        self.nodename = nodename
        self.location = location
        self.prev = ''



global nodelist
nodelist = []
nodeA = node("A", (100 ,200))
nodeB = node("B" ,(350 ,100))
nodeC = node("C", (225 ,300))
nodeD = node("D", (100 ,450))
nodeE = node("E", (250, 575))
nodeF = node("F", (550, 500))
nodeG = node("G", (750, 475))
nodeH = node("H", (700, 350))
nodeI = node("I", (575, 225))
nodeJ = node("J", (1000, 50))
nodeK = node("K", (550, 350))
nodeL = node("L", (900, 300))
nodeM = node("M", (850, 600))
nodeN = node("N", (1050, 450))
nodeO = node("O", (950, 700))
nodeP = node("P", (600, 725))

nodelist.append(nodeA)
nodelist.append(nodeB)
nodelist.append(nodeC)
nodelist.append(nodeD)
nodelist.append(nodeE)
nodelist.append(nodeF)
nodelist.append(nodeG)
nodelist.append(nodeH)
nodelist.append(nodeI)
nodelist.append(nodeJ)
nodelist.append(nodeK)
nodelist.append(nodeL)
nodelist.append(nodeM)
nodelist.append(nodeN)
nodelist.append(nodeO)
nodelist.append(nodeP)
