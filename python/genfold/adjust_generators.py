from alg3 import *
import sys
import copy

def construct_required_folding(Hname,Hgens,testfile,F,Hrank,verbose,FZ):
     
    if verbose==1:
        print("into construct_required_folding")

    #set flags for testing subgroup generators
    num_H_gens=1 # set to 0 if Hrank = number of Hgens
    H_gens_in_F=1 # set to 0 if Hgens belong to F
    H_rank=1 # set to 0 if the computed rank of H is equal to Hrank
    H_gens_basis=1 #set to 0 if Hgens coincide with the computed basis for H
    edges_rept=1 #set to 0 if new Hgens are input and do not cause loops in Stallings folding of H
    edges_miss=1 #set to 0 if new Hgens are input and do (possibly) genr H
    nielsen_red=1#set to 0 if Hgens are Nielsen reduced
    

    while num_H_gens==1:
        while True: # a loop that runs till it's broken out of (i.e. until len(Hgens)=Hrank)
            for w in Hgens: #remove trivial elements from Hgens before testing the number of generators
                if w==['']:
                    Hgens.remove(w)
            if len(Hgens)==Hrank: #check if the number of generators equals the required rank of the subgroup
                num_H_gens=0
                break
            else:
                print('Please enter a Nielsen reduced free generating set of size %s ' % (Hrank,),'as a comma separated list, e.g. x1,x2,X1')
                
                if verbose==1:
                    print("calling genr_input")
                Hgens=genr_input(Hrank)

            
        if verbose==1:
            print("after 1st test Hgens is ", Hgens)
            print("Hrank is ", Hrank, "len(Hgens) is ",len(Hgens))

        #if we reach here, then num_H_gens=0
        
        #check that the elements of Hgens are in the free group F
        if verbose==1:
            print("calling generators_in_free_group")
        H_gens_in_F=generators_in_free_group(F,Hgens)# this will be 0 if all elements of Hgens are in F, and 1 otherwise
        if H_gens_in_F!=0: #if some Hgens are not in F, input new Hgens and reset num_H_gens, so no further tests are applied and the loop repeats from the start
            H_gens_in_F=1 #just to make sure
            num_H_gens=1
            print('Please enter a Nielsen reduced free generating set of size %s ' % (Hrank,),'as a comma separated list, e.g. x1,x2,X1, of elements of the free group on generators ', F.gens)
            
            if verbose==1:
                print("calling genr_input")
            Hgens=genr_input(Hrank)

        if verbose==1:
            print("after 2nd test Hgens is ", Hgens)
            print("Hrank is ", Hrank, "len(Hgens) is ",len(Hgens))

        
        if (H_gens_in_F,num_H_gens)==(0,0):#if the tests above were passed ...

            #construct the Stallings folding of H
            if verbose==1:
                print("calling subgroup_compute")
            H=subgroup_compute(Hname,Hgens,FZ)
            
            if len(H.subgroup_free_gens)!=Hrank: #if the rank of the subgroup generated by Hgens is less than the length of Hgens ...
                H_gens_in_F=1 #reset all flags to skip all further tests and return to start of loop
                num_H_gens=1
                #and enter new generators
                print('The basis computed has ', len(H.subgroup_free_gens),' elements, but the required subgroup rank is ',Hrank)
                print('Please enter a Nielsen reduced free generating set of size %s ' % (Hrank,),'as a comma separated list, e.g. x1,x2,X1, of elements of the free group on generators ', F.gens)
                if verbose==1:
                    print("calling genr_input")
                Hgens=genr_input(Hrank)
            else:
                H_rank=0

        if verbose==1:
            print("after 3rd test Hgens is ", Hgens)
            print("H.subgroup_free_gens is ", H.subgroup_free_gens)

        
        output_graph_file(H.flower,testfile+"firstfolding.gv","fold",verbose)#for testing only, remove later

            
        if (H_gens_in_F,num_H_gens,H_rank)==(0,0,0):#if the tests above were passed ...
            
            #check to see if the generators input are the same as the generators found by Stallings folding
            if verbose==1:
                print("calling check_gens")
            H_gens_basis=check_gens(H,Hgens)
            if H_gens_basis==0: #if H_gens_basis=0 the basis computed is equal to the input generators and the main loop is broken out of
                break

            if verbose==1:
                print("H free gens",H.subgroup_free_gens)
                print("subgroup genrs input", Hgens)

        #this point is reached only if all tests above are passed except the last - in which case it is necessary to find a different spanning tree for the stallings folding of H

       
        stall=label_with_Zs(H,Hgens,verbose) #relabel Stallings folding with given gens/ Z labels - to set up search for required gens
                    
        output_graph_file(stall,testfile+"stall_labl.gv","stall",verbose)#for testing only, remove later
                
        #check to see that all edges have been used in reading gens and that no (directed) output labels have been assigned twice to the same edge
        edges_rept=check_nielsen_reduced(stall,verbose)
        if edges_rept==1: 
            H_gens_in_F=1 #reset all flags to skip all further tests and return to start of loop
            num_H_gens=1
            H_rank=1
            #and enter new generators
            print("The generators entered ", Hgens, " are not Nielsen reduced")
            print('Please enter a Nielsen reduced free generating set of size %s ' % (Hrank,),'as a comma separated list, e.g. x1,x2,X1, of elements of the free group on generators ', F.gens)
            if verbose==1:
                    print("calling genr_input")
            Hgens=genr_input(Hrank)

        if (H_gens_in_F,num_H_gens,H_rank,edges_rept)==(0,0,0,0):#if the tests above were passed (but the basis calculated needs adjusting) ...
            nielsen_red=build_new_labelling(stall,FZ,verbose)
            if nielsen_red!=0:
                H_gens_in_F=1 #reset all flags to skip all further tests and return to start of loop
                num_H_gens=1
                H_rank=1
                edges_rept=1
                #and enter new generators
                print("No rept edges found BUT the generators entered ", Hgens, " are not Nielsen reduced")
                print('Please enter a Nielsen reduced free generating set of size %s ' % (Hrank,),'as a comma separated list, e.g. x1,x2,X1, of elements of the free group on generators ', F.gens)
                if verbose==1:
                    print("calling genr_input")
                Hgens=genr_input(Hrank)

        if (H_gens_in_F,num_H_gens,H_rank,edges_rept,nielsen_red)==(0,0,0,0,0):#if the tests above were passed (but the basis calculated needs adjusting) ...

            #using the new labellings construct a spanning tree for the stallings folding
            forced_bfs(stall,verbose)# use the new labels to make a new tree

            if len(stall.components)>1: #this would be catastrophic and mean something is wrong with the algorithm (or its implementation)
                error_message="Exiting. Something's wrong. The candidate tree for the Stallings folding did not span: the bfs_forced function ended up with "+len(stall.components)+" components"
                sys.exit(error_message)
            
            # reassign subgroup_free_gens, using the new spanning tree for the stallings folding
            H.subgroup_free_gens=subgroup_basis(stall)[1]
            
            #set H.flower equal to stall
            H.flower=stall

    return(H)

