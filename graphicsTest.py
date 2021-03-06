from graphics import *

win = GraphWin('Draft', 500, 500) # give title and dimensions

def drawPole(poleLoc,poleSize):
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

poleLoc = (100,100)
poleSize = 20
drawPole(poleLoc, poleSize)
drawPole([150,150],20)
drawPole([200,200],20)
drawPole([250,250],20)
drawPole([300,300],20)


win.getMouse()
