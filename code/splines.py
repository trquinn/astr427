# Illustration of
# 1) The differences between spline boundary conditions
# 2) The dangers of extrapolation

import numpy as np
from  scipy.interpolate import CubicSpline

# Data for a sin curve
x = np.arange(0.,9.)
y = np.sin(x)
xint = np.arange(-1, 9, 0.01) # values to interpolate at

# Cubic spline interpolation using the default boundary conditions
spline1 = CubicSpline(x, y)
yints1 = spline1(xint)
# Cubic spline specifying "natural" boundary conditions:
# the 2nd derivatives are 0 at the boundaries
spline2 = CubicSpline(x, y, bc_type='natural')
yints2 = spline2(xint)

import pylab
pylab.plot(x, y, marker="x", label="data")
pylab.plot(xint, np.sin(xint), label="theory")
pylab.plot(xint, yints1, label="spline, default")
pylab.plot(xint, yints2, label="natural spline")
pylab.legend()

