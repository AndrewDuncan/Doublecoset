from alg2 import *

def subgroup_input():
	Hname=input('Enter the name of the subgroup: ')
	n=input('How many generators does this subgroup have? ')
	n=int(n)
	Hgens=[]
	for i in range(1,n+1):
		w=input('Enter the %s generator: ' % (i,))
		w.split(",")
		print('w is ',w)
		Hgens.append(w)
	FZ=free_group(len(Hgens),"z")
	H=subgroup(Hname,Hgens,FZ.gens)
	H.stallings()
	flower=H.flower
	T=bfs(flower,)
	T.forest()
	H.subgroup_free_gens=subgroup_basis(flower)[0]
	test=0
	while test==0:
		if len(Hgens)>len(H.subgp_free_gens):
			print('There are more elements in the generators than there are in the basis computed.')
			print('The generators are:\n',Hgens,'\nand the basis is:\n',H.subgp_free_gens)
			n=len(H.subgp_free_gens)
			Hgens=[]
			print('Please input %s generators for H' % (n,))
			for i in range(1,n+1):
				w=input('Enter the %s generator: ' % (i,))
				w.split(",")
				print('w is ',w)
				Hgens.append(w)
				FZ=free_group(len(Hgens),"z")
			H=subgroup(Hname,Hgens,FZ.gens)
			H.stallings()
			flower=H.flower
			T=bfs(flower,)
			T.forest()
			H.subgroup_free_gens=subgroup_basis(flower)[0]
		else:
			test=1
	print('The generators of H are:\n',Hgens,)
	#output a message reporting this fact,
	#list both Hgens and the free_gens found
	#tell the user to input len(H.subgroup_free_gens) generators for H

subgroup_input()
