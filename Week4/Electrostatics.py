import numpy as np

def pointPotential(x,y,q,posx,posy):
    """this function finds the electric potential at a point due to a point charge"""
    k = 1.3806488e-23 #Nm^2/C^2
    V = (k*q/(np.sqrt((x-posx)**2+(y-posy)**2)))
    return V

def dipolePotential(x,y,q,d):
    """This finds the electric potential at a point when given a two point charges"""
    Vxy = pointPotential(x,y,q,d/2,0) + pointPotential(x,y,-q,-d/2,0)
    return Vxy
