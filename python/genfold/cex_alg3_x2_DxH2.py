from alg3 import *

#print('digraph g1 {')
#print(str(g1))
#print('}')
F1=free_group(2,"x")
F2=free_group(2,"y")
Z=free_group(4,"z")
F=(F1,F2)
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
g1=['y1','Y2']
g2=['y2','y1','y2']
g3=['y2','y2','y2']
g4=['Y2','y1']
H1=subgroup('H1',[h1,h2,h3,h4],['z1','z2','z3','z4'])
H2=subgroup('H2',[g1,g2,g3,g4],['z1','z2','z3','z4'])
#	F=(F1,F2)
(flower1,double1,forest1)=alg2_pre(H1)
(flower2,double2,forest2)=alg2_pre(H2)
H=(H1,H2)
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2

D=Graph()
a1=D.addVertex(1)
a2=D.addVertex(2)
a3=D.addVertex(3)
a4=D.addVertex(4)
a5=D.addVertex(5)
a6=D.addVertex(6)
a7=D.addVertex(7)
a8=D.addVertex(8)
a9=D.addVertex(9)
a10=D.addVertex(10)
a11=D.addVertex(11)
a12=D.addVertex(12)
a13=D.addVertex(13)
a14=D.addVertex(14)
D.addEdge(a1,a1,'z4')
D.addEdge(a1,a2,'Y1')
D.addEdge(a1,a2,'Y2')
D.addEdge(a1,a3,'z1')
D.addEdge(a1,a4,'y1')
D.addEdge(a2,a2,'z1')
D.addEdge(a2,a9,'Y2')
D.addEdge(a2,a11,'z2')
D.addEdge(a1,a10,'y2')
D.addEdge(a3,a4,'y2')
D.addEdge(a3,a5,'z2')
D.addEdge(a3,a12,'Y2')
D.addEdge(a4,a10,'Z4')
D.addEdge(a4,a6,'y1')
D.addEdge(a4,a7,'z1')
D.addEdge(a4,a11,'y2')
D.addEdge(a5,a6,'Y2')
D.addEdge(a5,a14,'y2')
D.addEdge(a5,a8,'Z3')
D.addEdge(a6,a11,'Z4')
D.addEdge(a6,a7,'Y2')
D.addEdge(a6,a13,'Z3')
D.addEdge(a7,a8,'Y2')
D.addEdge(a7,a14,'z3')
D.addEdge(a8,a13,'Y2')
D.addEdge(a9,a10,'z2')
D.addEdge(a9,a10,'z3')
D.addEdge(a11,a12,'Z3')
print('digraph D {')
print(str(D))
print('}')


print('digraph H2 {')
print(str(flower2))
print('}')

DxH2=D.product(flower2)

print('digraph DxH2 {')
print(str(DxH2))
print('}')
