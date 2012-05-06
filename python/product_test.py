from graph import *

G=Graph()
a=G.addVertex()
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
H=Graph()
u=H.addVertex()
v=H.addVertex()
w=H.addVertex()
z=H.addVertex()
H.addEdge(u,v,'x')
H.addEdge(w,z,'x')
H.addEdge(z,v,'y')

P=G.product(H)
print "digraph P {"
print (str(P))
print "}"
