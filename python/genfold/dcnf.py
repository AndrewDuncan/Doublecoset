from alg2 import *
from input import * #this is temporary until input is incorporated into alg1

print('First, enter the details of the first free group')
F1=enter_free_group()
print('Now enter the details of the second free group')
F2=enter_free_group()
while F1.alpha.lower()==F2.alpha.lower():
	print('The two free groups are both represented by the letter',F1.alpha)
	print('Please re-enter the details of the second free group')
	F2=enter_free_group()
print('Enter the details of the first subgroup')
H1=enter_subgroup()
print('Now enter the details of the second subgroup')
H2=enter_subgroup() #need to test whether both subgroups have the same number of generators

(flower1,double1,forest1)=alg2_pre(H1)
(flower2,double2,forest2)=alg2_pre(H2)

while True:
	w=input('Enter the word you wish to put into normal form, or enter \'done\' to finish:\n')
	if w.lower()=='done':
		break
	w=w.replace(' ','')
	w=w.split(',')
	w=listsplitter(w,F1.mongens,F2.mongens)
	w=amalgamate(w,F1,F2,H1,H2)
	print('After amalgamation the word is:',w)
#	w=reducelist(w)
#	w=nf_in_list(w,flower1,flower2,double1,double2,F1,F2)
#	print('The word in double coset normal form is:',w)
#	w=joiner(w)
#	w=popper(w)
#	w=element(w).word
#	print('which is the same as:',w)
