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
H.addEdge(a3,a2,'z1')
H.addEdge(a3,a4,'x1')
H.addEdge(a2,a5,'x1')
H.addEdge(a1,a7,'z2')
H.addEdge(a1,a8,'y1')
H.addEdge(a8,a9,'z1')
H.addEdge(a7,a9,'y1')
H.addEdge(a7,a11,'z2')
H.addEdge(a9,a10,'z1')
H.addEdge(a11,a10,'y1')
H.addEdge(a11,a12,'x1')
H.addEdge(a12,a13,'x1')
H.addEdge(a13,a14,'x1')
H.addEdge(a11,a14,'z3')
H.addEdge(a14,a15,'x1')
H.addEdge(a15,a16,'z1')
H.addEdge(a16,a17,'z1')

print ("digraph H {")
print (str(H))
print ("}")

(F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2)=alg3_pre()
d1(H,F,Z)