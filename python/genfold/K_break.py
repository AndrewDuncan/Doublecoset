from K import *


##############Dothisfor 1,2
testfile='ex_paper/H1/'

#define the free group F, by giving the number of generators, and letter for the generators
F1=free_group(3,"x")
#
#Choose the subgroup name
Hname='H1'
# Enter a free generating set for the subgroup
#
h1=['x1','x1','x1']
h2=['x2','x3','X2']
h3=['x1','x2','x3']

#make the generators into a list
Hgens=[h1,h2,h3]

#check that the elements of Hgens are in the free group F
generators_in_free_group(F1,Hgens)

#find the folding corresponding to the generators entered(testfile here is needed only for testing and can be removed later)
(H1,FZ)=construct_required_folding(Hname,Hgens,testfile,F1)
#################
rankZ=len(FZ.gens)
##################
testfile='ex_paper/H2/'

#define the free group F, by giving the number of generators, and letter for the generators
F2=free_group(4,"y")
#
#Choose the subgroup name
Hname='H2'
# Enter a free generating set for the subgroup
#
g1=['y1','y1']
g2=['y3','y4']
g3=['y1','y1','y3','Y1','y2']
#make the generators into a list
Hgens=[g1,g2,g3]

#check that the elements of Hgens are in the free group F
#generators_in_free_group(F2,Hgens)

#find the folding corresponding to the generators entered(testfile here is needed only for testing and can be removed later)
(H2,FZ)=construct_required_folding(Hname,Hgens,testfile,F2)
####################
#make sure both subgroups have the same rank
if rankZ!=len(FZ.gens):
    error_message="Exiting: the two subgroups entered must have the same rank"
    sys.exit(error_message)
##################

F=(F1,F2)
H=(H1,H2)
flower1=H1.flower
flower2=H2.flower
flower=(flower1,flower2)
#
#reset testfile name
testfile='ex_ paper/'

