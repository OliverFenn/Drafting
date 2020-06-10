# graphics.py
"""
This is a function to be used with graphics.py
This function is made to attempt to automate the creation of Single Line
Diagrams which show the layout of utility poles.
Inputs:
  poleLoc - an array with an [x,y] coordinate of the center of the pole to be
            drawn.
  poleSize - an integer describing the radius of the pole.
  win - the window to draw in
"""
from graphics import *
def drawPole(poleLoc,poleSize,win):
    pole = Circle(Point(poleLoc[0],poleLoc[1]), poleSize) # set center and radius
    pole.setWidth(2)
    pole.setOutline("black")
    pole.setFill("white")
    pole.draw(win)
    line = Line(Point(poleLoc[0]-poleSize,poleLoc[1]-poleSize),Point(poleLoc[0]+poleSize,poleLoc[1]+poleSize))
    line.setWidth(2)
    line.setFill("black")
    line.draw(win)
    line = Line(Point(poleLoc[0]-poleSize,poleLoc[1]+poleSize),Point(poleLoc[0]+poleSize,poleLoc[1]-poleSize))
    line.setWidth(2)
    line.setFill("black")
    line.draw(win)
