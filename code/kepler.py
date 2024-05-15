# A simple demonstration of how Newton can go wrong
# with Kepler at high eccentricity
import numpy as np
import pylab

def kep(E, e, M):
    return E - e*np.sin(E) - M
def dkep(E, e, M):
    return 1 - e*np.cos(E)

# Cover a large range of eccentric anomolies
Ea = np.arange(0, 20*np.pi, .01)

# Values of E - e*sin(E)
Ka = kep(Ea, .9, 0.0)
pylab.plot(Ea, Ka)

# Illustrate one Newton step for M = 6.0
# Plot M = 6 line
pylab.plot(Ea, Ea*0.0 +6.0)
# plot a line with a slope given by the derivative
pylab.plot(Ea, Ea*dkep(0.0, .9, 0.0))
# The intersection of the two lines shows where the first Newton step will
# end up


pylab.ylabel('M')
pylab.xlabel('E')
