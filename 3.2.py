import sys

x=int(sys.argv[1])
result=0
a0=0
a1=1
if not x < 0:
    if x == 0:
        print "result 0"
    elif x == 1:
        print "result 1"
    else:

        for counter in range(x-1):
            result = a0 + a1
            a0=a1
            a1=result
            print "element="+str(counter+2)
            print "result="+str(result)
            print "a1="+str(a1)
            print "a0=" + str(a0)