#################################end of construct_required_folding
#################################

def genr_input(n):

    nn=int(n)
    Hgens=[]
    for i in range(1,nn+1):
        w=input('Enter generator number %s: ' % (i,))
        w=w.replace(' ','')
        w=w.split(",")
        Hgens.append(w)
    return(Hgens)

def generators_in_free_group(F,Hgens):
    
    test=0
    for w in Hgens:
        if not F.is_element(w):
            test=1
            break

    return(test)

def subgroup_compute(Hname,Hgens,FZ):

    H=subgroup(Hname,Hgens,FZ.gens)
    alg2_pre(H)
    return(H)

def check_gens(H,Hgens):  #check to see if the generators Hgens are the ones found by the Stallings folding

    all_clean=0

    for i in range(len(H.subgroup_free_gens)):
        #print("i", i, Hgens[i], "z", H.basis[i])
        #print("free gens",H.subgroup_free_gens[H.basis[i]])
        if  Hgens[i]!=H.subgroup_free_gens[H.basis[i]]:
            all_clean=1
            break
        
    return(all_clean)   

def label_with_Zs(H,Hgens,verbose): 
    if verbose==1:
        print("calling label_with_Zs")
        
    stall=copy.deepcopy(H.flower)#not sure if needed
    
    for u in stall.vertices:
        u.outedges_write ={}# initialise the output labels of the copy of the folding of H
        u.inedges_write = {}
    
    if verbose==1:
        print("len subgp_gens", len(Hgens))
    for i in range(len(Hgens)): # for each of the input generators
        if verbose==1:
            print("i is ", i)
        suffix=Hgens[i]
        u=stall.root
        while len(suffix)>0 and (suffix[0] in u.outedges.keys() or suffix[0].swapcase() in u.inedges.keys()):
            if verbose==1:
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
                           
                        if verbose==1:
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
                        if verbose==1:
                            print("read edge ", x, "and set out label to ", H.basis[i])
                        u=x[1] # u is the initial vertex of the edge read (in reverse)
                        break

            suffix = suffix[1:]

    return(stall) 

