from alg2 import *

F1=free_group(3,'x')
F2=free_group(4,'y')
H1=subgroup('H1',[['x1','x1','x1'],['x2','x3','X2'],['x1','x2','x3']],['u','v','w'])
H2=subgroup('H2',[['y2','y2'],['y3','y4'],['y1','y1','y3','Y1','y2']],['u','v','w'])

alg2_pre(H1,H2)

w=['x1','x2','y1','y1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
w=amalgamate(w,F1,F2,H1,H2)
print(w)

w=['x1','x2','y1','y1','x1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
w=amalgamate(w,F1,F2,H1,H2)
print(w)

w=['x1','x2','y1','y1','x1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
w=amalgamate(w,F1,F2,H1,H2)
print(w)
