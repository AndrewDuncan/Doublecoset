#Theta 2 -- add paths to Theta1
import copy
from graph import *
import ex_K
ex = ex_K
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#First copy Theta 1 (run it again)

while ex.K.fold() is True:
    ex.K.fold()

xlist=[]
for i in range(4,9):
    xlist.append(ex.K.vertices[i])

for i in range(16,23):
    xlist.append(ex.K.vertices[i])

for v in xlist:
    ex.K.removeVertex(v)

vlist=ex.K.vertices
#print vlist

z1=ex.K.addVertex()
z2=ex.K.addVertex()
z3=ex.K.addVertex()
z4=ex.K.addVertex()
z5=ex.K.addVertex()
ex.K.addEdge(vlist[0],z1,'b')
ex.K.addEdge(vlist[5],z2,'b')
ex.K.addEdge(vlist[6],z3,'b')
ex.K.addEdge(z1,z2,'c')
ex.K.addEdge(z2,z3,'c')
ex.K.addEdge(vlist[6],z4,'a')
ex.K.addEdge(vlist[7],z5,'A')
ex.K.addEdge(z4,z5,'a')
ex.K.addPath(vlist[0],vlist[6],'abc')

while ex.K.fold() is True:
    ex.K.fold()

vlist=ex.K.vertices
#print vlist

#add new paths as necessary
ex.K.addPath(vlist[8],vlist[14],'X')

while ex.K.fold() is True:
   ex.K.fold()
    
print "digraph K {"
print (str(ex.K))
print "}"
