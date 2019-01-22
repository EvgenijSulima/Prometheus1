import sys
x=(sys.argv[1])
y=(sys.argv[2])
z=(sys.argv[3])

if x+y > z and x+z > y and y+z > z and x >0 and y>0 and z>0 :
    print "triangle"
else :
    print "not triangle"


