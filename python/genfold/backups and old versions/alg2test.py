from alg2a import *

F1=free_group(3,'a')
F2=free_group(2,'b')
F1.make_gens()
F2.make_gens()
h1=['a1','a1','A2']
h2=['b1','b1','b2','b2']
h3=['a1','a2','a3','a3','a2','a1']
h4=['b1','B2','B2','B1']
H1=subgroup('H1',[h1,h3],['u','v'])
H2=subgroup('H2',[h2,h4],['u','v'])

w=['a1','a2','A1','b2','b2','B1','a3','A2','a1','a1','B1','B1','A3','a1']

#print('###nf_in_list starts###')

#nf_in_list([['a1', 'a2', 'A1'], ['b2', 'b2', 'B1'], ['a3', 'A2', 'a1', 'a1'], ['B1', 'B1'], ['A3', 'a1']],F1,F2,H1,H2)

#print('###alg2_main starts###')

#alg2_main(w,F1,F2,H1,H2)

print('###alg2_main2 starts###')

alg2_main2(w,F1,F2,H1,H2)
