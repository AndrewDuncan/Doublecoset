        
    delta_n=delta_5# delta_5 is a list of 2 graphs: delta_5[0] and delta_5[1], the X1 and X2 components of delta
    delta_n.append(delta_z)# extend the list of graphs to include the Z component delta_z
    #test only...
    for k in (0,1):
        for v in delta_n[k].vertices:
            a=1
            #print("testing: k is ", k," v is ", v," and v.nu_im is ", v.nu_im," and original is ", v.original)
    again=True
    vertex_delete_list=[]# a list of vertices that have become redundant and will be deleted at the end of reassembly
    while again:
        again=False
        for k in (0,1,2):
            for v in delta_n[k].vertices:
                ind=delta_n[k].vertices.index(v)#extract the index of v
                for j in (0,1,2):
                    for u in delta_n[j].vertices:
                        if ((j==k and delta_n[j].vertices.index(u)>ind) or j>k) and not (j,u) in vertex_delete_list:
                            #print("passed test  and k,j,v,u ", k, " ", j," ",v," ", u)
                            if k<=1 and j<=1:#this part applies if both v and u belong to the X1 or X2 components
                                if len(v.nu_im.intersection(u.nu_im))>0:#u should be replaced with v, and u deleted, in this case
                                    again=True#something has been done, so the main loop should be repeated
                                    vertex_delete_list.append((j,u))# need to record j as well as u, so the vertex u can be easily found
                                    #print("something to do: k is ", k, " v is ", v, " j is ", j, " u is ", u, "nu-im int is ", v.nu_im.intersection(u.nu_im))
                                    v.nu_im=v.nu_im.union(u.nu_im)
                                    #print("union ",  v.nu_im)
                                    u.nu_im=set()#make this empty so that u will not be considered again (is this necessary with u on vertex_delete_list?)
                                    for e in u.outedgesList:#replace all outedges u -> x with v -> x
                                        #here should also find the corresponding inedge u -> x of x, and replace it with v -> x
                                        target_list=e[1].label.split("-",1)
                                        target=target_list[0]
                                        if target in v.nu_im:
                                            #print("u is ", u, " outedge is ", e, " and both ends replaced by ", v)
                                            delta_n[k].addEdge(v,v,e[0])
                                        else:
                                            delta_n[k].addEdge(v,e[1],e[0])
                                            #print("u is ", u," outedge is ", e, " and origin  replaced by ", v)

                                    for e in u.inedgesList:#replace all inedges x -> u with x -> v
                                        #here should also find the corresponding outedge x -> u of x, and replace it with x -> v
                                        origin_list=e[1].label.split("-",1)
                                        origin=origin_list[0]
                                        if origin in v.nu_im:
                                            #print("u  is ",u," inedge is ", e, " and both ends replaced by ", v)
                                            delta_n[k].addEdge(v,v,e[0])
                                        else:
                                            delta_n[k].addEdge(e[1],v,e[0])
                                            #print("u is ",u,"inedge is ", e, " and target replaced by ", v)    
                                     
                                    #if u occurs in an edge replace it with v ... if the above have been done should only need to do this for delta_z
                                    for i in (0,1,2):
                                        for w in delta_n[i].vertices:
                                            if not (i,w) in vertex_delete_list:
                                                for e in w.outedgesList:#if there is an edge w -> u
                                                    if e[1]==u:
                                                        w.removeOutEdge(e[0],e[1])#remove it and 
                                                        delta_n[i].addEdge(w,v,e[0])#replace it with w -> v
                                                         
                                                for e in w.inedgesList:#if there is an edge v -> w
                                                    if e[1]==v:
                                                        delta_n[i].addEdge(u,w,e[0])
                                                        w.removeInEdge(e[0],e[1])#replace it with u -> w
                            #else:
                                #print("k,j,v,u ", k, " ", j," ",v," ", u)
                            #now need to cover the case where k or j>1
    print("dels ", vertex_delete_list)
