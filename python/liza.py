from graph import *

G=Graph()

a=G.addVertex("a")
b=G.addVertex("b")
c=G.addVertex("c")
d=G.addVertex("d")
e=G.addVertex(5)
G.addEdge(b,a,'x')
G.addEdge(c,b,'x')
G.addEdge(a,c,'x')
G.addEdge(c,d,'y')
G.addEdge(d,a,'z')
G.addEdge(a,e,'y')
G.addEdge(e,e,'z')

print "digraph liza {"
print (str(G))
print "}"
