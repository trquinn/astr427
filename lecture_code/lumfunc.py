# Examples of how to turn functions of many variables into a function
# of a single variable. The motivation is that you are using a package
# (say for integration) that requires a function of a single variable,
# and the other variables are considered constant during the calculation

# Example function: assume LF is a function of mass, metalicity, and age:
def LF(mass, z, time):
    return mass*z*time # Not a realistic dependence!

# Here are the constants
zI = 0.03
timeI = 3e7

# Lambda: anonymous functions; PopI is now a function of one variable
# NOTE: this does not "enclose" zI and timeI; See below for a factory function
# using this
PopI = lambda mass: LF(mass, zI, timeI)
print(PopI(1.0))

# A "factory function": given metalicity and age, creates a function of mass
# and returns it
def make_LumFunc(z, time):
    def PopI_arg(mass) :
        return LF(mass, z, time)
    return PopI_arg

PopI = make_LumFunc(zI, timeI)

# Here is how to use lambda in a factory function.  In contrast to the
# lambda above, this will enclose the current values of z and time.
def make_LumFunc(z, time):
    return lambda mass: LF(mass, z, time)

# A "functor" object: define the call operator to add in the extra arguments
class LumFunc:
    def __init__(self, zi, timei):
        self.z = zi
        self.time = timei
    def __call__(self, mass):
        return LF(mass, self.z, self.time)

PopI = LumFunc(zI, timeI)
