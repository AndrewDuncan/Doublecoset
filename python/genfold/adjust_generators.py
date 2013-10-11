from alg3 import *
#from alg2 import *
#from input import * #temporary, will eventually be included in the above import
#import copy
F1=free_group(2,"x")
F2=free_group(2,"y")
Z=free_group(4,"z")
F=(F1,F2)
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
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


def check_gens(H,Hgens):  #check to see if the generators Hgens are the ones found by the Stallings folding
    all_clean=0
    print("H gens",H.subgroup_free_gens)
    print("sub gens 1", Hgens)
    print("input gens",Hgens)
    for i in range(len(H.subgroup_free_gens)):
        print("i", i, Hgens[i], "z", H.basis[i])
        print("free gens",H.subgroup_free_gens[H.basis[i]])
        if  Hgens[i]!=H.subgroup_free_gens[H.basis[i]]:
            all_clean=1
            print("hoo")
        else:
            print("agast")


    if all_clean==1:
        print("o o")
    
    return(all_clean)    

def label_with_Zs(H,flower,Hgens): 
#this should only be done if the number of gens input is the same as the rank of the subgroup
    if len(Hgens)!=len(H.subgroup_free_gens):
        print("The generators are: ",Hgens," and the basis is:",H.subgroup_free_gens)
        print("There are different numbers of  elements in the generators than the rank computed.")
        print("Please enter a free generating set of the correct size")
        return

    stall=copy.deepcopy(flower)
    
    for u in stall.vertices:
        u.outedges_write ={}# initialise the output labels of the copy of the folding of H
        u.inedges_write = {}
    
    print("len subgp_gens", len(Hgens))
    for i in range(len(Hgens)): # for each of the input generators
        print("i is ", i)
        suffix=Hgens[i]
        u=stall.root
        while len(suffix)>0 and (suffix[0] in u.outedges.keys() or suffix[0].swapcase() in u.inedges.keys()):
            print("suffix", suffix)
            l=suffix[0]
            if l in u.outedges.keys(): # if the next letter is the label of an outedge u
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
                            L.append(H.basis[i])#set the z label of this outedge to the element of the Z-basis for this genr
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
                            L.append(H.basis[i])#set the z label of this outedge to the element of the Z-basis for this genr
                            u.inedges_write[(l.swapcase(),x[1])]=L
                        else:
                            u.inedges_write[(l.swapcase(),x[1])]=[H.basis[i]]#set the z label of this inedge to the element of the Z-basis for this genr  #the z label of the next edge read
                        #now set the write label of the inedge of the vertex at the other end of this edge
                        if (l.swapcase(),u) in x[1].outedges_write:
                            L=x[1].outedges_write[(l.swapcase(),u)]
                            L.append(H.basis[i])#set the z label of this outedge to the element of the Z-basis for this genr
                            x[1].outedges_write[(l.swapcase(),u)]=L
                        else:
                            x[1].outedges_write[(l.swapcase(),u)]=[H.basis[i]]
                        print("read edge ", x, "and set out label to ", H.basis[i])
                        u=x[1] # u is the initial vertex of the edge read (in reverse)
                        break

            suffix = suffix[1:]

    return(stall) 

#function to check for duplicates in a list
def anydup(thelist):
    seen = set()
    for x in thelist:
        if x in seen: 
            return True
        seen.add(x)
    return False

#check that when the (original or current) input generators are read in the stallings folding (labelled with Zs) there are no repeated edges
def check_neilsen_reduced(stall): 
    edgerep=0
    edgecover=0
    for u in stall.vertices:
        for e in u.inedgesList:
            if e not in u.inedges_write:
                print("at vertex ", u, "inedge", e,"is not read: there is nothing in u.inedges_write:", u.inedges_write)
                edgecover=1
                return(edgecover,edgerep)

            if anydup(u.inedges_write[e]):
                print("at vertex ", u, "inedge", e,"is read twice: there is repetition in u.inedges_write:", u.inedges_write)
                edgerep=1
                break
        
        for e in u.outedgesList:
            if anydup(u.outedges_write[e]):
                print("at vertex ", u, "outedge",e, "is read twice: there is repetition in u.outedges_write:", u.outedges_write)
                edgerep=1
                break
            
    return(edgecover,edgerep)

def check_edges_covered(stall):
    edgecover=0
    for u in stall.vertices:
        for e in u.inedgesList:
            if len(u.inedges_write[e])==0:
                print("at vertex ", u, "inedge", e,"is not read: there is nothing in u.inedges_write:", u.inedges_write)
                edgecover=1
                break

    return(edgecover,edgerep)

#once generators have been read and all edges labelled with Zs, find, for each letter z in Z an edge which is labelled only with  z, and put this edge outside the (potential) tree. Assumes check_neilsen_reduced has run with output 0,0.
def build_new_labelling(stall):
    gen_found={} #dictionary with entries (z:i) where z is in Z and i is 0 to start with and becomes 1 once an edge labelled only with z has been found and put outside the candidate tree
    for z in Z:
        gen_found[z]=0

    for u in stall.vertices:
        for e in u.inedgesList:
            a=b


############################
#Hgens=H1.subgp_gens  
Hgens=[h1,h2,h3,h4]
ac=check_gens(H1,Hgens)
print("if the input generators equal the basis found by folding the next digit will be 0", ac)
stall=label_with_Zs(H1,flower1,Hgens)
for u in stall.vertices:
            print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write)
            print(u,"inedgeslist", u.inedgesList)
            print(u, "outedgeslist", u.outedgesList,"\n\n")
ec,cn=check_neilsen_reduced(stall)
print( "edges covered", ec,"neilsen reduced =", cn)

#ec=check_edges_covered(stall)
#print("edges_covered =", ec)
