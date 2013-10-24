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
                

