import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#nothing to add to theta to form theta1: so theta1=theta2
J=Graph(rooted=True,label='J')
J.addLoop(J.root,'bCaySrtxzAB')
J.addLoop(J.root,'yyxacaXyrUXYZYA')
J.addLoop(J.root,'zYY')

while J.fold() is True:
    J.fold()

 

y2list=[]
for i in range(-4,17):
    y2list.append(J.vertices[i])

for v in y2list:
    J.removeVertex(v)

vlist=J.vertices

J.addPath(vlist[1],vlist[2],'Yt')

while J.fold() is True:
   J.fold()    

G=Graph(label='G2')
a=G.addVertex(1)
b=G.addVertex(2)
c=G.addVertex(3)
d=G.addVertex(4)
e=G.addVertex(5)
f=G.addVertex(6)
G.addEdge(a,b,'t')
G.addEdge(b,a,'u')
G.addEdge(a,f,'s')
G.addEdge(f,a,'s')
G.addEdge(a,c,'r')
G.addEdge(c,d,'r')
G.addEdge(d,e,'t')
G.addEdge(f,e,'r')   

P=J.product(G)
print "digraph P {"
print (str(P))
print "}"
