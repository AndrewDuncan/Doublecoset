from graph import *

G=Graph()
a=G.addVertex()
b=G.addVertex()
c=G.addVertex()
d=G.addVertex()
e=G.addVertex()
f=G.addVertex()
G.addEdge(a,c,'w')
G.addEdge(a,b,'y')
G.addEdge(a,f,'x')
G.addEdge(b,a,'z')
G.addEdge(c,d,'w')
G.addEdge(d,e,'y')
G.addEdge(f,e,'w')
G.addEdge(f,a,'x')

print "digraph liza2 {"
print(str(G))
print "}"
