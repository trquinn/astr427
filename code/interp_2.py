import numpy as np
from  scipy.interpolate import lagrange
from  scipy.interpolate import interp1d
from  scipy.interpolate import CubicSpline

# Data table from a file; first column is x; second column is y
data = np.loadtxt("hw1.dat")
x = data[:,0]
y = data[:,1]

# A Langrange interpolation using all the data.
# This will be a 4th order polynomial
poly = lagrange(x, y)
# interpolation points
xint = np.arange(-1.0, 1.0, 0.01)
yintp = poly(xint)

# Cubic spline interpolation using the default boundary conditions
spline = interp1d(x, y, 'cubic')
yints = spline(xint)

# Cubic spline using a slightly different interface,
# and specify "natural" boundary conditions: the 2nd derivatives are 0
# at the boundaries
spline2 = CubicSpline(x, y, bc_type='natural')
yints2 = spline2(xint)

# Actual function that generated the data
def runge(x) :
    return 1/(1 + 25*x**2)

ytrue = runge(xint)

import pylab
pylab.plot(xint, ytrue, label="actual function")
pylab.show()
pylab.plot(x, y, marker="x", label="data")
pylab.plot(xint, yintp, label="polynomial")
pylab.plot(xint, yints, label="spline")
pylab.plot(xint, yints2, label="natural spline")
pylab.plot(xint, ytrue, label="actual function")
pylab.legend()

