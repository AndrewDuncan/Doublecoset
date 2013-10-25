    #################
def rest_of(stall,FZ,verbose,change_tree,want_to_alter):
    for u in stall.vertices:
        if verbose==1:
            print("vertex ", u)
        for e in u.inedgesList:
            if verbose==1:
                print(" in-edge e is ", e)
            if len(u.inedges_write[e])>1:
                if verbose==1:
                    print("write-label written to space as len >1")
                u.inedges_write[e]=""
            elif len(u.inedges_write[e])==1:
                zlab=u.inedges_write[e][0].lower()
                if verbose==1:
                    print("zlab is ", zlab, "u.inedges_write[e]", u.inedges_write[e],"gen_found[zlab] is ",gen_found[zlab])
                if gen_found[zlab]==0: 
                    newlab=u.inedges_write[e][0].lower()
                    if change_tree==1 and want_to_alter=='y':# if the user wants to change the tree then they can choose which edge to leave out
                        print("in-edge into vertex ", u," from vertex ", e[1], " with label ", e[0], " and write-label ", zlab," could be left out of the tree.")
                        print("If it is to be left in the outedge in the opposite direction with the same label will also have to be left in")
                        print("Warning: exactly one (in or out) edge with label z must be left out, for all elements z of Z")
                        leave_out=input("To leave this edge out enter 'y'. Otherwise hit any key: ")
                        if leave_out=='y':
                            u.inedges_write[e]=newlab
                            if verbose==1:
                                print("leave_out is ", leave_out)
                                print("in-edge ", e,"has been given write label", u.inedges_write[e])
                            gen_found[zlab]=1
                        else: 
                            u.inedges_write[e]=""
                            if verbose==1:
                                print("leave_out is not set: ", leave_out)
                            
                    else:
                        u.inedges_write[e]=newlab
                        if verbose==1:
                            print("in-edge ", e,"has been given write label", u.inedges_write[e])
                        gen_found[zlab]=1
                else:
                    u.inedges_write[e]=""
            else:
                error_message="fouled up in build_new_labelling: there's an in edge with no write_label: e is "+str(e)
                sys.exit(error_message)
                
        for e in u.outedgesList:
            if verbose==1:
                print(" out-edge e is ", e)
            if len(u.outedges_write[e])>1:
                u.outedges_write[e]=""
                if verbose==1:
                    print("write-label written to space as len >1")
            elif len(u.outedges_write[e])==1:
                zlab=u.outedges_write[e][0].lower()
                if verbose==1:
                    print("zlab is ", zlab, "u.outedges_write[e]", u.outedges_write[e],"gen_found[zlab] is ",gen_found[zlab])
                if gen_found[zlab]==0: 
                    if change_tree==1 and want_to_alter=='y':# if the user wants to change the tree then they can choose which edge to leave out
                        print("out-edge from vertex ", u," to vertex ", e[1], " with label ", e[0], " and write-label ", zlab," could be left out of the tree.")
                        leave_out=input("To leave this edge out enter 'y'. Otherwise hit any key: ")
                        if leave_out=='y':
                            u.outedges_write[e]=newlab
                            if verbose==1:
                                print("leave_out is ", leave_out)
                                print("out-edge ", e,"has been given write label", u.outedges_write[e])
                            gen_found[zlab]=1
                        else: 
                            u.outedges_write[e]=""
                            if verbose==1:
                                print("leave_out is not set: ", leave_out)
                        ########################################
                    else:
                        u.outedges_write[e]=u.outedges_write[e][0].lower()
                        if verbose==1:
                            print("out-edge ", e,"has been given write label", u.outedges_write[e])
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

################
      
        for e in u.outedgesList:
            if verbose==1:
                print(" out-edge e is ", e)
            if len(u.outedges_write[e])==1:
                zlab=u.outedges_write[e][0].lower()
                if verbose==1:
                    print("in-edge that could be left out found -- ", e)
                    print("zlab is ", zlab, "u.outedges_write[e]", u.outedges_write[e],"gen_found[zlab] is ",gen_found[zlab])
                gen_potential[zlab].append([u,e,1,0])# add this edge to the list of possible egdes; mark out-edges with 0 
                    

