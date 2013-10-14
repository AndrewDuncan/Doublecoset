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
#a6=D.addVertex(6)
#a7=D.addVertex(7)
D.addEdge(a1,a2,'z1')
D.addEdge(a2,a3,'z2')
D.addEdge(a3,a4,'Z3')
D.addEdge(a4,a5,'y2')
D.addEdge(a5,a1,'x2')
D.addEdge(a1,a1,'z4')

D1=Graph()
c1=D1.addVertex(1)
c2=D1.addVertex(2)
D1.addEdge(c1,c1,'z4')
D1.addEdge(c2,c1,'x1')
D1.addEdge(c2,c1,'x2')

print('digraph D1 {')
print(str(D1))
print('}')

print('digraph H1 {')
print(str(flower1))
print('}')

D1xH1=D1.product(flower1)

print('digraph D1xH1 {')
print(str(D1xH1))
print('}')

D2=Graph()
b1=D2.addVertex(1)
b2=D2.addVertex(2)
b3=D2.addVertex(3)
b4=D2.addVertex(4)
b5=D2.addVertex(5)
b6=D2.addVertex(6)
b7=D2.addVertex(7)
b8=D2.addVertex(8)
b9=D2.addVertex(9)
D2.addEdge(b1,b1,'z4')
D2.addEdge(b2,b1,'y1')
D2.addEdge(b2,b1,'y2')
D2.addEdge(b1,b3,'z1')
D2.addEdge(b1,b4,'y1')
D2.addEdge(b3,b4,'y2')
D2.addEdge(b3,b5,'z2')
D2.addEdge(b5,b6,'Y2')
D2.addEdge(b4,b6,'y1')
D2.addEdge(b5,b8,'Z3')
D2.addEdge(b6,b7,'Y2')
D2.addEdge(b7,b8,'Y2')
D2.addEdge(b8,b9,'Y2')

print('digraph D2 {')
print(str(D2))
print('}')


print('digraph H2 {')
print(str(flower2))
print('}')

D2xH2=D2.product(flower2)

print('digraph D2xH2 {')
print(str(D2xH2))
print('}')
