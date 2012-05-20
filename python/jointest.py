from graph import *

G=Graph(label='G')

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

G1 =str(G)

H=Graph(label='H')

a1=H.addVertex("a1")
b1=H.addVertex("b1")
c1=H.addVertex("c1")
d1=H.addVertex("d1")
e1=H.addVertex("e1")
H.addEdge(b1,a1,'x1')
H.addEdge(c1,b1,'x1')
H.addEdge(a1,c1,'x1')
H.addEdge(c1,d1,'y1')
H.addEdge(d1,a1,'z1')
H.addEdge(a1,e1,'y1')
H.addEdge(e1,e1,'z1')

H1=str(H)

print "digraph liza {"
print (G1+H1)
print "}"
