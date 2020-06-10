
from graphics import *
from drawPole import *
from angle import *

from time import sleep
import numpy as np

pole1 = [-75.0041319,42.7246809]
pole2 = [-75.0047765,42.7249515]
pole3 = [-75.0047949,42.7254047]
turnTheta = angle(pole1,pole2,pole3)
print(turnTheta)

#win = GraphWin('Draft', 500, 500) # give title and dimensions
#poleLoc = (100,100)
#poleSize = 20
#drawPole(poleLoc, poleSize, win)
#drawPole([150,150],20, win)
#drawPole([200,200],20, win)
#drawPole([250,250],20, win)
#drawPole([300,300],20, win)
#win.getMouse()
