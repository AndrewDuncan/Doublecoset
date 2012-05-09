from graph import *

G=Graph()

a=G.addVertex('a')
b=G.addVertex()
c=G.addVertex()
d=G.addVertex()
e=G.addVertex()
G.addEdge(b,a,'x')
G.addEdge(c,b,'x')
G.addEdge(a,c,'x')
G.addEdge(c,d,'y')
G.addEdge(d,a,'z')
G.addEdge(a,e,'y')
G.addEdge(e,e,'z')
G.addPath(a,e,'r')

print "digraph G {"
print (str(G))
print "}"
