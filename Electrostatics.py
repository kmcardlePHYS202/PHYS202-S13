import numpy as np

def pointPotential(x,y,q,posx,posy):
    """finds the electric potential at a point due to point charge"""
    k = 1.3806488e-23 #Nm^2/C^2
    V = (k*q/(np.sqrt((x-posx)**2+(y-posy)**2)))
    return V

def dipolePotential(x,y,q,d):
    """finds the electric potential at a point given a two point charges"""
    Vxy = pointPotential(x,y,q,d/2,0) + pointPotential(x,y,-q,-d/2,0)
    return Vxy

def pointField(x,y,q,Xq,Yq):
    """Returns a tuple of the electric field caused by q at (Xq,Yq)"""
    k = 1.3806488e-23 #Nm^2/C^2
    Ex = (k*q*(x-Xq))/(((x-Xq)**2+(y-Yq)**2)**(0.5))
    Ey = (k*q*(y-Yq))/(((x-Xq)**2+(y-Yq)**2)**(0.5))
    return [Ex,Ey]
