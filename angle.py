# angle.py
"""
This is a function to be used with graphics.py
This function allows to calculate the angle on a pole by giving coordinates
Inputs:
  backPole - an array with an [x,y] coordinate of the center of the pole to be
            drawn.
  pole - an array with an [x,y] coordinate of the center of the pole to be
            drawn.
  forwardPole - an array with an [x,y] coordinate of the center of the pole to be
            drawn.
Outputs:
  angle: the angle on a pole in degrees
"""
#pole1 = [42.7246809,-75.0041319]
#pole2 = [42.7249515,-75.0047765]

import numpy as np
def angle(backPole,pole,forwardPole):
    def cart2pol(x, y):
        rho = np.sqrt(x**2 + y**2)
        phi = (np.arctan2(y, x)*180/np.pi)
        return(rho, phi)
    def pol2cart(rho, phi):
        x = rho * np.cos(phi)
        y = rho * np.sin(phi)
        return(x, y)

    vec1 = [pole[0]-backPole[0],pole[1]-backPole[1]]
    vec2 = [forwardPole[0]-pole[0],forwardPole[1]-pole[1]]
    vec1Pol = cart2pol(vec1[0],vec1[1])
    vec2Pol = cart2pol(vec2[0],vec2[1])
    angle = vec2Pol[1]-vec1Pol[1]
    return angle
