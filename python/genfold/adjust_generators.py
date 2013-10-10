from alg3 import *
#from alg2 import *
#from input import * #temporary, will eventually be included in the above import
#import copy
F1=free_group(4,"x")
F2=free_group(2,"y")
Z=free_group(4,"z")
F=(F1,F2)
h1=['X1','x3','x4','X2']
h2=['x2','X1','x3','x4','x2']
h3=['x2','x2','x2']
h4=['X2','x1','x3','x2']
g1=['y1','Y2']
g2=['y2','y1','y2']
g3=['y2','y2','y2']
g4=['Y2','y1']
H1=subgroup('H1',[h1,h2,h3,h4],['z1','z2','z3','z4'])
H2=subgroup('H2',[g1,g2,g3,g4],['z1','z2','z3','z4'])
#	F=(F1,F2)
print("flower1")
(flower1,double1,forest1,bfs1)=alg2_pre(H1)
print("flower2")
(flower2,double2,forest2,bfs2)=alg2_pre(H2)
H=(H1,H2)
flower=(flower1,flower2)


def check_gens(H):
    all_clean=0
    print("H gens",H.subgroup_free_gens,"\n\n", H.subgroup_free_gens)
    print("sub gens 1", H.subgp_gens)
    for i in range(len(H.subgroup_free_gens)):
        print("i", i, H.subgp_gens[i], "z", H.basis[i])
        print("free gens",H.subgroup_free_gens[H.basis[i]])
        if  H.subgp_gens[i]!=H.subgroup_free_gens[H.basis[i]]:
            all_clean=1
            print("hoo")
        else:
            print("agast")


    if all_clean==1:
        print("o o")
    
    return(all_clean)    

def label_with_Zs(H,flower): #this should only be done if the number of gens input is the same as the rank of the subgroup

    stall=copy.deepcopy(flower)
    
    for u in stall.vertices:
        u.outedges_write ={}# initialise the output labels of the copy of the folding of H
        u.inedges_write = {}
    
    print("len subgp_gens", len(H.subgp_gens))
    for i in range(len(H.subgp_gens)): # for each of the input generators
        print("i is ", i)
        suffix=H.subgp_gens[i]
        u=stall.root
        while len(suffix)>0 and (suffix[0] in u.outedges.keys() or suffix[0].swapcase() in u.inedges.keys()):
            print("suffix", suffix)
            l=suffix[0]
            if l in u.outedges.keys(): # if the current letter is the label of an outedge u
                for x in u.outedgesList: 
                    if l == x[0]: 
                        if (l,x[1]) in u.outedges_write:
                            L=u.outedges_write[(l,x[1])]
                            L.append(H.basis[i])#set the z label of this outedge to the element of the Z-basis for this genr
                            u.outedges_write[(l,x[1])]=L
                        else:
                            u.outedges_write[(l,x[1])]=[H.basis[i]]
                        #now set the write label of the inedge of the vertex at the other end of this edge
                        if (l,u) in x[1].inedges_write:
                            L=x[1].inedges_write[(l,u)]
                            L.append(H.basis[i])#set the z label of this outedge to the  element of the Z-basis for this genr
                            x[1].inedges_write[(l,u)]=L
                        else:
                            x[1].inedges_write[(l,u)]=[H.basis[i]]  
                           
                        print("read edge ", x, "and set out label to ", H.basis[i])
                        u=x[1] # set u equal to the terminal vertex of the edge read
                        break

            if l.swapcase() in u.inedges.keys():
                for x in u.inedgesList:
                    if l.swapcase() == x[0]: 
                        if (l.swapcase(),x[1]) in u.inedges_write:
                            L=u.inedges_write[(l.swapcase(),x[1])]
                            L.append(H.basis[i].swapcase())#set the z label of this outedge to the inverse of the element of the Z-basis for this genr
                            u.inedges_write[(l.swapcase(),x[1])]=L
                        else:
                            u.inedges_write[(l.swapcase(),x[1])]=[H.basis[i].swapcase()]#set the z label of this inedge to the inverse of the element of the Z-basis for this genr  #the z label of the next edge read
                        #now set the write label of the inedge of the vertex at the other end of this edge
                        if (l.swapcase(),u) in x[1].outedges_write:
                            L=x[1].outedges_write[(l.swapcase(),u)]
                            L.append(H.basis[i].swapcase())#set the z label of this outedge to the element of the Z-basis for this genr
                            x[1].outedges_write[(l.swapcase(),u)]=L
                        else:
                            x[1].outedges_write[(l.swapcase(),u)]=[H.basis[i].swapcase()]
                        print("read edge ", x, "and set out label to ", H.basis[i])
                        u=x[1] # u is the initial vertex of the edge read (in reverse)
                        break

            suffix = suffix[1:]

    return(stall) 
        
ac=check_gens(H1)
print("ac", ac)
stall=label_with_Zs(H1,flower1)
for u in stall.vertices:
            print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write)
            print(u,"inedgeslist", u.inedgesList)
            print(u, "outedgeslist", u.outedgesList,"\n\n")
#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
testfile='adjust_generators/'
#print("name will be", testfile+"Delta")
# Open alg3_test_Delta_in.gv in write mode: this will be the graph above
with open(testfile+"flower1.gv", "w") as f1:
    f1.write("digraph D {\n") #and write to it
with open(testfile+"flower1.gv", "a") as f1: #then open it in append mode
    f1.write(str(flower1)) #and continue to write to it
    f1.write("}")
f1.close()
