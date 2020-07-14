# Dijkstra's Shortest Path Algorithm

## Introduction
This project aims to use Dijkstra's algorithm to find the shortest path between any two nodes for the given wieghted graph. A graphical user interface will allow the user to view the graph and input the two nodes to find the shortest path for. The output is the length of the shortest path and the set of nodes that form the shortest path.
## Requirements
 - Python 3.x
 - Tkinter
 - Pygame
## Example
![](ShortestPathExample.gif)
## What I learned
I learned a lot about how event loops work. In this project there were two event loops, one for Tkinter and one for Pygame. Originally, I was using the Pyglet package for drawing the graph component on screen but ended up switching to Pygame because it was easier to customize the event loop. I learned more about how to integrate a gui with the functional algorithm code. I broke the code down into many functions so I could reuse functionalities without having to rewrite things as much. I broke the complex process of using the algorithm and drawing the graph into small, manageable pieces so the logic of the program was clear to me and I understood what small process needs to happen at each step in order to cumulatively amount to the complete process. This made it easier to merge the GUI logic with the algorithm logic. 
