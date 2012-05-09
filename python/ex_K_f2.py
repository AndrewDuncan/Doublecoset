#Theta 2 -- add paths to Theta1
import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#First copy Theta 1 (run it again)
K=Graph(rooted=True)
K.addLoop(K.root,'bCaySrtxzAB')
K.addLoop(K.root,'yyxacaXyrSXYZYA')
K.addLoop(K.root,'zYY')

while K.fold() is True:
    K.fold()

xlist=[]
for i in range(4,9):
    xlist.append(K.vertices[i])

for i in range(16,23):
    xlist.append(K.vertices[i])

for v in xlist:
    K.removeVertex(v)

vlist=K.vertices
#print vlist

z1=K.addVertex()
z2=K.addVertex()
z3=K.addVertex()
z4=K.addVertex()
z5=K.addVertex()
K.addEdge(vlist[0],z1,'b')
K.addEdge(vlist[5],z2,'b')
K.addEdge(vlist[6],z3,'b')
K.addEdge(z1,z2,'c')
K.addEdge(z2,z3,'c')
K.addEdge(vlist[6],z4,'a')
K.addEdge(vlist[7],z5,'A')
K.addEdge(z4,z5,'a')
K.addPath(vlist[0],vlist[6],'abc')

while K.fold() is True:
    K.fold()

vlist=K.vertices
#print vlist

#add new paths as necessary
K.addPath(vlist[8],vlist[14],'X')

while K.fold() is True:
   K.fold()
    
print "digraph K {"
print (str(K))
print "}"
