import math

# Math mainly between vectors (fancy way of saying multiple numbers),
# Search online for what these do

# Add 2 vectors' values from each other (which translates it positivley)
def add(vector1, vector2):
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])

# Subtract 2 vectors' values from each other (which translates it negativley)
def sub(vector1, vector2):
    return (vector1[0] - vector2[0], vector1[1] - vector2[1])

# Multiply both values in a vector by another number
def multiply(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)

# Move a value from vector1 to vector2 smoothly by t
def linearInterpolateVector(vector1, vector2, t):
    return add(multiply(vector1, 1-t), multiply(vector2, t))

# Move a value from scalar1 to scalar2 smoothly by t
def linearInterpolateScalar(scalar1, scalar2, t):
    return scalar1 * (1-t) + scalar2 * t

# Gets the straight-line distance of a vector from (0,0) aka the magnitude
def calcMagnitude(vector):
    return math.sqrt(pow(vector[0], 2) + pow(vector[1], 2))
