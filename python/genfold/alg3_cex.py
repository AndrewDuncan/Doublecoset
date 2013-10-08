from alg3 import *

D=Graph()
a1=D.addVertex(1)
a2=D.addVertex(2)
a3=D.addVertex(3)
a4=D.addVertex(4)
a5=D.addVertex(5)
D.addEdge(a1,a2,'z1')
D.addEdge(a2,a3,'z2')
D.addEdge(a4,a3,'z3')
D.addEdge(a4,a5,'y2')
D.addEdge(a5,a1,'x2')
D.addEdge(a1,a1,'z4')
#
testfile='cex/'
# Open alg3_test_Delta_in.gv in write mode: this will be the graph above
with open(testfile+"Delta_in.gv", "w") as Del:
    Del.write("digraph D {\n") #and write to it
with open(testfile+"Delta_in.gv", "a") as Del: #then open it in append mode
    Del.write(str(D)) #and continue to write to it
    Del.write("}")
Del.close()

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
print("flower1")
(flower1,double1,forest1,bfs1)=alg2_pre(H1)
print("flower2")
(flower2,double2,forest2,bfs2)=alg2_pre(H2)

# Open alg3_test_flower1.gv in write mode: this will be the graph above
with open(testfile+"flower1.gv", "w") as flo1:
    flo1.write("digraph S1 {\n") #and write to it
with open(testfile+"flower1.gv", "a") as flo1: #then open it in append mode
    flo1.write(str(flower1)) #and continue to write to it
    flo1.write("}")
flo1.close()

# Open alg3_test_flower2.gv in write mode: this will be the graph above
with open(testfile+"flower2.gv", "w") as flo2:
    flo2.write("digraph S2 {\n") #and write to it
with open(testfile+"flower2.gv", "a") as flo2: #then open it in append mode
    flo2.write(str(flower2)) #and continue to write to it
    flo2.write("}")
flo2.close()


#print("H1.subgroup_free_gens are ", H1.subgroup_free_gens)
H=(H1,H2)
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2
print("now D0")
D0=MakeComps(D,F,Z) # returnsdelta_k0[0],delta_k0[1],delta_z

# Open alg3_test_D0_1.gv in write mode
with open(testfile+"D0_1.gv", "w") as D01:
    D01.write("digraph D1_1 {\n") #and write to it
with open(testfile+"D0_1.gv", "a") as D01: #then open it in append mode
    D01.write(str(D0[0])) #and continue to write to it
    D01.write("}")
D01.close()
#print ("digraph D1_1 {")
#print (str(D1[0]))
#print ("}")

# Open alg3_test_D0_2.gv in write mode
with open(testfile+"D0_2.gv", "w") as D02:
    D02.write("digraph D1_2 {\n") #and write to it
with open(testfile+"D0_2.gv", "a") as D02: #then open it in append mode
    D02.write(str(D0[1])) #and continue to write to it
    D02.write("}")
D02.close()

# Open alg3_test_D0_Z.gv in write mode
with open(testfile+"D0_Z.gv", "w") as D0Z:
    D0Z.write("digraph D1_Z {\n") #and write to it
with open(testfile+"D0_Z.gv", "a") as D0Z: #then open it in append mode
    D0Z.write(str(D0[2])) #and continue to write to it
    D0Z.write("}")
D0Z.close()

delta_0=[D0[0],D0[1]] # take the first two components of D0, that is the X1 and X2 components
flower=[flower1,flower2]
print("now D1")
D1=Mod1(delta_0,Z,H,flower)


# Open alg3_test_D1_1.gv in write mode
with open(testfile+"D1_1.gv", "w") as D11:
    D11.write("digraph D1_1 {\n") #and write to it
with open(testfile+"D1_1.gv", "a") as D11: #then open it in append mode
    D11.write(str(D1[0])) #and continue to write to it
    D11.write("}")
D11.close()

# Open alg3_test_D1_2.gv in write mode
with open(testfile+"D1_2.gv", "w") as D12:
    D12.write("digraph D1_2 {\n") #and write to it
with open(testfile+"D1_2.gv", "a") as D12: #then open it in append mode
    D12.write(str(D1[1])) #and continue to write to it
    D12.write("}")
D12.close()

print("now D2")
D2=Mod2(D1,flower)

# Open alg3_test_P_1_1.gv in write mode
with open(testfile+"P_1_1.gv", "w") as P11:
    P11.write("digraph P11 {\n") #and write to it
with open(testfile+"P_1_1.gv", "a") as P11: #then open it in append mode
    P11.write(str(D2[0][0])) #and continue to write to it
    P11.write("}")
P11.close()
# Open alg3_test_P_1_2.gv in write mode
with open(testfile+"P_1_2.gv", "w") as P12:
    P12.write("digraph P12 {\n") #and write to it
with open(testfile+"P_1_2.gv", "a") as P12: #then open it in append mode
    P12.write(str(D2[0][1])) #and continue to write to it
    P12.write("}")
P12.close()

# Open alg3_test_D2_1.gv in write mode
with open(testfile+"D2_1.gv", "w") as D21:
    D21.write("digraph D2_1 {\n") #and write to it
with open(testfile+"D2_1.gv", "a") as D21: #then open it in append mode
    D21.write(str(D2[2][0])) #and continue to write to it
    D21.write("}")
D21.close()

# Open alg3_test_D2_2.gv in write mode
with open(testfile+"D2_2.gv", "w") as D22:
    D22.write("digraph D2_2 {\n") #and write to it
with open(testfile+"D2_2.gv", "a") as D22: #then open it in append mode
    D22.write(str(D2[2][1])) #and continue to write to it
    D22.write("}")
D22.close()

print("now D3")
D3=Mod3(D2[2],flower,D2[0])

# Open alg3_test_D3_1.gv in write mode
with open(testfile+"D3_1.gv", "w") as D31:
    D31.write("digraph D3_1 {\n") #and write to it
with open(testfile+"D3_1.gv", "a") as D31: #then open it in append mode
    D31.write(str(D3[0][0])) #and continue to write to it
    D31.write("}")
D31.close()

# Open alg3_test_D3_2.gv in write mode
with open(testfile+"D3_2.gv", "w") as D32:
    D32.write("digraph D3_2 {\n") #and write to it
with open(testfile+"D3_2.gv", "a") as D32: #then open it in append mode
    D32.write(str(D3[0][1])) #and continue to write to it
    D32.write("}")
D32.close()
