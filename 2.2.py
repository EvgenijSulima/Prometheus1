import sys
x=int(sys.argv[1])
y=int(sys.argv[2])
z=int(sys.argv[3])
kup=''
pri=''
song='Everybody sing a song:'
for v in range(x):
     pri = pri + '-la'
     if v==0 :
          pri = 'la'
if not y==0:
     for v in range(y):
          kup=kup+" "+pri
if z==0:
     song = song + kup+'.'
else:
     song = song + kup+'!'
print song
