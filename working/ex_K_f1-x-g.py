import copy
from graph import *
import ex_K
ex = ex_K
#input the graph theta1 constructed from the flower automaton of K
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3

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
#now input the graph from example 3.7

G=Graph()
a=G.addVertex(1)
b=G.addVertex(2)
c=G.addVertex(3)
d=G.addVertex(4)
e=G.addVertex(5)
G.addEdge(b,a,'a')  #label x1
G.addEdge(c,b,'a')  #label x1
G.addEdge(a,c,'a') #label x1
G.addEdge(c,d,'b') #label x2
G.addEdge(d,a,'c') #label x3
G.addEdge(a,e,'b') #label x2
G.addEdge(e,e,'c') #label x3


P=ex.K.product(G)
print "digraph P {"
print (str(P))
print "}"
