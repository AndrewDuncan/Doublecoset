import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#nothing to add to theta to form theta1: so theta1=theta2
I=Graph(rooted=True,label='I')
I.addLoop(I.root,'bCaySrtxzAB')
I.addLoop(I.root,'yyxacaXyrUXYZYA')
I.addLoop(I.root,'zYY')

while I.fold() is True:
    I.fold()


y1list=[]
for i in range(0,4):
    y1list.append(I.vertices[i])

for i in range(8,24):
    y1list.append(I.vertices[i])

for v in y1list:
    I.removeVertex(v)   


vlist=I.vertices

I.addPath(vlist[0],vlist[1],'sX')

while I.fold() is True:
   I.fold()    

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

P=I.product(G)
print "digraph P {"
print (str(P))
print "}"