#check that when the (original or current) input generators are read in the stallings folding (labelled with Zs) there are no repeated edges or missed edges (if there are missed edges something has gone badly wrong).
def check_nielsen_reduced(stall,verbose):
    if verbose==1:
        print("into check_nielsen_reduced")
    edgerep=0
    for u in stall.vertices:
        for e in u.inedgesList:
            if e not in u.inedges_write:
                if verbose==1:
                    print("at vertex ", u, "inedge", e,"is not read: there is nothing in u.inedges_write:", u.inedges_write)
                error_message="Exiting: the subgroup of the stallings folding is not generated by "+list(Hgens)
                sys.exit(error_message)

            if anydup(u.inedges_write[e]):
                if verbose==1:
                    print("at vertex ", u, "inedge", e,"is read twice: there is repetition in u.inedges_write:", u.inedges_write)
                edgerep=1
                break
        
        for e in u.outedgesList:
            if anydup(u.outedges_write[e]):
                if verbose==1:
                    print("at vertex ", u, "outedge",e, "is read twice: there is repetition in u.outedges_write:", u.outedges_write)
                edgerep=1
                break
            
   
    return(edgerep)


#once generators have been read and all edges labelled with Zs, find, for each letter z in Z an edge which is labelled only with  z, and put this edge outside the (potential) tree. Assumes check_nielsen_reduced has run with output 0,0.
def build_new_labelling(stall,FZ,verbose):
    if verbose==1:
        print("into build_new_labelling")
    gen_found={} #dictionary with entries (z:i) where z is in Z and i is 0 to start with and becomes 1 once an edge labelled only with z has been found and put outside the candidate tree
    for z in FZ.gens:
        if verbose==1:
            print("z is",z)
        gen_found[z]=0
    
    for u in stall.vertices:
        for e in u.inedgesList:
            if verbose==1:
                print(" in edge e is ", e)
            if len(u.inedges_write[e])>1:
                if verbose==1:
                    print("write-label written to space as len >1")
                u.inedges_write[e]=""
            elif len(u.inedges_write[e])==1:
                zlab=u.inedges_write[e][0].lower()
                if verbose==1:
                    print("zlab is ", zlab, "u.inedges_write[e][0]", u.inedges_write[e][0],"gen_found[zlab] is ",gen_found[zlab])
                if gen_found[zlab]==0: 
                    newlab=u.inedges_write[e][0].lower()
                    u.inedges_write[e]=newlab
                    if verbose==1:
                        print("in edge ", e,"has been given write label", u.inedges_write[e])
                    gen_found[zlab]=1
                else:
                    u.inedges_write[e]=""
            else:
                error_message="fouled up in build_new_labelling: there's an in edge with no write_label: e is "+str(e)
                sys.exit(error_message)
                
        for e in u.outedgesList:
            if verbose==1:
                print(" in edge e is ", e)
            if len(u.outedges_write[e])>1:
                u.outedges_write[e]=""
                if verbose==1:
                    print("write-label written to space as len >1")
            elif len(u.outedges_write[e])==1:
                zlab=u.outedges_write[e][0].lower()
                if verbose==1:
                    print("zlab is ", zlab, "u.outedges_write[e][0]", u.outedges_write[e][0],"gen_found[zlab] is ",gen_found[zlab])
                if gen_found[zlab]==0: 
                    u.outedges_write[e]=u.outedges_write[e][0].lower()
                    if verbose==1:
                        print("out edge ", e,"has been given write label", u.outedges_write[e])
                    gen_found[zlab]=1
                else:
                    u.outedges_write[e]=""
            else:
                error_message="fouled up in build_new_labelling: there's an out edge with no write_label: e is "+str(e)
                sys.exit(error_message)

    #now match up in and out edges --- above only one of the pair was given the correct z label. 
    for z in FZ.gens:
        #print("z is",z)
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

    #now check we have a tree (assuming the graph is connected)
    number_of_edges_of_tree=0
    nr=0
    for u in stall.vertices:
        for e in u.outedgesList:
            if u.outedges_write[e]=="":
                number_of_edges_of_tree += 1
    
    if len(stall.vertices)-number_of_edges_of_tree!=1:
        nr=1
    
    return(nr)

def forced_bfs(stall,verbose):
    if verbose==1:
        print("into forced_bfs")
    #must be a rooted graph, with output labels corresponding to edges outside a spanning forest

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


def output_graph_file(graph,filename,graphname,verbose):  

    if verbose==1:
        print("into output_graph_file")
        print("opening file ",filename)
    with open(filename, "w") as go:
        go.write("digraph graphname {\n") #and write to it
    with open(filename, "a") as go: #then open it in append mode
        go.write(str(graph)) #and continue to write to it
        go.write("}")
    go.close()   

#function to check for duplicates in a list
def anydup(thelist):
    seen = set()
    for x in thelist:
        if x in seen: 
            return True
        seen.add(x)
    return False
