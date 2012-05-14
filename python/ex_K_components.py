import copy
import ex_K
ex = ex_K


while ex.K.fold() is True:
    ex.K.fold()

X1=copy.deepcopy(ex.K)
Y1=copy.deepcopy(ex.K)
Y2=copy.deepcopy(ex.K)

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

print "digraph Y1 {"
#print (str(Y1))
print (str(Y2))
#print (str(X1))
print "}"
