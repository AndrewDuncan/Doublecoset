from alg2 import *

F1=free_group(3,'x')
F2=free_group(4,'y')
FZ=free_group(3,'z')
H1=subgroup('H1',[['x1','x1','x1'],['x2','x3','X2'],['x1','x2','x3']],FZ.gens)
H2=subgroup('H2',[['y2','y2'],['y3','y4'],['y1','y1','y3','Y1','y2']],FZ.gens)

alg2_pre(H1)
alg2_pre(H2)
#
#print("H1 name, gens, free_gens", H1.name, H1.subgp_gens, H1.subgroup_free_gens)
#print("H2 name, gens, free_gens", H2.name, H2.subgp_gens, H2.subgroup_free_gens)

w=['x1','x2','y1','y1','x1','x1']
print(w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
print(w, "after listsplitter and then")
w=amalgamate(w,F1,F2,H1,H2)
print('after amalgamate', w)

w=['x1','x2','y1','y1','x1','x1','x1']
print('\n\n\n',w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
#print(w, "after listsplitter and then")
w=amalgamate(w,F1,F2,H1,H2)
print("after amalgamate", w,'\n')
#print('expected output: [\'x1\', \'x2\', \'y1\', \'y1\', \'y3\', \'y4\']')

#w=['x1','x2','y2','x1','x1','x1','y2']
#print(w,' becomes')
#w=listsplitter(w,F1.mongens,F2.mongens)
#print(w, "after listsplitter and then")
#w=amalgamate(w,F1,F2,H1,H2)
#print("after amalgamate", w,'\n')

w=['x1','x2','y1','y1','x1','x1','x1','Y4','Y1','Y2']
print('\n\n\n',w,' becomes')
w=listsplitter(w,F1.mongens,F2.mongens)
#print(w, "after listsplitter and then")
w=amalgamate(w,F1,F2,H1,H2)
print("after amalgamate", w,'\n')
#print('expected output:[\'x1\', \'x2\', \'x1\', \'x2\', \'x3\', \'X1\', \'X1\', \'X1\']')
