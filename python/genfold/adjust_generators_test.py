from adjust_generators1 import *

#set verbose =1 to see lots of information and to 0 for a quiet run
verbose =1
#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='adjust_generators/'

#define the free group F, by giving the number of generators, and letter for the generators
F=free_group(4,"x")
#
#Choose the subgroup name
Hname='H'

#Enter the rank of the subgroup
Hrank=4
# Enter a free generating set for the subgroup
#h1=['X1','x3','x4','X2']
#h2=['x2','X1','x3','x4','x2']
#h3=['x2','x2','x2']
#h4=['X2','x1','x3','x2']
#
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
#h5=['x2','x1','x1']

#make the generators into a list
Hgens=[h1,h2,h3,h4]#,h5]

#find the folding corresponding to the generators entered
#
(H,FZ)=construct_required_folding(Hname,Hgens,testfile,F,Hrank,verbose)

#write the final folding as a graph
filename=testfile+"stallings.gv"
output_graph_file(H.flower,filename,"stallings",verbose)


#The original folding can be seen by running dot -Tpng on testfile+flower.gv and the final folding, by running dot on testfile+stallings.gv
#other properties of H can be seen by printing H.property, where property is something like subgroup_free_gens
 
