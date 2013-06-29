from graph import *

G=Graph()
a=G.addVertex()
b=G.addVertex()
c=G.addVertex()
d=G.addVertex()
e=G.addVertex()
f=G.addVertex()
G.addEdge(a,b,'x')
G.addEdge(a,b,'y')
G.addEdge(b,c,'x')
G.addEdge(b,c,'y')
G.addEdge(c,d,'x')
G.addEdge(c,d,'y')
G.addEdge(d,a,'x')
G.addEdge(d,a,'y')
G.addEdge(a,e,'w')
G.addEdge(e,a,'w')
G.addEdge(e,f,'x')
G.addEdge(f,e,'y')


print "digraph hd {"
print(str(G))
print "}"

D= G.double()
print ("digraph SxS {")
print (str(D))
print ("}")
