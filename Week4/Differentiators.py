import numpy as np


def finiteDifference(x,y):
    """finds the derivative of the function y over the range x using a finite di"""
    dydx = np.zeros(y.shape,float)
    dydx[:-1] = diff(y)/diff(x)
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    return dydx



def fourPtFiniteDiff(x,y):
    """finds the derivative of the function y over the range x using a four poin"""
    dydx = np.zeros(y.shape,float)
    for i in range(2,len(y)-2):
        a = y[i-2]
        b = y[i-1]
        c = y[i+1]
        d = y[i+2]
        dydx[i] = (a-8*b+8*c-d)/(12*(x[1]-x[0]))
    dydx[-1] = (y[-1]-y[-2])/(x[-1]-x[-2])
    dydx[-2] = (y[-2]-y[-3])/(x[-2]-x[-3])
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    dydx[1] = (y[2]-y[1])/(x[2]-x[1])
    return dydx




