from alg3 import *

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

print('digraph g {')
print(str(g))
print('}')
F1=free_group(3,"x")
F2=free_group(3,"y")
Z=free_group(3,"z")
F=(F1,F2)
#(F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2)=alg3_pre()
delta_k0=[0,1]
delta_k0[0],delta_k0[1],delta_z=d1(g,F,Z)
deltap_k1=[0,1]
deltap_k1[0],deltap_k1[1]=d2(delta_k0,Z)
#delta_k1=[0,1]
#delta_k1[0],delta_k1[1]=d3(deltap_k1)
