from alg2 import *
F1=free_group(4,'a')
F2=free_group(5,'b')
h1=['a1','a1','a2','a2']
h2=['a1','A2','a3','A4']
h3=['b1','b1','b1']
h4=['B2','b3','b1','b1']
H1=subgroup('H1',[h1,h2],['u','v'])
H2=subgroup('H2',[h3,h4],['u','v'])

w=[['a1','a1'],['b2'],['a3'],['B4']]
w=['a1','a1','b2','a3','B4']
#w=[]
#w=['a1']
w=['a1','a1','A1','a1','a2','B3','B4','B3','B5','b1','a1','a2','A4','A3','A2','b1','b3','b3','b3','a1','a1','a1','a1','a1','A2']

alg2(w,F1,F2,H1,H2)

#amalgamate(w,F1,F2,H1,H2)
