from graph import *

G=Graph()
a=G.addVertex(1)
b=G.addVertex(2)
c=G.addVertex(3)
d=G.addVertex(4)
e=G.addVertex(5)
G.addEdge(b,a,'x1')
G.addEdge(c,b,'x1')
G.addEdge(a,c,'x1')
G.addEdge(c,d,'x2')
G.addEdge(d,a,'x3')
G.addEdge(a,e,'x2')
G.addEdge(e,e,'x3')

G2 = G.double()
print "digraph GxG {"
print (str(G2))
print "}"
