from alg3 import *

# Open testfile/flower[k].gv in write mode: this will be the graph above
#with open(testfile+"flower1.gv", "w") as f1:
#    f1.write("digraph D {\n") #and write to it
#with open(testfile+"flower1.gv", "a") as f1: #then open it in append mode
#    f1.write(str(flower1)) #and continue to write to it
#    f1.write("}")
#f1.close()

 
def output_graph_file(graph,filename,graphname):  
    # Open testfile/graph.gv in write mode
    with open(filename, "w") as go:
        go.write("digraph graphname {\n") #and write to it
    with open(filename, "a") as go: #then open it in append mode
        go.write(str(graph)) #and continue to write to it
        go.write("}")
    go.close()   

def output_graph_pair(graphpair,basename,testfile):
    for k in (0,1):
        n=str(k+1)
        filename=testfile+basename+n+".gv"
        graphname=basename+n
        output_graph_file(graphpair[k],filename,graphname)
 


def check_gens(H,Hgens):  #check to see if the generators Hgens are the ones found by the Stallings folding
    all_clean=0
    print("H free gens",H.subgroup_free_gens)
    print("sub gens 1", Hgens)
    print("input gens",Hgens)
    for i in range(len(H.subgroup_free_gens)):
        print("i", i, Hgens[i], "z", H.basis[i])
        print("free gens",H.subgroup_free_gens[H.basis[i]])
        if  Hgens[i]!=H.subgroup_free_gens[H.basis[i]]:
            all_clean=1
            print("hoo unequal at", i," Hgens[i] =", Hgens[i],"H.basis[i]=", H.basis[i],"H.subgroup_free_gens[H.basis[i]]=", H.subgroup_free_gens[H.basis[i]])
        else:
            print("Hgens equal to free gens at ",i)


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


#once generators have been read and all edges labelled with Zs, find, for each letter z in Z an edge which is labelled only with  z, and put this edge outside the (potential) tree. Assumes check_neilsen_reduced has run with output 0,0.
def build_new_labelling(stall,FZ):
    gen_found={} #dictionary with entries (z:i) where z is in Z and i is 0 to start with and becomes 1 once an edge labelled only with z has been found and put outside the candidate tree
    for z in FZ.gens:
        print("z is",z)
        gen_found[z]=0

    for u in stall.vertices:
        for e in u.inedgesList:
            print(" in edge e is ", e)
            if len(u.inedges_write[e])>1:
                print("write written to space as len >1")
                u.inedges_write[e]=""
            elif len(u.inedges_write[e])==1:
                #if u.inedges_write[e][0]==u.inedges_write[e][0].lower():
                zlab=u.inedges_write[e][0].lower()
                print("zlab is ", zlab, "u.inedges_write[e][0]", u.inedges_write[e][0],"gen_found[zlab] is ",gen_found[zlab])
                if gen_found[zlab]==0: 
                    newlab=u.inedges_write[e][0].lower()
                    u.inedges_write[e]=newlab
                    print("in edge ", e,"given write label", u.inedges_write[e])
                    gen_found[zlab]=1
                else:
                    u.inedges_write[e]=""
            else:
                print("fouled up in build_new_labelling: there's an in edge with no write_label: e is ", e)
                return
        for e in u.outedgesList:
            print(" in edge e is ", e)
            if len(u.outedges_write[e])>1:
                u.outedges_write[e]=""
                print("write written to space as len >1")
            elif len(u.outedges_write[e])==1:
                zlab=u.outedges_write[e][0].lower()
                print("zlab is ", zlab, "u.outedges_write[e][0]", u.outedges_write[e][0],"gen_found[zlab] is ",gen_found[zlab])
                if gen_found[zlab]==0: 
                    u.outedges_write[e]=u.outedges_write[e][0].lower()
                    print("out edge ", e,"given write label", u.outedges_write[e])
                    gen_found[zlab]=1
                else:
                    u.outedges_write[e]=""
            else:
                print("fouled up in build_new_labelling: there's an out edge with no write_label: e is ", e)
                return

    #now match up in and out edges --- above only one of the pair was given the correct z label. 
    for z in FZ.gens:
        print("z is",z)
        gen_found[z]=0

    for u in stall.vertices:
        for e in u.inedgesList:
            if u.inedges_write[e]!="":
                (l,v)=e
                v.outedges_write[(l,u)]=u.inedges_write[e]
                gen_found[u.inedges_write[e]]=1


        for e in u.outedgesList:
            if u.outedges_write[e]!="" and gen_found[u.outedges_write[e]]==0:
                (l,v)=e
                v.inedges_write[(l,u)]=u.outedges_write[e]
                gen_found[u.outedges_write[e]]=1

 #   return(stall)

def reverse_a_z(stall,z):
    for u in stall.vertices:
        for e in u.inedgesList:
            if u.inedges_write[e].lower()==z.lower():
                u.inedges_write[e]=u.inedges_write[e].swapcase()
                break

        for e in u.outedgesList:
            if u.outedges_write[e].lower()==z.lower():
                u.outedges_write[e]=u.outedges_write[e].swapcase()
                break

def forced_bfs(stall): #must be a rooted graph, with output labels corresponding to edges outside a spanning forest

    #initialise attributes used to define spanning tree
    stall.components={}
    i = 0 #time a vertex is added
    q = [] #queue of vertices to be processed within a connected component
    N = {} #dictionary of adjacent edges to a vertex
    for v in stall.vertices:
        v.colour = 0 #colour is synonomous with connected component. Here is is initialised
        v.length = 0#distance from root
        v.time = 0 #time added
        v.parent=None
        v.path=[]
        N[v]=[] #will be a list of all edges incident to v, except those which have Z labels (so are designated outside the tree)
        for (a,b) in v.outedgesList: 
            if v.outedges_write[(a,b)]=="":
                N[v].append((a,b,"+")) #record + for outedges
            
        for (a,b) in v.inedgesList:
            if v.inedges_write[(a,b)]=="":
                N[v].append((a.swapcase(),b,"-"))#record - for inedges
                
    Nout = list(stall.vertices) #list of all vertices. When a vertex is added to a tree it is removed from this list
    c = 0
    while Nout:
        c += 1
        i += 1
        v =Nout[0]
        Nout.remove(v)
        v.colour = c
        v.length = 0
        v.time = i
        v.parent = v
        v.path =[]
        stall.components[c]=v #print("components are now", stall.components)
        q.append(v)# add v to the end of the queue
        while q:
            u=q[0] # for the first element u of the queue
            for (a,b,d) in N[u]: #and all edges incident to u, with label a to vertex b (and in/out indicator d) 
                if b.colour == 0: # if b is not already in a component 
                    i += 1         #increase time by 1 
                    b.colour = c   #put b in the current component
                    b.parent = u   #make u the parent of b
                    b.length = u.length + 1 #make the distance of b from the root one more than the distance of u
                    b.time = i     # time b was added
                    b.path =u.path + [a] # path from the root to b
                    q.append(b)    # add b to the end of the queue 
                    Nout.remove(b) # remove b from the list of all vertices
                
            q.pop(0) # remove the first element of the queue
