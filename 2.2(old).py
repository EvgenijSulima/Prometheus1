import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
pes='Everybody sing a song:'
if z == 1 :
	zn='!'
else:
	zn='.'
pes=str('Everybody sing a song:')+((' la'+'-la'*(x-1))*y)+zn
print pes