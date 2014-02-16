from copygraph import *
from alg3 import *

H=Graph()
a1=H.addVertex(1)
a2=H.addVertex(2)
a3=H.addVertex(3)
a4=H.addVertex(4)
a5=H.addVertex(5)
a6=H.addVertex(6)
a7=H.addVertex(7)
a8=H.addVertex(8)
a9=H.addVertex(9)
a10=H.addVertex(10)
a11=H.addVertex(11)
a12=H.addVertex(12)
a13=H.addVertex(13)
a14=H.addVertex(14)
a15=H.addVertex(15)
a16=H.addVertex(16)
a17=H.addVertex(17)
H.addEdge(a1,a6,'x1')
H.addEdge(a1,a2,'y1')
H.addEdge(a3,a2,'z')
H.addEdge(a3,a4,'x2')
H.addEdge(a2,a5,'X3')
H.addEdge(a1,a7,'z2')
H.addEdge(a1,a8,'y2')
H.addEdge(a8,a9,'z')
H.addEdge(a7,a9,'Y1')
H.addEdge(a7,a11,'z2')
H.addEdge(a9,a10,'z')
H.addEdge(a11,a10,'y3')
H.addEdge(a11,a12,'x')
H.addEdge(a12,a13,'x')
H.addEdge(a13,a14,'x')
H.addEdge(a11,a14,'z1')
H.addEdge(a14,a15,'x')
H.addEdge(a15,a16,'z')
H.addEdge(a16,a17,'x')
H.root=a1


F1=free_group(3,"y")
L=F1.mongens
#print("L is ", L)
#Cp=CopyGraph(H,['y1','y2','y3','Y1','Y2','Y3'])
Cp=CopyGraph(H,L)

#print("Cp is ", str(Cp), "verts", Cp.vertices)
#print("Cp root ",Cp.root)

same,diff=CompareGraphs(H,Cp)
print("same = ",same)
print("diff = ", diff)
print(str(H))
print(str(Cp))

for v in Cp.vertices:
	print("v is ", v," and has boundary ",v.boundary, " and label, name ",v.label, v.name)


print("Cp root ",Cp.root)
#print("atts", dir(H))
