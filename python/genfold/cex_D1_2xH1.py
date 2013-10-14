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
(flower1,double1,forest1,bfs1)=alg2_pre(H1)
(flower2,double2,forest2,bfs2)=alg2_pre(H2)
H=(H1,H2)
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2

D=Graph()
a1=D.addVertex(1)
a2=D.addVertex(2)
a3=D.addVertex(3)
a5=D.addVertex(5)
a9=D.addVertex(9)
a10=D.addVertex(10)
a15=D.addVertex(15)
a16=D.addVertex(16)
a17=D.addVertex(17)
a18=D.addVertex(18)
#a7=D.addVertex(7)
D.addEdge(a1,a2,'z1')
D.addEdge(a2,a3,'z2')
D.addEdge(a5,a1,'x2')
D.addEdge(a1,a1,'z4')
D.addEdge(a1,a17,'x1')
D.addEdge(a1,a5,'X1')
D.addEdge(a1,a5,'X2')
D.addEdge(a2,a3,'z3')
D.addEdge(a3,a18,'X2')
D.addEdge(a5,a5,'z1')
D.addEdge(a5,a10,'Z4')
D.addEdge(a5,a16,'X1')
D.addEdge(a9,a10,'z2')
D.addEdge(a9,a10,'z3')
D.addEdge(a9,a15,'x2')
D.addEdge(a10,a16,'X2')
D.addEdge(a15,a16,'x1')
D.addEdge(a15,a16,'x2')
D.addEdge(a2,a17,'x2')
D.addEdge(a17,a18,'x1')
D.addEdge(a17,a18,'x2')
#D.addEdge(a,a,'')
#D.addEdge(a,a,'')
#D.addEdge(a,a,'')
#D.addEdge(a,a,'')


print('digraph D {')
print(str(D))
print('}')


DxH1=D.product(flower1)

print('digraph DxH1 {')
print(str(DxH1))
print('}')

