from alg2 import *

F3=free_group(2,'a')
F4=free_group(2,'b')
FZ=free_group(4,'z')
u1=['a2','A1']
u2=['a2','a2','a2']
u3=['a2','a1','a2']
u4=['A1','a2']
v1=['b2','B1']
v2=['b2','b2','b2']
v3=['b2','b1','b2']
v4=['B1','b2']
G1=subgroup('G1',[u1,u2,u3,u4],FZ.gens)
G2=subgroup('G2',[v1,v2,v3,v4],FZ.gens)

alg2_pre(G1)
alg2_pre(G2)

w=['b1', 'a1', 'a1', 'a1', 'a2', 'A1', 'A1', 'A1', 'B1', 'A1'] 
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgamate(w,F3,F4,G1,G2)
print("after amalgamate", w,'\n')

w1=[]
w2=['A1']
w=['b1']+w1+['a2']+w2+['B1']
print('n=0, w is', w)
w=listsplitter(w,F3.mongens,F4.mongens)
w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgamate w is", w,'\n')
for n in range(0,5):
	w1=w1+['a1']
	w2=w2+['A1']
	w=['b1']+w1+['a2']+w2+['B1']
	w1=element(w1).word
	w2=element(w2).word
	print('n, w', n+1, w)
	w=listsplitter(w,F3.mongens,F4.mongens)
	w=amalgamate(w,F3,F4,G1,G2)
	print(" and after amalgamate w is", w,'\n')
