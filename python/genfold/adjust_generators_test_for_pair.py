from adjust_generators import *

#define the free groups F1, F2 and FZ, by giving the number of generators, and letter for the generators
F1=free_group(4,"x")
F2=free_group(2,"y")
FZ=free_group(4,"z")
#

#list generators hi, gi for the subgroups H1 and H2
#h1=['X1','x3','x4','X2']
#h2=['x2','X1','x3','x4','x2']
#h3=['x2','x2','x2']
#h4=['X2','x1','x3','x2']
#
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
g1=['y1','Y2']
g2=['y2','y1','y2']
g3=['y2','y2','y2']
g4=['Y2','y1']

#define the subgroups H1 and H2 using these generators and the generators of FZ (need to add validity tests here)
H1=subgroup('H1',[h1,h2,h3,h4],FZ.gens)
H2=subgroup('H2',[g1,g2,g3,g4],FZ.gens)

#make the Stallings folding and choose spanning tree for it, for H1 and H2
(flower1,double1,forest1,bfs1)=alg2_pre(H1)
(flower2,double2,forest2,bfs2)=alg2_pre(H2)

#for convenience group all the above in pairs
F=(F1,F2)
H=(H1,H2)
flower=(flower1,flower2)

print("flower 1")
for u in flower1.vertices:
    print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write)
    print(u,"inedgeslist", u.inedgesList)
    print(u, "outedgeslist", u.outedgesList,"\n\n")

#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='adjust_generators/'

#create graphs for each flower
output_graph_pair(flower,"flower",testfile)

Hgens=[h1,h2,h3,h4]
ac1=check_gens(H1,Hgens)
ac2=check_gens(H2,[g1,g2,g3,g4])
print("for subgroup 1 if the input generators equal the basis found by folding the next digit will be 0:", ac1)
print("for subgroup 1 if the input generators equal the basis found by folding the next digit will be 0:", ac2)
stall1=label_with_Zs(H1,flower1,Hgens) #relabel stallings folding with given gens/ Z labels - to set up search for required gens(in reality only do this if ac=1)
stall2=label_with_Zs(H2,flower2,[g1,g2,g3,g4])
stall=(stall1,stall2)

# Output new files to see effect of relabelling
output_graph_pair(stall,"stall",testfile)

#check to see that the new graph is connected and all edges have been used in reading gens
for k in(0,1):
    ec,cn=check_neilsen_reduced(stall[k])
    print( "k=",k, "edges covered", ec,"neilsen reduced =", cn)

#build up the new output labelling from the relabelled foldings stall
for k in (0,1):
    build_new_labelling(stall[k],FZ)

#using the new labellings construct a spanning tree for the stallings folding
for k in (0,1):
    print(stall[k].root)
    forced_bfs(stall[k])# use the new labels to make a new tree
    print("k=", k,"stall components", stall[k].components)

for k in (0,1):
    for v in stall[k].vertices:
        print("k=", k,"vertex ", v,"colour, length, time, parent, path",v.colour,v.length,v.time, v.parent,v.path)
        print("H subgroup_free_gens", H[k].subgroup_free_gens, "H.subgp_gens", H[k].subgp_gens)

for k in (0,1):
    print("k is", k)
    for u in stall[k].vertices:
        print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write,"\n")
        print(u,"inedgeslist", u.inedgesList,"\n")
        print(u, "outedgeslist", u.outedgesList,"\n\n")
        # reassign subgroup_free_gens, using the new spanning tree for the stallings folding
        H[k].subgroup_free_gens=subgroup_basis(stall[k])[1]
        print("New H subgroup_free_gens", H[k].subgroup_free_gens, " and H.subgp_gens", H[k].subgp_gens)
