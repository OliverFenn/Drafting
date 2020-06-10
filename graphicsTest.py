
from graphics import *
from drawPole import *
#from angle import *

from time import sleep



win = GraphWin('Draft', 500, 500) # give title and dimensions

poleLoc = (100,100)
poleSize = 20
drawPole(poleLoc, poleSize, win)
drawPole([150,150],20, win)
drawPole([200,200],20, win)
drawPole([250,250],20, win)
drawPole([300,300],20, win)

win.getMouse()
