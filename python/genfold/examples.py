from alg1 import *

F1=free_group(3,"a")
G=free_group(2,"alpha")
h1=['a1','a1','a1']
h2=['a1','A2','a1','a1']
h3=['a2','a2','a1','a1','A2']
h4=['A2','A2','a1','a2','a1',]
#h5=['A2','A2',a'a2','a2']
#h6=['a2','a2','a2','a2','a2']
w=['A2','a1','a2']
y=['a1','a2','a2','A2','A1']
v=['b1','B1','b1','B2']
X=F1.mongens
#print("generators of X are ",X)
#F.is_element(v)
#print(F1.is_element(h1))
#F.is_element(w)
#print(F1.is_element(h2))
#print("now G\n")
Y=G.mongens
#print(Y)
#G.is_element(v)
#G.is_element(w)
FZ=free_group(4,"z")
H1=subgroup("H1",[h1,h2,h3,h4],FZ.gens)
#print(H1.coherent)
GH=H1.flower

H1.stallings()
S=H1.flower
print ("digraph {")
print (str(S))
print ("}")

T=bfs(S,)
N=T.forest()
#for v in S.vertices:
#	print("S vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)
#	print("S, output labels of outedges of ",v," are ", v.outedges_write)
#	print("S, output labels of inedges of ",v," are ", v.inedges_write)
D= S.double()
#print ("digraph {")
#print (str(D))
#print ("}")

DB=bfs(D,sorted(D.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
DF=DB.forest()
for v in D.vertices:
	print("D vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)

NF=Normal_form(S,['a1','a1','a1','A1','a1','a2','a3','A2','A3','A2','a1','a1','a1','a1','A3','a1','a1','a1'],DB).spit_out_nf()
print("NF =", element(['a1','a1','a1','A1','a1','a2','a3','A2','A3','A2','a1','a1','a1','a1','A3','a1','a1','a1']).word)
print("NF a,b,c =", NF[0],NF[1],NF[2]) 
print("or NF using map into Z's: a, b, c =", NF[3],NF[1],NF[4])

ww=['a1','a1','a2','a2','a3','A1','a2','a2','A2','a1','A2','A2','a1','A3','A3','A3']
vv=Normal_form(S,ww,DB).spit_out_nf()
print("vv is ", element(ww).word)
print("a,b,c =", vv[0],vv[1],vv[2])
print("or using map into Z's: a, b, c =", vv[3],vv[1],vv[4])
type2=Normal_form(S,['a1','a1','a1','a1','a2','a1','a2','a2'],DB).spit_out_nf() 
print("type 2 is ", element(['a1','a1','a1','a1','a2','a1','a2','a2']).word)
print("a,b,c =", type2[0],type2[1],type2[2])
print("or using map into Z's: a, yZ, b =", type2[3],type2[1],type2[4])
another=Normal_form(S,['a1','a1','a1','a1','a1','a1','a1','a1','a1','a4','a3','A2','a2','A3','A4','a1','A1','A1','A1','A1','A1','A1','A1','A1','A1'],DB).spit_out_nf()
print("another is ", element(['a1','a1','a1','a1','a1','a1','a1','a1','a1','a4','a3','A2','a2','A3','A4','a1','A1','A1','A1','A1','A1','A1','A1','A1','A1']).word)
print("another a,b,c =", another[0],another[1],another[2])
print("or another using map into Z's: a,b, c =", another[3],another[1],another[4])
new=Normal_form(S,['a1','a1','a1','a1','a2','a2','A1','A2','a1','A2','A1'],DB).spit_out_nf()
print("new is ", element(['a1','a1','a1','a1','a2','a2','A1','A2','a1','A2','A1']).word)
print("new a,b,c =", new[0],new[1],new[2])
print("or using map into Z's: a,b, c =", new[3],new[1],new[4])
aa=['a1','a1','a1','a1','a1','a1','a1','a1','a1','a4','a3','A2','a2','A3','A4','a1','A1','A1','A1','A1','A1','A1','A1','A1','A1']
print("aa is",element(aa).word)
aaa=Normal_form(S,aa,DB).spit_out_nf()
print("aaa a,b,c =", aaa[0],aaa[1],aaa[2])
print("or using map into Z's: a,b, c =", aaa[3],aaa[1],aaa[4])
cc=Normal_form(S,['a1','a1','a1','a1','a2','a3','A1','A2','A3','A2','A1'],DB).spit_out_nf()
print("cc is",element(['a1','a1','a1','a1','a2','a3','A1','A2','A3','A2','A1']).word)
print("a,b,c =", cc[0],cc[1],cc[2])
print("or using map into Z's: a,b, c =", cc[3],cc[1],cc[4])


#this is the example

tt=Normal_form(S,['A1','A1','A1','A1','A1','A1','A1','A1','A1','a2'],DB).spit_out_nf()
print("tt is ", element(['A1','A1','A1','A1','A1','A1','A1','A1','A1','a2']).word)
print("normal form of tt is a,b,c =", tt[0],tt[1],tt[2]) 
print("or using map into Z's: a,b, c =", tt[3],tt[1],tt[4])

H1.subgroup_free_gens=subgroup_basis(S)[1]
print("basis of H1",H1.subgroup_free_gens)
print("or", subgroup_basis(S)[0])

zw=['z2','z1','Z4','z1']
print("y word is", phi(H1,zw)[0])
print("error is", phi(H1,zw)[1])
print(len(zw))
print(len([]))
print(len(['x1']))
