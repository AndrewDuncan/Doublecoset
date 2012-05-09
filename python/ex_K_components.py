import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
K=Graph(rooted=True)
K.addLoop(K.root,'bCaySrtxzAB')
K.addLoop(K.root,'yyxacaXyrSXYZYA')
K.addLoop(K.root,'zYY')

while K.fold() is True:
    K.fold()

X1=copy.deepcopy(K)
Y1=copy.deepcopy(K)
Y2=copy.deepcopy(K)

#x2=X1.vertices
#print x2

x2list=[]
for i in range(4,9):
    x2list.append(X1.vertices[i])

for i in range(16,23):
    x2list.append(X1.vertices[i])

for v in x2list:
    X1.removeVertex(v)

y1list=[]
for i in range(0,4):
    y1list.append(Y1.vertices[i])

for i in range(8,24):
    y1list.append(Y1.vertices[i])

for v in y1list:
    Y1.removeVertex(v)   

y2list=[]
for i in range(-4,17):
    y2list.append(Y2.vertices[i])

for v in y2list:
    Y2.removeVertex(v)

print "digraph X1 {"
print (str(X1))
#print (str(Y2))
print "}"
