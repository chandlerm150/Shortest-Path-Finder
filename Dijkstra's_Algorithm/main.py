import sys
import pygame
import math
from tkinter import *
from tkinter import messagebox
import Node
import Edge


def solver():
    #create a list of unvisited nodes
    unvisited = []
    for i in Node.nodelist:
        unvisited.append(i.nodename)

    #Initialize the distance to each node as infinity (99999 is effective in this case), update shortest distances at each iteration
    inf = 99999
    shortestDist = {}
    for i in unvisited:
        shortestDist.update({i : inf})

    currentNode = starting.capitalize()
    shortestDist[currentNode] = 0

    #Run until every node is visited, starting with starting node
    while len(unvisited) != 0:

        ##Examine closest nodes and update distance in shortestDist of each neighboring node if it is lower than the previous shortest distance for each node
        neighbors = getNeighbors(currentNode)
        for i in neighbors:
            if (neighbors[i] + shortestDist[currentNode] ) < shortestDist[i]:
                shortestDist[i] = neighbors[i] + shortestDist[currentNode]
                nodeobj = getNodeObject(i)
                nodeobj.prev = currentNode

        ##Remove current node from unvisited and then change current node to closest node
        unvisited.remove(currentNode)
        closest = None
        for i in unvisited:
            if closest == None:
                closest = i
            else:
                for j in shortestDist:
                    if shortestDist[j] < shortestDist[closest] and j in unvisited:
                        closest = j
        currentNode = closest

    nodeObj = getNodeObject(ending.capitalize())
    name = nodeObj.nodename

    #Create a list to keep track of shortest path. Start at ending node and add each node's previous node to the list until starting node is reached.
    shortestpath = []
    while name != starting.capitalize():
        shortestpath.append(name)
        name = getNodeObject(name).prev
    shortestpath.append(starting.capitalize())

    # Draw the shortest path on the screen
    totalDist = 0
    count = 0
    for j in shortestpath:
        if count <= len(shortestpath)-2:
            node1 = getNodeObject(j)
            node2 = getNodeObject(shortestpath[count + 1])
            totalDist += (math.hypot(node1.location[0] - node2.location[0], node1.location[1] - node2.location[1])) / 10
            line = pygame.draw.line(screen, visitedColor, (node1.location[0], node1.location[1]),(node2.location[0], node2.location[1]), 5)
        count +=1
        pygame.display.update()

    for i in shortestpath:
        ci = pygame.draw.circle(screen, visitedColor, (getNodeObject(i).location[0], getNodeObject(i).location[1]), 35)
        theFont = pygame.font.SysFont('Times New Roman', 35)

        name = getNodeObject(i).nodename
        textsurface = theFont.render(name, False, textColor)
        screen.blit(textsurface, (getNodeObject(i).location[0] - 10, getNodeObject(i).location[1] - 16))
    labelEdges()
    print("The total distance is: ", str(totalDist)[:6])

    #draw text detailing the shortest path information to screen
    distfont = pygame.font.SysFont('Arial', 16, bold=True)
    theString = "The length of the shortest path is: " + str(totalDist)[0:6]
    distSurface = distfont.render(theString, False, (250, 250, 250))
    screen.blit(distSurface, (10, 10))

    shortestPathString = ''
    for i in shortestpath:
        shortestPathString = shortestPathString + i + '  '

    theString2 = "The shortest path from "+ str(starting).capitalize()+ " to "+ str(ending).capitalize()+ " is:  " + shortestPathString[::-1] +  " "
    pathSurface = distfont.render(theString2, False, (250, 250, 250))
    screen.blit(pathSurface, (10, 30))


# Returns a dictionary containing the neighboring nodes and their distance from the provided node
def getNeighbors(nodeName):
    neighbors = {}
    for j in Edge.edgelist:
        if (j.nodename1 == nodeName):
            neighbors.update({j.nodename2: j.dist})
        elif (j.nodename2 == nodeName):
            neighbors.update({j.nodename1: j.dist})
    return neighbors

