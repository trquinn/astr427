import numpy as np

# points to plot
xint = np.arange(9e-9, 1.0e-7, 1e-10)

def func(x) :
    return (1.0 - np.cos(x))/x**2

def small(x) :
    return 1.11e-16/x**2

import pylab
pylab.plot(xint, small(xint))
pylab.plot(xint, 2*small(xint))
pylab.plot(xint, func(xint))
pylab.ylim((-.1,1.5))
