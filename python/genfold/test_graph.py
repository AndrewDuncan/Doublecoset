import string
from graph_tabbed import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
K=Graph(rooted=True,label='K')
K.addLoop(K.root,['b1','C1','a1'])
K.addLoop(K.root,['b1','c2','a1','a1'])
K.addPath(K.vertices[0],K.vertices[4],['A1','c2','a1','A1','a1','A1','a1'])

K.addEdge(K.vertices[0],K.vertices[0],'A1')
K.addEdge(K.vertices[4],K.vertices[4],'a1')
K.addEdge(K.vertices[1],K.vertices[5],'c1')

while K.fold() is True:

    K.fold()

D=K.double()
KD=K.product(D)
print ("digraph {")
print (str(KD))
print ("}")