#Returns the node object for the given node name. Node objects can be used to access a node's location or previous node.
def getNodeObject(n):
    try:
        for i in Node.nodelist:
            if i.nodename == n:
             return i
    except:
        print("Unable to find node object. Check getNodeObject() function")

def closeProgram():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        sys.exit()

#Draw the length values for each edge
def labelEdges():
    for i in Edge.edgelist:
        distValue = i.getDist()
        edgefont = pygame.font.SysFont('Arial',14, bold=True)
        edgesurface = edgefont.render(str(distValue)[0:5], False, (250, 250, 250))
        x1 = getNodeObject(i.nodename1).location[0]
        y1 = getNodeObject(i.nodename1).location[1]
        x2 = getNodeObject(i.nodename2).location[0]
        y2 = getNodeObject(i.nodename2).location[1]
        m1 = float(abs((x1 + x2)/2))
        m2 = float(abs((y1 + y2)/2))
        midpoint = (int(m1), int(m2))
        screen.blit(edgesurface, midpoint)

#Draws blank graph with no path filled in
def drawBlankGraph():

    #Draw the lines connecting the nodes
    for j in Edge.edgelist:
        node1 = getNodeObject(j.nodename1)
        node2 = getNodeObject(j.nodename2)
        line = pygame.draw.line(screen, unvisitedColor, (node1.location[0],node1.location[1]), (node2.location[0],node2.location[1]), 5)

    #Draw the nodes, node labels, and edge length
    for i in Node.nodelist:
        ci = pygame.draw.circle(screen, unvisitedColor, (i.location[0], i.location[1]), 35)
        theFont = pygame.font.SysFont('Times New Roman',35)
        textsurface = theFont.render(i.nodename, False, (250, 250, 250))
        screen.blit(textsurface, (i.location[0]-10, i.location[1]-16))
    labelEdges()


#Creates Tkinter submission box for collecting user input for starting and ending node
def createSubmissionBox():

    #Function to retrieve text from Tkinter entry object
    def getInputNodes():
        startExists = False
        endExists = False
        for i in Node.nodelist:
            if i.nodename == str(startEntry.get()).capitalize():
                startExists = True
            if i.nodename == str(endEntry.get()).capitalize():
                endExists = True

        #check for valid input
        if not startExists or not endExists:
            messagebox.showerror("Invalid input", "Please enter a single letter from the graph for each input.")
            window.destroy()
            createSubmissionBox()

        global starting
        global ending
        starting = startEntry.get()
        ending = endEntry.get()

        window.quit()
        window.destroy()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    #Initialize Tkinter window
    window = Tk()
    w = 300
    h= 150
    x = 1200
    y = 300
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.protocol("WM_DELETE_WINDOW", closeProgram)
    startLabel = Label(window, text='Starting node: ').pack()
    startEntry = Entry(window)
    startEntry.pack()
    endLabel = Label(window, text='Ending node: ').pack()
    endEntry = Entry(window)
    endEntry.pack()
    spacer = Label(window, text='').pack()
    submit = Button(window, text='Find shortest path', command=getInputNodes).pack()
    window.update()
    mainloop()

def clearTextSurface():
    rect = pygame.Rect(5, 5, 1100, 150)
    pygame.draw.rect(screen, (0,0,0), rect)
    pygame.display.update()

#Initialize pygame values
pygame.init()
pygame.font.init()
width = 1200
height = 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Dijkstra's Algorithm")
unvisitedColor = (0, 153, 255)
visitedColor = (10, 194, 0)
textColor = (255, 255, 255)

#Draw the blank graph and run the algorithm
drawBlankGraph()
roundcount = 0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if(roundcount > 1):
        drawBlankGraph()
        createSubmissionBox()
        clearTextSurface()
        drawBlankGraph()
        solver()
    roundcount +=1
    pygame.display.flip()
    clock.tick(30)








