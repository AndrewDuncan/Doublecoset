from alg2 import *
F1=free_group(2,'a')
F2=free_group(2,'b')
h1=['a2','A1']
h2=['a1','a1','a1']
h3=['a2','a1','a2']
h4=['A1','a2']
h5=['b2','B1']
h6=['b1','b1','b1']
h7=['b2','b1','b2']
h8=['B1','b2']
H1=subgroup('H1',[h1,h2,h3,h4],['z1','z2','z3','z4'])
H2=subgroup('H2',[h5,h6,h7,h8],['z1','z2','z3','z4'])

alg2_pre(H1,H2)

def amalg_test(w,n):
	for i in range(0,n+1):
		word=[]
		word.extend(w)
		for j in range (1,n):
			word.append('a1')
		print(word)
		word.append('a2')
		print(word)
		for j in range (1,n+1):
			word.append('A1')
		print(word)
		W=[]
		for c in w:
			W.append(c.swapcase())
		word.extend(W)
		print(word)
		word=listsplitter(word,F1.mongens,F2.mongens)
		amalg_word=amalgamate(word,F1,F2,H1,H2)
		print('n=',i,'\n',word,'becomes\n',amalg_word,'\n\n\n\n')
	return

n=input('Enter n:')
n=int(n)
#w=input('Enter w:')
#w=list(w)
w=['b1','a1']

amalg_test(w,n)
