from alg2_new import *

F3=free_group(3,'a')
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

(flower1,double1,forest1,bfs1)=alg2_pre(G1)
(flower2,double2,forest2,bfs2)=alg2_pre(G2)

NF=Normal_form(flower1,['a1','a1','a1','A1','a1','a2','a3','A2','A3','A2','a1','a1','a1','a1','A3','a1','a1','a1'],bfs1).spit_out_nf()
print("NF =", element(['a1','a1','a1','A1','a1','a2','a3','A2','A3','A2','a1','a1','a1','a1','A3','a1','a1','a1']).word)
print("NF a,b,c =", NF[0],NF[1],NF[2]) 
print("or NF using map into Z's: a, b, c =", NF[3],NF[1],NF[4])
##########################
#test using NF
w=['a1','a1','a1','A1','a1','a2','a3','A2','A3','A2','a1','a1','a1','a1','A3','a1','a1','a1']
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgam_normal_form(w,F3,F4,G1,G2)
#w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w[0], "and ", w[1],'\n')
##############
w=['b1', 'a1', 'a1', 'a1', 'a2', 'A1', 'A1', 'A1', 'b1', 'a1'] 
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgam_normal_form(w,F3,F4,G1,G2)
#w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w[0], "and ", w[1],'\n')

w=['b1', 'a1', 'a1', 'a1', 'a2', 'A1', 'A1', 'A1', 'B1', 'A1'] 
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgam_normal_form(w,F3,F4,G1,G2)
#w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w[0], "and ", w[1],'\n')



w=['b1', 'a1', 'a1', 'a1', 'a2', 'a2','A1', 'A1', 'A1', 'B1','b2', 'A1'] 
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgam_normal_form(w,F3,F4,G1,G2)
#w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w[0], "and ", w[1],'\n')

w1=[]
w2=['A1']
w=['b1']+w1+['a2']+w2+['B1']
print('n=0, w is', w)
w=listsplitter(w,F3.mongens,F4.mongens)
(w,v)=amalgam_normal_form(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w, "and ", v,'\n')
for n in range(0,5):
	w1=w1+['a1']
	w2=w2+['A1']
	w=['b1']+w1+['a2']+w2+['B1']
	w1=element(w1).word
	w2=element(w2).word
	print('n, w is', n+1, w)
	w=listsplitter(w,F3.mongens,F4.mongens)
	(w,v)=amalgam_normal_form(w,F3,F4,G1,G2)
	print(" and after amalgam_normal_form w and v are", w, "and ", v,'\n')

w=['b2','b1','B2','B2','a2']
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgam_normal_form(w,F3,F4,G1,G2)
#w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w[0], "and ", w[1],'\n')

w=['a2','b1','B2']
print('\n\n\n',w,' becomes')
w=listsplitter(w,F3.mongens,F4.mongens)
#print(w, "after listsplitter and then")
w=amalgam_normal_form(w,F3,F4,G1,G2)
#w=amalgamate(w,F3,F4,G1,G2)
print(" and after amalgam_normal_form w and v are", w[0], "and ", w[1],'\n')
