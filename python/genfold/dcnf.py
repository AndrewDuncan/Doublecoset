from alg1 import *
from input_ajd import * #this is temporary until input is incorporated into alg1

F1=enter_free_group()
F2=enter_free_group()
H1=enter_subgroup()
H2=enter_subgroup()

(flower1,double1,forest1)=alg2_pre(H1)
(flower2,double2,forest2)=alg2_pre(H2)

while True:
	w=input('Enter the word you wish to put into normal form, or enter \'done\' to finish:\n')
	if w.lower()=='done':
		break
	w=w.replace(' ','')
	w=w.split(',')
	w=listsplitter(w,F1.mongens,F2.mongens)
	w=amalgamate(w)
	w=reducelist(w)
	w=nf_in_list(w,flower1,flower2,double1,double2,F1,F2)
	print('The word in double coset normal form is:',w)
	w=joiner(w)
	w=popper(w)
	w=element(w).word
	print('which is the same as:',w)