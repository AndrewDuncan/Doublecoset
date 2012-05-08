from graph import *

G=Graph()
a=G.addVertex(1)
b=G.addVertex(2)
c=G.addVertex(3)
d=G.addVertex(4)
e=G.addVertex(5)
f=G.addVertex(6)
G.addEdge(a,b,'y3')
G.addEdge(b,a,'y4')
G.addEdge(a,f,'y2')
G.addEdge(f,a,'y2')
G.addEdge(a,c,'y1')
G.addEdge(c,d,'y1')
G.addEdge(d,e,'y3')
G.addEdge(f,e,'y1')

G2 = G.double()
print "digraph GxG {"
print (str(G2))
print "}"
