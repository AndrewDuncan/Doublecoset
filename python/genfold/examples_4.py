from alg2 import *
F1=free_group(3,'x')
F2=free_group(4,'y')
#H1=subgroup('H1',[['x1','x1','x1'],['x2','x3','X2'],['x1','x2','x3']],['u','v','w'])
#H2=subgroup('H2',[['y2','y2'],['y3','y4'],['y1','y1','y3','Y1','y2']],['u','v','w'])
h1=['x1','x1','x1']
h2=['x2','x3','X2']
h3=['x1','x2','x3']
g1=['y2','y2']
g2=['y3','y4']
g3=['y1','y1','y3','Y1','y2']
#X=F1.mongens
#print(X)
#G.is_element(v)
#G.is_element(w)
FZ=free_group(3,"z")
H1=subgroup("H1",[h1,h2,h3],FZ.gens)
H2=subgroup("H2",[g1,g2,g3],FZ.gens)
#print(H1.coherent)
#GH=H1.flower
#print("root of GH", GH.root)

H1.stallings()
S1=H1.flower
H2.stallings()
S2=H2.flower
print ("digraph {")
print (str(S1))
print ("}")

T1=bfs(S1,)
T1.forest()
T2=bfs(S2,)
T2.forest()
#for v in S1.vertices:
#	print("S1 vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)
#	print("S1, output labels of outedges of ",v," are ", v.outedges_write)
#	print("S1, output labels of inedges of ",v," are ", v.inedges_write)
D1= S1.double()
D2= S2.double()
print ("digraph {")
print (str(D1))
print ("}")

DB1=bfs(D1,sorted(D1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
DF1=DB1.forest()
DB2=bfs(D2,sorted(D2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
DF2=DB2.forest()
for v in D1.vertices:
	print("D1 vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)


H1.subgroup_free_gens=subgroup_basis(S1)[1]
H2.subgroup_free_gens=subgroup_basis(S2)[1]
print("basis of H1",H1.subgroup_free_gens)
print("or", subgroup_basis(S1)[0])

print("basis of H2",H2.subgroup_free_gens)
print("or", subgroup_basis(S2)[0])


#zw=['z2','z1','Z3','z1']
#print("y word is", phi(H1,zw)[0])
#print("error is", phi(H1,zw)[1])
#print(len(zw))
#print(len([]))
#print(len(['x1']))
print("H1 name, gens, free_gens", H1.name, H1.subgp_gens, H1.subgroup_free_gens)
print("H2 name, gens, free_gens", H2.name, H2.subgp_gens, H2.subgroup_free_gens)
print("diff from here")
w=['x1','x2','y1','y1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
print(w, "after listsplitter and then")
w=amalgamate(w,F1,F2,H1,H2)
print(w)

w=['x1','x2','y1','y1','x1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
print(w, "after listsplitter and then")
w=amalgamate(w,F1,F2,H1,H2)
print(w)

w=['x1','x2','y1','y1','x1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
print(w, "after listsplitter and then")
w=amalgamate(w,F1,F2,H1,H2)
print(w)

