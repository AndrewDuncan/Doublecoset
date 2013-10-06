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
D.addEdge(a3,a2,'z1')
D.addEdge(a3,a4,'x1')
D.addEdge(a2,a5,'x1')
D.addEdge(a1,a7,'z2')
D.addEdge(a1,a8,'y1')
D.addEdge(a8,a9,'z1')
D.addEdge(a7,a9,'y1')
D.addEdge(a7,a11,'y1')
D.addEdge(a9,a10,'z1')
D.addEdge(a11,a10,'y1')
D.addEdge(a11,a12,'x1')
D.addEdge(a12,a13,'x2')
D.addEdge(a13,a14,'x2')
D.addEdge(a11,a14,'z3')
D.addEdge(a14,a15,'x1')
D.addEdge(a15,a16,'z1')
D.addEdge(a16,a17,'z1')

#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
testfile='alg3_test_'
print("name will be", testfile+"Delta")
# Open alg3_test_Delta_in.gv in write mode: this will be the graph above
with open(testfile+"Delta_in.gv", "w") as Del:
    Del.write("digraph D {\n") #and write to it
with open(testfile+"Delta_in.gv", "a") as Del: #then open it in append mode
    Del.write(str(D)) #and continue to write to it
    Del.write("}")
Del.close()

#(F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2)=alg3_pre()
#d1(D,F,Z)
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
#print("H1.subgroup_free_gens are ", H1.subgroup_free_gens)
H=(H1,H2)
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2
D1=d1(D,F,Z) # returnsdelta_k0[0],delta_k0[1],delta_z

# Open alg3_test_D0_1.gv in write mode
with open(testfile+"D0_1.gv", "w") as D01:
    D01.write("digraph D1_1 {\n") #and write to it
with open(testfile+"D0_1.gv", "a") as D01: #then open it in append mode
    D01.write(str(D1[0])) #and continue to write to it
    D01.write("}")
D01.close()
#print ("digraph D1_1 {")
#print (str(D1[0]))
#print ("}")

# Open alg3_test_D0_2.gv in write mode
with open(testfile+"D0_2.gv", "w") as D02:
    D02.write("digraph D1_2 {\n") #and write to it
with open(testfile+"D0_2.gv", "a") as D02: #then open it in append mode
    D02.write(str(D1[1])) #and continue to write to it
    D02.write("}")
D02.close()
#print ("digraph D1_2 {")
#print (str(D1[1]))
#print ("}")

# Open alg3_test_D0_Z.gv in write mode
with open(testfile+"D0_Z.gv", "w") as D0Z:
    D0Z.write("digraph D1_Z {\n") #and write to it
with open(testfile+"D0_Z.gv", "a") as D0Z: #then open it in append mode
    D0Z.write(str(D1[2])) #and continue to write to it
    D0Z.write("}")
D0Z.close()
#print ("digraph D1_Z {")
#print (str(D1[2]))
#print ("}")
delta_0=[D1[0],D1[1]]
flower=[flower1,flower2]
D2=d2(delta_0,Z,H,flower)

# Open alg3_test_D2_1.gv in write mode
with open(testfile+"D2_1.gv", "w") as D21:
    D21.write("digraph D2_1 {\n") #and write to it
with open(testfile+"D2_1.gv", "a") as D21: #then open it in append mode
    D21.write(str(D2[0])) #and continue to write to it
    D21.write("}")
D21.close()

# Open alg3_test_D2_2.gv in write mode
with open(testfile+"D2_2.gv", "w") as D22:
    D22.write("digraph D2_2 {\n") #and write to it
with open(testfile+"D2_2.gv", "a") as D22: #then open it in append mode
    D22.write(str(D2[1])) #and continue to write to it
    D22.write("}")
D22.close()
#print('digraph D2_1 {')
#print(str(D2[0]))
#print('}')
#print('digraph D2_2 {')
#print(str(D2[1]))
#print('}')
