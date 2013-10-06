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
D.addEdge(a1,a2,'x1')
D.addEdge(a3,a2,'z1')
D.addEdge(a3,a4,'x1')
D.addEdge(a2,a5,'x1')
D.addEdge(a1,a7,'z2')
D.addEdge(a1,a8,'y1')
D.addEdge(a8,a9,'z1')
D.addEdge(a7,a9,'y1')
D.addEdge(a7,a11,'y1')
D.addEdge(a9,a10,'z1')
D.addEdge(a9,a11,'y1')
D.addEdge(a11,a10,'z1')
D.addEdge(a11,a12,'z1')
D.addEdge(a12,a13,'x2')
D.addEdge(a13,a14,'X2')
D.addEdge(a11,a14,'z1')
D.addEdge(a14,a15,'x1')
D.addEdge(a15,a16,'z1')
D.addEdge(a16,a17,'z1')

D.root=a1

#set v.original for all vertices so far (to either 0 or 1)
for v in D.vertices:
    v.original =0
    v.nu_im={v.label}# and set it's nu_im

#now add some new vertices, which we will not make "original"
a21=D.addVertex(21)
a22=D.addVertex(22)
a23=D.addVertex(23)
a24=D.addVertex(24)
a25=D.addVertex(25)
a26=D.addVertex(26)
a27=D.addVertex(27)
a28=D.addVertex(28)

#for some new vertices set v.original to 0 (which says "not original"), or 1 and  for others leave it unset
a21.original=1
a22.original=1
a23.original=1
a24.original=1

#for some new vertices set nu_im: for others leave it unset
a21.nu_im={a21.label}
a23.nu_im={a22.label}
a25.nu_im={a23.label}
a27.nu_im={a27.label}

D.addEdge(a1,a22,'z1')
D.addEdge(a1,a21,'z1')
D.addEdge(a1,a23,'z1')

D.addEdge(a2,a21,'z1')
D.addEdge(a2,a24,'z1')
D.addEdge(a2,a28,'z1')

D.addEdge(a10,a21,'Z1')

D.addEdge(a12,a28,'x1')

D.addEdge(a25,a26,'y1')
D.addEdge(a25,a27,'y1')

# Open folding_test_1.gv in write mode
with open("folding_test_1.gv", "w") as fo1:
    fo1.write("digraph D {\n") #and write to it
with open("folding_test_1.gv", "a") as fo1: #then open it in append mode
    fo1.write(str(D)) #and continue to write to it
    fo1.write("}")
fo1.close()


for v in D.vertices:
    if hasattr(v, 'original') and hasattr(v,'nu_im'):
        print((v.name,v.label)," original and nu_im are", v.original, v.nu_im)
    elif hasattr(v, 'original') and not hasattr(v,'nu_im'):
        print((v.name,v.label)," original and nu_im are", v.original, " and unset")
    elif not hasattr(v, 'original') and hasattr(v,'nu_im'):
        print((v.name,v.label)," original and nu_im are",  " unset and ", v.nu_im)
    else: 
        print((v.name,v.label)," original and nu_im are both unset")

go = True
while go: #fold D
    go = D.fold()
with open("folding_test_2.gv", "w") as fo2:
    fo2.write("digraph D {\n")
with open("folding_test_2.gv", "a") as fo2:
    fo2.write(str(D))
    fo2.write("}")
fo2.close()
print("After folding\n")
for v in D.vertices:
    if hasattr(v, 'original') and hasattr(v,'nu_im'):
        print((v.name,v.label)," original and nu_im are", v.original, v.nu_im)
    elif hasattr(v, 'original') and not hasattr(v,'nu_im'):
        print((v.name,v.label)," original and nu_im are", v.original, " and unset")
    elif not hasattr(v, 'original') and hasattr(v,'nu_im'):
        print((v.name,v.label)," original and nu_im are",  " unset and ", v.nu_im)
    else: 
        print((v.name,v.label)," original and nu_im are both unset", v.outedges)

