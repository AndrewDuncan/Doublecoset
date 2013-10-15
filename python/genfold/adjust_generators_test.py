from adjust_generators import *

#define the free groups F1, F2 and FZ, by giving the number of generators, and letter for the generators
F1=free_group(4,"x")
#FZ=free_group(3,"z")
#
# Enter a free generating set for H
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

Hgens=[h1,h2,h3,h4]#,h5]

#check that the rank of FZ is equal to the length of FZ
#FZ=numbers_of_gens_of_subgroup(Hgens,FZ)    
#OR set the rank of FZ equal to the number of generators in Hgens
FZ=free_group(len(Hgens),"z")

#construct the flower automaton for the subgroup H
Hname='H'
H=subgroup(Hname,Hgens,FZ.gens)
#print("H name, subgp_gens flower coherent subgp_free_gens basis", H.name,"\n", H.subgp_gens,"\n", H.flower,"\n", H.coherent,"\n",H.subgp_free_gens,"\n", H.basis)

#make the Stallings folding for H and choose spanning tree for it
(flower,double,forest,bfs)=alg2_pre(H)
#print("flower ")
#for u in flower.vertices:
#    print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write)
#    print(u,"inedgeslist", u.inedgesList)
#    print(u, "outedgeslist", u.outedgesList,"\n\n")

(H,FZ)=check_Hgens_against_computed_basis(H,FZ)

#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='adjust_generators/'

#create graphs for each flower
output_graph_file(flower,"flower",testfile+"flower")

#Hgens=[h1,h2,h3,h4,h5]
ac=check_gens(H,Hgens)
print("if the input generators equal the basis found by folding the next digit will be 0:", ac)
if ac==1:
    stall=label_with_Zs(H,flower,Hgens) #relabel stallings folding with given gens/ Z labels - to set up search for required gens(in reality only do this if ac=1)

    # Output new file to see effect of relabelling
    output_graph_file(stall,"stall",testfile+"stall")
    #check to see that the new graph is connected and all edges have been used in reading gens
    ec,cn=check_neilsen_reduced(stall)
    print("edges covered", ec,"neilsen reduced =", cn)#

    #build up the new output labelling from the relabelled foldings stall
    build_new_labelling(stall,FZ)

    #using the new labellings construct a spanning tree for the stallings folding
    print(stall.root)
    forced_bfs(stall)# use the new labels to make a new tree
    print("stall components", stall.components)

    for v in stall.vertices:
        print("vertex ", v,"colour, length, time, parent, path",v.colour,v.length,v.time, v.parent,v.path)
        print("H subgroup_free_gens", H.subgroup_free_gens, "H.subgp_gens", H.subgp_gens)

        for u in stall.vertices:
            print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write,"\n")
            print(u,"inedgeslist", u.inedgesList,"\n")
            print(u, "outedgeslist", u.outedgesList,"\n\n")

    # reassign subgroup_free_gens, using the new spanning tree for the stallings folding
    H.subgroup_free_gens=subgroup_basis(stall)[1]
    print("New H subgroup_free_gens", H.subgroup_free_gens, " and H.subgp_gens", H.subgp_gens,"H.subgp_free_gens ", H.subgp_free_gens)
    confirm()



def confirm():
    ok=''
    while True:
        ok=input('Is this ok? y/n: ')
        if ok.lower()=='y':
            return(1)
        elif ok.lower()=='n':
            return(0)
        else:
            print('Please respond by entering \'y\' or \'n\'')
