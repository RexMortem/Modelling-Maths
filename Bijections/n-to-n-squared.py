# bijection between Naturals and Naturals^2 (set of all pairs of naturals)
# Naturals include 0 here

import math

triangleNumber = lambda n: math.floor((n/2) * (n+1)) 
inverseTriangleNumber = lambda n: math.floor(-1/2 + math.sqrt(2*n + 1/4)) # formula derived from completing the square on triangleNum formula

# Bijection going from N to N^2
def generatePair(n):
    layersCompleted = inverseTriangleNumber(n) # also the total 
    first = n - triangleNumber(layersCompleted)
    return (first, layersCompleted - first)

# Bijection going from N^2 to N
def generateScalar(pair):
    total = pair[0] + pair[1]
    return triangleNumber(total) + pair[0]

# First 10 pairs
for i in range(10):
    print(i, generatePair(i), generateScalar(generatePair(i)))
