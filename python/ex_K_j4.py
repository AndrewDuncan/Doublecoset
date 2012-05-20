import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#from ex_K_j4-x-g.py, there is nothing to add to theta 4
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
print "digraph J {"
print (str(J))
print "}"
