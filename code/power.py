#
# Some examples to demonstrate recommended and not recommended
# uses of functions.  Note that the actual "power" operator in
# python is not implemented as shown here.
# 
import math
# The following is standard function use
# 
def power(x, y):
    # function parameters can be overwritten
    # however this is not recommended as it may cause confusion
    x = math.log(x)
    x *= y
    return math.exp(x)

z = power(2, 3)

# The following is NOT recommended: "result" will not be returned to the
# calling context
def power(x, y, result):
    x = math.log(x)
    x *= y
    result =  math.exp(x)

# Since the result is modified, not overwritten, the result gets returned
# to the calling context.  This type of use may be useful to save memory
# when working with long lists or arrays.
def power(x, y, result):
    x = math.log(x)
    x *= y
    result.append(math.exp(x))
    
# Manipulation of global variables as below is STRONGLY discouraged
global z

def power(x, y):
    global z
    x = math.log(x)
    x *= y
    z =  math.exp(x)


