from alg2 import *
F1=free_group(3,'a')
F2=free_group(2,'b')
h1=['a1','a2','a3']
h2=['a2','a1','A2','A1']
h3=['b1','b1','b1']
h4=['b1','b2','b2','b1']
H1=subgroup('H1',[h1,h2],['u','v'])
H2=subgroup('H2',[h3,h4],['u','v'])

w=['a1','a1','a2','B2','A3','b2','a1','a2']

#to remove print output leave last argument blank; otherwise set it to 1
alg2(w,F1,F2,H1,H2,1)
