from alg2 import *
from input_ajd import * #temporary, will eventually be included in the above import

def alg3_pre():
	F1=enter_free_group()
	F2=enter_free_group()
	F=(F1,F2)
	H1=enter_subgroup()
	H2=enter_subgroup()
	(flower1,double1,forest1)=alg2_pre(H1)
	(flower1,double1,forest1)=alg2_pre(H2)
	if F1.rank>F2.rank:
		Z=free_group(F1.rank,'z')
	else:
		Z=free_group(F2.rank,'z')

def d1(delta,F1,F2,Z):
	delta_10=Graph(False,'Delta\' 1,0')
	delta_20=Graph(False,'Delta\' 2,0')
	delta_k0=(delta_10,delta_20)
	delta_z=Graph(False,'Delta Z')
	for k in (1,2):
		delta_k0[k-1]=delta
		for v in delta_k0[k-1].vertices: #part a
			for outedges in v.outedgesList:
				if the edge has a label in F[2-k]: ###
					remove the outedge from the vertex ###
			for inedges in v.inedgesList:
				if the edge has a label in F[2-k]: ###
					remove the inedge from the vertex ###
		for v in delta_k0[k-1]: #part b
			if len(v.inedgesList)+len(v.outedgesList)==1:
				if the edge has a label from Z: ###
					add edge to delta z ###
					remove edge from F[k-1] ###
		if k==1:
			delta_k0[1]=delta_k0[0]
		for v in delta_k0[k-1]:
			v.nu_im=('v') #part d
			v.label='({0},{1})'.format(v.label,k) #part c

#lines labeled with ### need to be rewritten