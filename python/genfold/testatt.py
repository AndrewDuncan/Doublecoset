from alg3 import *

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
a15=D.addVertex(15)
a16=D.addVertex(16)
a17=D.addVertex(17)
D.addEdge(a1,a6,'x1')
D.addEdge(a1,a2,'y1')

for v in D.vertices:
    v.original=1

a18=D.addVertex(18)
if not hasattr(a18,'original'):
    print("ooh")
else:
    print("ah")
