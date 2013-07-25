from alg2 import *

def subgroup_input():
	Hname=input('Enter the name of the subgroup: ')
	while True:
		try:
			n=input('How many generators does this subgroup have? ')
			n=int(n)
			if n < 0:
				n=''
			int(n)
			break
		except ValueError:
			print('The number of generators must be a non-negative integer.')
	Hgens=genr_input(n)
	FZ=free_group(len(Hgens),"z")
	#print(FZ.gens)
	H=subgroup(Hname,Hgens,FZ.gens)
	(flower1,forest1)=setup_subgroup(H)
	H.subgroup_free_gens=subgroup_basis(flower1)[0]
	test=0
	while test==0:
		if len(Hgens)>len(H.subgroup_free_gens):
			print('The generators are:\n',Hgens,'\nand the basis is:\n',H.subgroup_free_gens)
			print('There are more elements in the generators than the rank computed.')
			print('Please enter a free generating set of size %s' % (n,))
			#n=len(H.subgroup_free_gens)
			#Hgens=[]
			#print('Please input %s generators for H' % (n,))
			Hgens=genr_input(n)
			H=subgroup(Hname,Hgens,FZ.gens)
			(flower1,forest1)=setup_subgroup(H)
			#H.stallings()
			#flower=H.flower
			#T=bfs(flower,)
			#T.forest()
			#double=flower.double()
			#bfs1=bfs(double,sorted(double.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
			#forest=bfs1.forest()
			H.subgroup_free_gens=subgroup_basis(flower1)[0]
		else:
			test=1
	#print('The generators of the subgroup are:\n',Hgens,'\nThe free generators and their corresponding \'z\' generators are:\n')
	#for i in range(0,len(H.subgroup_free_gens)):
	#	print(H.subgroup_free_gens[i][0],FZ.gens[i])
	print('The generators are:\n',Hgens,'The free generators and their corresponding \'z\' generators are:')
	for i in range(0,len(H.subgroup_free_gens)):
		print(H.subgroup_free_gens[i][0],FZ.gens[i])
	k=confirm()
	return (k,H)
	
def confirm():
	ok=''
	while True:
		ok=input('Is this ok? y/n: ')
		if ok=='y':
			return(1)
		elif ok=='n':
			return(0)
		else:
			print('Please respond by entering \'y\' or \'n\'')

def enter_subgroup():
	t=0
	while t==0:
		tt=subgroup_input()
		t=tt[0]
	return tt[1]

def genr_input(n):
	nn=int(n)
	Hgens=[]
	for i in range(1,nn+1):
		w=input('Enter generator number %s: ' % (i,))
		w=w.replace(' ','')
		w=w.split(",")
		print('w is ',w)
		Hgens.append(w)
	return(Hgens)

def setup_subgroup(H1):
	H1.stallings()
	flower1=H1.flower
	T1=bfs(flower1,)
	T1.forest()
	return(flower1,T1)

#enter_subgroup()

def free_group_input():
	r=input('Enter the letter to represent the free group: ')
	while True:
		try:
			n=input('Enter the rank of the free group: ')
			n=int(n)
			if n < 1:
				n=''
			int(n)
			break
		except ValueError:
			print('The number of generating elements must be a positive integer.')
	F=free_group(n,r)
	return F


def enter_free_group():
	ok=''
	F=free_group_input()
	while True:
		print('This free group has the generators\n',F.gens)
		ok=input('Is this ok? y/n: ')
		if ok=='y':
			return F
		elif ok=='n':
			F=free_group_input()
		else:
			print('Please respond by entering \'y\' or \'n\'')

#enter_free_group()
