from alg1a import *

#w=element(['A1','A1','a1','A1','a1','A1','a1'])
#q=element(['x','X','x','y','x','X','x'])
#u=w.freely_reduce()
#x=q.freely_reduce()
#v=w.inverse()
#z=q.inverse()
#print('q =', q)
#print('u =', u)
#print('v =', v)
#print('z =', z)
#F1=free_group(26,"alpha")
F=free_group(2,"a")
#print(F1.is_element(u))
#print(F.is_element(u))
#print(F1.is_element(z))
#print(F.is_element(z))
#print(F1.mongens)
#XX= F.mongens
#print(XX)
h1=['a2','A1']
h2=['a2','a2','a2']
h3=['a2','a1','a2']
h4=['A2','a1']
FZ=free_group(4,"z")
#print(FZ.gens)
H1=subgroup("H1",[h1,h2,h3,h4],["u","v","w","x"])
H=subgroup("H",[h1,h2,h3,h4],FZ.gens)
RH=H.flower
H.stallings()
SH=H.flower
T=bfs(SH,).forest()
D= SH.double()
DB=bfs(D,sorted(D.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
DF=DB.forest()
w=['a2','A1']
n=5
print("at v = 0, w is ", w)
for v in range(0,n):
	NF=Normal_form(SH,w,DB).spit_out_nf()
	print("with v =",v)
	print("NF a,b,c =", NF[0],NF[1],NF[2])
	print("or NF using map into Z's: a, b, c =", NF[3],NF[1],NF[4])
	w.append('A1')
	w.insert(0,'a1')
	print("at v =",v+1, "w is ", w)

#NF=Normal_form(SH,w,DB).spit_out_nf()

#for v in SH.vertices:
#	print("S vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)
#	print("S, output labels of outedges of ",v," are ", v.outedges_write)
#	print("S, output labels of inedges of ",v," are ", v.inedges_write)
#
#
#for v in D.vertices:
#	print("D vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)
#
#
#print ("digraph SH {")
#print (str(SH))
#print ("}")

#print("NF a,b,c =", NF[0],NF[1],NF[2])
#print("or NF using map into Z's: a, b, c =", NF[3],NF[1],NF[4])
