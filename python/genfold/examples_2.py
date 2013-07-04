from alg1 import *
F1=free_group(3,'a')
F2=free_group(2,'b')
h1=['a1','a2','a3']
h2=['a2','a1','A2','A1']
h3=['b1','b1','b1']
h4=['b1','b2','b2','b1']
H1=subgroup('H1',[h1,h2],['u','v'])
H2=subgroup('H2',[h3,h4],['u','v'])

#w1=['a1','a1','a2']
w=[['a1','a1','a2'],['B2'],['A3'],['b2'],['a1','a2']]
#alg2(w,F1,F2,H1,H2)
H1.stallings()
H2.stallings()
S1=H1.flower
S2=H2.flower
bfs(S1,)
#N1=T1.forest()
bfs(S2,)
#N2=T2.forest()
D1= S1.double()
D2= S2.double()
D1B=bfs(D1,sorted(D1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
D1F=D1B.forest()
D2B=bfs(D2,sorted(D2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
D2F=D2B.forest()
#NF=Normal_form(S1,w,D1B).spit_out_nf()
s=0
for i in range(0,5):
	if s==0:
		NF=Normal_form(S2,w[i],D2B).spit_out_nf()
		print("i is ", i, "s is", s,"w[i] =", element(w[i]).word)
		print("nf of w is a,b,c =", NF[0],NF[1],NF[2]) 
		print("or nf of w using map into Z's: a, b, c =", NF[3],NF[1],NF[4])
		s=1
	else:
		NF=Normal_form(S1,w[i],D1B).spit_out_nf()
		print("i is ", i, "s is", s,"w[i] =", element(w[i]).word)
		print("nf of w is a,b,c =", NF[0],NF[1],NF[2]) 
		print("or nf of w using map into Z's: a, b, c =", NF[3],NF[1],NF[4])
		s=0
