from graph import *

G=Graph()
a=G.addVertex()
b=G.addVertex()
c=G.addVertex()
d=G.addVertex()
e=G.addVertex()
f=G.addVertex()
g=G.addVertex()
h=G.addVertex()
i=G.addVertex()
G.addEdge(a,b,'x')
G.addEdge(b,c,'x')
G.addEdge(c,a,'x')
G.addEdge(b,f,'y')
G.addEdge(f,g,'y')
G.addEdge(g,b,'y')
G.addEdge(c,h,'y')
G.addEdge(h,i,'y')
G.addEdge(i,c,'y')
G.addEdge(a,d,'y')
G.addEdge(d,e,'y')
G.addEdge(e,a,'y')

print "digraph bez {"
print(str(G))
print "}"
