import numpy as np

def LinearLeastSquaresFit(x,y):
    """take in arrays representing (x,y) values for a set of linearly varying data and
    perform a linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit like with their uncertainties."""
    
    n = np.double(len(x))
    x_ = np.mean(x)
    y_ = np.mean(y)
    x2_ = np.mean(x**2)
    xy_ = np.mean(x*y)
    
    m = (xy_ - (x_*y_))/(x2_ - (x_**2))
    b = ((x2_*y_) - (x_*xy_))/(x2_ - (x_**2))
    
    delta = y-(m*x + b)
    d2_ = np.mean(delta**2)
    
    sig_m = np.sqrt((1/(n-2))*(d2_/(x2_ - (x_**2))))
    sig_b = np.sqrt((1/(n-2))*((d2_*x2_)/(x2_ - (x_**2))))

    
    return m,b,sig_m,sig_b
