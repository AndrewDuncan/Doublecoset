import copy
from graph import *
#input the graph theta1 constructed from the flower automaton of K
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
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


P=K.product(G)
print "digraph P {"
print (str(P))
print "}"
