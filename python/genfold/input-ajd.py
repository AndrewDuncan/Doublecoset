from alg1 import *
from alg2 import *

def subgroup_input():
	n=input('How many generators does this subgroup have? ')
	Hgens=genr_input(n)
	#Hname=Hdesc[0]
	H_free_gens=setup_subgroup(Hname,n,Hgens)
	print("free gens",H_free_gens)
	print('lengths', len(Hgens), len(H_free_gens))
	test=0
	while test==0:
		if len(Hgens)>len(H_free_gens):
			print('The generators are:\n',Hgens,'\nand the basis computed is:\n',H_free_gens)
			print('There are more elements in the generators than there are in the basis computed.')
			print('Please enter a free generating set of size', n)
			#n=len(H_free_gens)
			Hgens=genr_input(n)
			#Hname=Hdesc[0]
			#Hgens=Hdesc[1]
			H_free_gens=setup_subgroup(Hname,n,Hgens)
			
		else:
			test=1
	print('The generators are:\n',Hgens,'\nand the basis computed is:\n',H_free_gens)
	k=confirm()
	return k
	
def confirm():
	k=2
	while k==2:
		ok=input('Is this ok? y/n: ')
		if ok=='y':
			return(1)
		elif ok=='n':
			return(0)
		else:
			print('Please respond by entering \'y\' or \'n\'')
			ok=input('Is this ok? y/n: ')


def genr_input(n):
	#Hname=input('Enter the name of the subgroup: ')
	nn=int(n)
	Hgens=[]
	for i in range(1,nn+1):
		w=input('Enter generator number %s: ' % (i,))
		w=w.split(",")
		print('w is ',w)
		#Hgens.append(w)
		Hgens=Hgens+w
	return(Hgens)

def setup_subgroup(Hname,n,inputs):
	#Hname=inputs[0]
	Hgens=inputs
	FZ=free_group(len(Hgens),"z")
	H=subgroup(Hname,Hgens,FZ.gens)
	H.stallings()
	flower=H.flower
	T=bfs(flower,)
	T.forest()
	double=flower.double()
	dbfs=bfs(double,sorted(double.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	forest=dbfs.forest()
	free_gens=subgroup_basis(flower)[0]
	return(free_gens)

def enter_subgroup():
	t=0
	while t==0:
		t=subgroup_input()
	return

Hname=input('Enter the name of the subgroup: ')
enter_subgroup()
