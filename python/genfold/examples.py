from alg1a import *

F1=free_group(3,"alpha")
G=free_group(2,"alpha")
h1="aaa"
h2="aBaa"
h3="bbaaB"
h4="BBaba"
#h5="BBabb"
#h6="bbbbb"
w="Bab"
y="abbBA"
v=["b1","B1","b1","B2"]
F1.make_gens()
X=F1.mongens
print("generators of X are ",X)
#F.is_element(v)
print(F1.is_element(h1))
#F.is_element(w)
print(F1.is_element(h2))
print("now G\n")
G.make_gens()
Y=G.mongens
print(Y)
G.is_element(v)
G.is_element(w)
H1=subgroup("H1",[h1,h2,h3,h4],["u","v","w","x"])
print(H1.coherent)
GH=H1.make_flower()
print ("digraph {")
#print (str(GH))
print ("}")

#R=H.flower
#print ("digraph H.flower {")
#print (str(R))
#print ("}")
#
#go = True
#while go:
# go = R.fold()
#
#S=R
print("now H1 stallings")
H1.stallings()
S=H1.flower
print ("digraph {")
#print (str(S))
print ("}")

T=bfs(S,)
N=T.forest()
for v in S.vertices:
	print("S vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)
	print("S, output labels of outedges of ",v," are ", v.outedges_write)
	print("S, output labels of inedges of ",v," are ", v.inedges_write)
D= S.double()
print ("digraph {")
print (str(D))
print ("}")

DB=bfs(D,sorted(D.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
DF=DB.forest()
for v in D.vertices:
	print("D vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)

NF=Normal_form(S,"aaaAabcBCBaaaaCaaa",DB).spit_out_nf()
print("NF a,b,c =", NF[0],NF[1],NF[2])
print("or NF using map into Z's: a, b, c =", NF[3],NF[1],NF[4])

ww="aabbcAbbBaBBaCCC"
vv=Normal_form(S,ww,DB).spit_out_nf()
#print("a,b,c =", vv[0],vv[1],vv[2])
#print("or using map into Z's: a, b, c =", vv[3],vv[1],vv[4])
type2=Normal_form(S,"aaaaabc",DB).spit_out_nf()
#print("a,yZ,b =", type2[0],type2[1],type2[2])
#print("or using map into Z's: a, yZ, b =", type2[3],type2[1],type2[4])
another=Normal_form(S,"aaaaaaaaadcBbCDaAAAAAAAAA",DB).spit_out_nf()
#print("another a,b,c =", another[0],another[1],another[2])
#print("or another using map into Z's: a,b, c =", another[3],another[1],another[4])
new=Normal_form(S,"aaaabcABCBA",DB).spit_out_nf()
#print("a,b,c =", new[0],new[1],new[2])
#print("or using map into Z's: a,b, c =", new[3],new[1],new[4])
aa="aaaaaaaaadcBbCDaAAAAAAAAA"
#print(element(aa).freely_reduce())
cc=Normal_form(S,"aaaabcABCBA",DB).spit_out_nf()
#print("a,b,c =", cc[0],cc[1],cc[2])
#print("or using map into Z's: a,b, c =", cc[3],cc[1],cc[4])


#this is the example

tt=Normal_form(S,"AAAAAAAAAb",DB).spit_out_nf()
tt
print("a,b,c =", tt[0],tt[1],tt[2])

