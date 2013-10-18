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


print "digraph J {"
print (str(J))
print "}"
