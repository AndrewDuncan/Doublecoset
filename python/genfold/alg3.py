from alg2 import *
from input_ajd import * #temporary, will eventually be included in the above import

def alg3_pre():
	F1=enter_free_group()
	F2=enter_free_group()
	H1=enter_subgroup()
	H2=enter_subgroup()
	(flower1,double1,forest1)=alg2_pre(H1)
	(flower1,double1,forest1)=alg2_pre(H2)
	if F1.rank>F2.rank:
		Z=free_group(F1.rank,'z')
	else:
		Z=free_group(F2.rank,'z')

def d1(delta,k,F1,F2,Z):
	delta_k0=Graph(False,'Delta\' %s,0' % k)
	delta_z=Graph(False,'Delta Z')