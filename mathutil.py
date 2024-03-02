import math

# Math

def add(vector1, vector2):
    return (vector1[0] + vector2[0], vector1[1] + vector2[1])

def sub(vector1, vector2):
    return (vector1[0] - vector2[0], vector1[1] - vector2[1])

def multiply(vector, scalar):
    return (vector[0] * scalar, vector[1] * scalar)

def linearInterpolateVector(vector1, vector2, t):
    return add(multiply(vector1, 1-t), multiply(vector2, t))
def linearInterpolateScalar(scalar1, scalar2, t):
    return scalar1 * (1-t) + scalar2 * t

def calcMagnitude(vector):
    return math.sqrt(pow(vector[0], 2) + pow(vector[1], 2))
