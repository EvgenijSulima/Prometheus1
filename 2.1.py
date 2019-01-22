import sys
import math
x=float(sys.argv[1])
mu=float(sys.argv[2])
sig=float(sys.argv[3])
f=1/sig/math.sqrt(2*math.pi)*math.exp(-1*(x-mu)**2/2/sig**2)
print f

