import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#nothing to add to theta to form theta1: so theta1=theta2
I=Graph(rooted=True,label='I')
I.addLoop(I.root,'bCaySrtxzAB')
I.addLoop(I.root,'yyxacaXyrUXYZYA')
I.addLoop(I.root,'zYY')

while I.fold() is True:
    I.fold()


y1list=[]
for i in range(0,4):
    y1list.append(I.vertices[i])

for i in range(8,24):
    y1list.append(I.vertices[i])

for v in y1list:
    I.removeVertex(v)   


vlist=I.vertices
#i=0
#for c in vlist:
#    print "(", i,",",c, ")",
#    i +=1

while I.fold() is True:
    I.fold()
print "digraph I {"
print (str(I))
print "}"
