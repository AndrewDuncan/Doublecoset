from alg3 import *

g=Graph()
a1=g.addVertex(1)
a2=g.addVertex(2)
a3=g.addVertex(3)
a4=g.addVertex(4)
a5=g.addVertex(5)
g.addEdge(a1,a2,'z1')
g.addEdge(a2,a3,'z2')
g.addEdge(a4,a3,'z3')
g.addEdge(a4,a5,'y2')
g.addEdge(a5,a1,'x2')
g.addEdge(a1,a1,'z4')
#
print('digraph g {')
print(str(g))
print('}')
F1=free_group(3,"x")
F2=free_group(3,"y")
Z=free_group(4,"z")
F=(F1,F2)
#(F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2)=alg3_pre()
delta_k0=[0,1]
delta_k0[0],delta_k0[1],delta_z=d1(g,F,Z)
deltap_k1=[0,1]
deltap_k1[0],deltap_k1[1]=d2(delta_k0,Z)
#delta_k1=[0,1]
#delta_k1[0],delta_k1[1]=d3(deltap_k1)
