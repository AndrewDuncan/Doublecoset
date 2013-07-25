from alg2 import *
from input_ajd import * #this is temporary until input is incorporated into alg1

#F=enter_free_group()
H=enter_subgroup()

(flower1,double1,forest1)=alg2_pre(H)
#double=H.flower.double()
while True:
	w=input('Enter the word you wish to put into normal form, or enter \'done\' to finish:\n')
	if w.lower()=='done':
		break
	w=w.replace(' ','')
	w=w.split(',')
	nf=Normal_form(flower1,w,double1).spit_out_nf()
	print('The normal form of this word is:')
	print(nf[0],nf[1],nf[2])
	print('or in terms of the z generators this is:')
	print(nf[3],nf[1],nf[4])

