from alg3 import *
import copy

g=Graph()
a1=g.addVertex(1)
a2=g.addVertex(2)
a3=g.addVertex(3)
a4=g.addVertex(4)
a5=g.addVertex(5)
a6=g.addVertex(6)
a7=g.addVertex(7)
g.addEdge(a1,a2,'x1')
g.addEdge(a2,a3,'y1')
g.addEdge(a3,a4,'z1')
g.addEdge(a2,a5,'x1')
g.addEdge(a6,a5,'z1')
g.addEdge(a7,a5,'y1')

h=Graph(False,'h');
j=Graph(False,'j');
h.vertices=g.vertices
j.vertices=copy.deepcopy(g.vertices)
j.removeVertex(j.vertices[6])
for v in j.vertices:
	print("vertex attrs", v.label,v.name)


print("g verts", g.vertices)
print("h verts", h.vertices)
print("j verts", j.vertices)
