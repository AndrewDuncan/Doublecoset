from alg3 import *

#print('digraph g1 {')
#print(str(g1))
#print('}')
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
H=(H1,H2)
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2
d1=phi(H1,['z1','z2','Z3'])
print('d1 = ', d1)
c1=element(d1[0]).word
c2=element(['y2','x2']).word
c=element(c1+c2).word
#r=element(['y2']).word
r=element(phi(H1,['z4'])[0]).word
C=element(c).inverse()
w=element(c1+c2+r+C).word
print('w = ',w)
w=popper(w)
print('w=popper(w)\n',w)
w=listsplitter(w,F1.mongens,F2.mongens)
nw=amalgam_normal_form(w,F1,F2,H1,H2)
print('normal form of w = ',nw)
for i in range(0,5):
	print('bongo')