#############################

for u in stall.vertices:
        if verbose==1:
            print("vertex ", u)
        for e in u.inedgesList:
            if verbose==1:
                print(" in-edge e is ", e)
            if len(u.inedges_write[e])>1:
                if verbose==1:
                    print("in manual constr of tree: write-label written to space as len >1")
                u.inedges_write[e]=""
            elif len(u.inedges_write[e])==1:
                zlab=u.inedges_write[e][0].lower()
                if verbose==1:
                    print("zlab is ", zlab, "u.inedges_write[e]", u.inedges_write[e],"gen_found[zlab] is ",gen_found[zlab])
                for i in range(len(gen_potential[zlab])):
                    if verbose==1:
                        print("i is ", i, "gen_potential[zlab][i] is", gen_potential[zlab][i])
                    if e==gen_potential[zlab][i][1] and gen_potential[zlab][i][2]==0:
                        newlab=u.inedges_write[e][0].lower()
                        u.inedges_write[e]=newlab
                        if verbose==1:
                            print("in manual constr of tree:in-edge ", e,"has been given write label", u.inedges_write[e])
                        gen_found[zlab]=1
                    else:
                        if verbose==1:
                            print("in manual constr of tree:in-edge ", e,"has been given write blank output label")
                        u.inedges_write[e]=""
            else:
                error_message="fouled up in build_new_labelling_with_user_input: there's an in edge with no write_label: e is "+str(e)
                sys.exit(error_message)
                

####################################
#############################
def amalgamate(w,F1,F2,H1,H2):
    if w==[]:
        print('w is the empty word')
        return([])
    F=(F1,F2)
    #print('F[0] alpha', F[0].alpha)
    #print('F[1] alpha', F[1].alpha)
    error=0
    n=len(w)-1
    if F[0].is_element(w[n])==1:
        f=0
        #print('f is ',f)
    elif F[1].is_element(w[n])==1:
        f=1
        #print('f is ',f)
    else:
        print('Error: ',w[n],'not in free group on', F[0].alpha, 'or', F[1].alpha)
        return
    ff=f
    for s in range(n,-1,-1):
        #print('s is',s,'f is',f)
        if F[f].is_element(w[s])==0:
            print("Error: ",w[s],'is not in F',f)
            error=1
            #print('error becomes 1')
            break
        f=1-f
    if error==1:
        return
    H=(H1,H2)
    f=ff
    for s in range(n,-1,-1):
        #put w[s] in terms of H[1-f] here
        #print('Start of loop. w is', w)    
        #print('s is',s)
        #print('w[s] is',w[s])
        #print("H[f] is ", H[f].name)
        t=hf_test(w[s],H[f])
        if t[0]==1: #if w[s] is in H[f]
            if len(w)>1:# if w has already been reduced to a single syllable there is no need to do anything more
                w[s]=phi(H[1-f],t[1])[0] #swap w[s] from H[f] to H[1-f]
                if s==0:#  if the first syllable is in H[f]
                    w[s]=w[s]+w[s+1]
                    w[s]=element(w[s]).word
                    for i in range(s+2,len(w)):
                        w[i-1]=w[i]
                    #print("a,len(w)", len(w))
                    w.pop(len(w)-1)
                    #print("b, len(w)", len(w))
                elif s==len(w)-1:# when the amalgamated syllable is the last one
                    w[s-1]=w[s-1]+w[s]
                    w[s-1]=element(w[s-1]).word
                    #print("c, len(w)",len(w))
                    w.pop(s)
                    #print("d,len(w)", len(w))
                else: # the general case
                    w[s-1]=w[s-1]+w[s]+w[s+1]
                    w[s-1]=element(w[s-1]).word
                    for i in range(s+2,len(w)):
                        w[i-2]=w[i]
                        #print("len(w)", len(w)," and i,w[i-2], w[i]", i,w[i-2],w[i])
                    #print("e,len(w)", len(w))
                    w.pop(len(w)-1)
                    #print("f,len(w)", len(w))
                    w.pop(len(w)-1)
                    #print("g,len(w)", len(w))

        f=1-f

    return(w)
