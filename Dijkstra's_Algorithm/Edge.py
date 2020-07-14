#This file creates the edge class and creates all the edges between the nodes

import Node
import math



# Creates an edge object between two nodes and calculates the distance between them
class edge:

    def __init__(self, n1, n2):
        self.nodename1 = n1
        self.nodename2 = n2
        self.dist = self.getDist()

    def getDist(self):
        for i in Node.nodelist:
            if (i.nodename == self.nodename1):
                nodeobj1 = i
            if (i.nodename == self.nodename2):
                nodeobj2 = i
        return (math.hypot(nodeobj1.location[0] - nodeobj2.location[0], nodeobj1.location[1] - nodeobj2.location[1]))/10


global edgelist
edgelist = []
edgeAB = edge("A", "B")
edgeAC = edge("A", "C")
edgeAD = edge("A", "D")
edgeBI = edge("B", "I")
edgeBJ = edge("B", "J")
edgeCI = edge("C", "I")
edgeCK = edge("C", "K")
edgeDE = edge("D", "E")
edgeEF = edge("E", "F")
edgeFK = edge("F", "K")
edgeFG = edge("F", "G")
edgeGH = edge("G", "H")
edgeHI = edge("H", "I")
edgeHJ = edge("H", "J")
edgeHL = edge("H", "L")
edgeLM = edge("L", "M")
edgeMF = edge("M", "F")
edgeMN = edge("M", "N")
edgeNO = edge("N", "O")
edgeOE = edge("O", "E")
edgeOP = edge("O", "P")
edgePE = edge("P", "E")
edgeGL = edge("G", "L")
edgeNJ = edge("N", "J")
edgeDK = edge("D", "K")



edgelist.append(edgeAB)
edgelist.append(edgeAC)
edgelist.append(edgeAD)
edgelist.append(edgeBI)
edgelist.append(edgeBJ)
edgelist.append(edgeCI)
edgelist.append(edgeCK)
edgelist.append(edgeDE)
edgelist.append(edgeEF)
edgelist.append(edgeFK)
edgelist.append(edgeFG)
edgelist.append(edgeGH)
edgelist.append(edgeHI)
edgelist.append(edgeHJ)
edgelist.append(edgeHL)
edgelist.append(edgeLM)
edgelist.append(edgeMF)
edgelist.append(edgeMN)
edgelist.append(edgeNO)
edgelist.append(edgeOE)
edgelist.append(edgeOP)
edgelist.append(edgePE)
edgelist.append(edgeGL)
edgelist.append(edgeNJ)
edgelist.append(edgeDK)

