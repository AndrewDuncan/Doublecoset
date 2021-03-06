from alg2 import *

Hname=input('Enter the name of the subgroup: ')
def subgroup_input():
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
	Hgens=[]
	for i in range(1,n+1):
		w=input('Enter generator number %s: ' % (i,))
		w=w.replace(' ','')
		w=w.split(",")
		print('w is ',w)
		Hgens=Hgens+w
	FZ=free_group(len(Hgens),"z")
	print(FZ.gens)
	H=subgroup(Hname,Hgens,FZ.gens)
	H.stallings()
	flower=H.flower
	T=bfs(flower,)
	T.forest()
	double=flower.double()
	bfs1=bfs(double,sorted(double.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	forest=bfs1.forest()
	H.subgroup_free_gens=subgroup_basis(flower)[0]
	test=0
	while test==0:
		if len(Hgens)>len(H.subgroup_free_gens):
			print('There are more elements in the generators than there are in the basis computed.')
			print('The generators are:\n',Hgens,'\nand the basis is:\n',H.subgroup_free_gens)
			n=len(H.subgroup_free_gens)
			Hgens=[]
			print('Please input %s generators for H' % (n,))
			for i in range(1,n+1):
				w=input('Enter the %s generator: ' % (i,))
				w=w.replace(' ','')
				w=w.split(",")
				print('w is ',w)
				Hgens=Hgens+w
				FZ=free_group(len(Hgens),"z")
			H=subgroup(Hname,Hgens,FZ.gens)
			H.stallings()
			flower=H.flower
			T=bfs(flower,)
			T.forest()
			double=flower.double()
			bfs1=bfs(double,sorted(double.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
			forest=bfs1.forest()
			H.subgroup_free_gens=subgroup_basis(flower)[0]
		else:
			test=1

	print('The generators of the subgroup are:\n',Hgens,'\nThe free generators and their corresponding \'z\' generators are:\n')

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
	while True:
		F=free_group_input()
		print('This free group has the generators\n',F.gens)
		ok=input('Is this ok? y/n: ')
		if ok=='y':
			return F
		elif ok!='n':
			print('Please respond by entering \'y\' or \'n\'')

