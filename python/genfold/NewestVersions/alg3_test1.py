from alg3 import *

g=Graph()
v1=g.addVertex(1)
v2=g.addVertex(2)
v3=g.addVertex(3)
v4=g.addVertex(4)
v5=g.addVertex(5)
g.addEdge(v1,v2,'z1')
g.addEdge(v2,v3,'z2')
g.addEdge(v4,v3,'z3')
g.addEdge(v4,v5,'b2')
g.addEdge(v5,v1,'b1')
g.addEdge(v1,v1,'z4')
print('digraph g {')
print(str(g))
print('}')
F1=free_group(2,"a")
F2=free_group(2,"b")
Z=free_group(4,"z")
F=(F1,F2)
#(F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2)=alg3_pre()
delta_k0=[0,1]
delta_k0[0],delta_k0[1],delta_z=d1(g,F,Z)
deltap_k1=[0,1]
deltap_k1[0],deltap_k1[1]=d2(delta_k0,Z)
#delta_k1=[0,1]
#delta_k1[0],delta_k1[1]=d3(deltap_k1)
