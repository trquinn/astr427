import numpy as np
from  scipy.interpolate import lagrange
from  scipy.interpolate import interp1d
from  scipy.interpolate import CubicSpline

# Data for a step function with the step at about x = 1.5
x = np.array([0.0, 1.0, 1.4, 1.6, 2.0, 3.0])
y = np.array([1.0, 1.0, 1.0, -1.0, -1.0, -1.0])

# A Langrange interpolation using all the data.
# This will be a 5th order polynomial
poly = lagrange(x, y)
xint = np.arange(0.0, 3.0, 0.01)
yintp = poly(xint)

# Cubic spline interpolation using the default boundary conditions
spline = interp1d(x, y, 'cubic')
yints = spline(xint)

# Cubic spline using a slightly different interface,
# and specify "natural" boundary conditions: the 2nd derivatives are 0
# at the boundaries
spline2 = CubicSpline(x, y, bc_type='natural')
yints2 = spline2(xint)

import pylab
pylab.plot(x, y, marker="x", label="data")
pylab.plot(xint, yintp, label="polynomial")
pylab.plot(xint, yints, label="spline")
pylab.plot(xint, yints2, label="natural spline")
pylab.legend()

