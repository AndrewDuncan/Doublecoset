from alg2 import *
from input import * #temporary, will eventually be included in the above import
import copy

def alg3_pre():
    print('For the first free group:')
    F1=enter_free_group()
    print('For the second free group:')
    F2=enter_free_group()
    F=(F1,F2)
    print('For the first subgroup:')
    H1=enter_subgroup()
    print('For the second subgroup:')
    H2=enter_subgroup()
    #(flower1,double1,forest1,bfs1)=
    alg2_pre(H1)
    #(flower1,double1)=(H1.flower,H1.double)#this line probably not needed
    alg2_pre(H2)
    #(flower2,double2)=(H2.flower,H2.double)#this line probably not needed
    H=(H1,H2)
    if F1.rank>F2.rank:
        Z=free_group(F1.rank,'z')
    else:
        Z=free_group(F2.rank,'z')
    return F,Z,H1,H2#,flower1,double1# this should return in a more systematic fashion


def MakeComps(delta,F,Z,verbose,logfile): #input Delta, free groups F=(F1,F2) and Z generators
    delta_k0=[] # to become a pair of graphs, one for each X_i
    delta_z=Graph(False,'Delta Z') # the Z component, composed of edges labelled with letters of Z, removed in the process of pruning shoots
    for k in (1,2): # do the following for X_1 and X_2 components
        delta_k0k=copy.deepcopy(delta) #take a new copy of delta, call it k0k
        for v in delta_k0k.vertices[::-1]: #part a,remove edges of k0k which are in X_[2-k] to make component
            for label,w in v.outedgesList[::-1]:
                if label in F[2-k].mongens: # 
                    v.removeOutEdge(label,w)
                    w.removeInEdge(label,v)
            for label,w in v.inedgesList[::-1]:
                if label in F[2-k].mongens:
                    v.removeInEdge(label,w)
                    w.removeOutEdge(label,v)
        shoots=1  #part b, remove Z shoots
        while shoots!=0:
            ind=0
            for v in delta_k0k.vertices[::-1]: #for each vertex of k0k
                if verbose[3]>1:
                    output_log_file(logfile,"k is "+ str(k)+" v name, v label "+str(v.name)+str(v.label))
                edgesList=v.inedgesList+v.outedgesList # make a list of all edges incident to v
                v_in_delta_z=0
                for u in delta_z.vertices: #now test to see if this vertex v is in the Z component, delta_z
                            if v.label==u.label:
                                v_in_delta_z=1# set this flag to 1 if v is already in delta_z
                                vcopy=u # keep track of which vertex of delta_z is equal to v
                if len(edgesList)==1: # if we have a shoot with leaf v
                     if edgesList[0][0] in Z.mongens: # and the shoot has a label in Z
                        ind+=1
                        if verbose[3]>1:
                            output_log_file(logfile,"ind is "+ str(ind))
                            output_log_file(logfile,"we found an edge to remove:"+ str(edgesList[0]))
                        vv_in_delta_z=0
                        for u in delta_z.vertices:
                            if verbose[3]>1:
                                output_log_file(logfile,"u is"+ str(u)+ " and edgesList[0] is "+ str(edgesList[0]))
                            if edgesList[0][1].label==u.label: 
                                vv_in_delta_z=1# set this flag to 1 if the other end of this edge is already in delta_z
                                vvcopy=u # and in this case keep track of the vertex of delta_z at the other end of the shoot with leaf v
                                if verbose[3]>1:
                                    output_log_file(logfile,"found that vertex "+ str(edgesList[0][0])+ "is already in delta_z")
                                break
                        if v_in_delta_z==0: # v is not already in delta_z
                            vcopy=delta_z.addVertex(v.name) # add a new vertex to delta_z with same descr as v
                            vcopy.label=v.label
                            v_in_delta_z=1 # record that v is now in delta_z
                            if verbose[3]>=1:
                                output_log_file(logfile,"D0 (MakeComps): k is "+ str(k)+ ", added vertex v  to delta_z with label: "+ str(vcopy.label))
                        if vv_in_delta_z==0: #if the other end of the shoot is not in delta_z
                            vv=edgesList[0][1]
                            vvcopy=delta_z.addVertex(vv.name)# add it to delta_z
                            vvcopy.label=vv.label
                            if verbose[3]>=1:
                                output_log_file(logfile,"D0 (MakeComps): k is "+ str(k)+ ", added vertex vv to  delta_z with label "+ str(vvcopy.label))
                            vv_in_delta_z=1 #record that this vertex is now in delta_z
                    
                        if len(v.inedgesList)==1: #if the shoot is an inedge at v
                            if verbose[3]>1:
                                output_log_file(logfile,"k is "+str(k)+"v is "+ str(v)+" inedges are"+ str(v.inedgesList)+ "outedges are "+ str(v.outedgesList))
                            #if the edge is already incident to vcopy in delta_z, do nothing
                            if (edgesList[0][0],edgesList[0][1]) not in vcopy.inedgesList:  
                                delta_z.addEdge(vvcopy,vcopy,edgesList[0][0])
                                if verbose[3]>=1:
                                    output_log_file(logfile,"D0 (MakeComps): adding edge, edgesList[0] is "+ str(edgesList[0]))
                                    output_log_file(logfile,"k is "+ str(k)+ ", v, vv = "+ str(vcopy)+", "+ str(vvcopy)+ "; added edge from vv to v with label "+ str(edgesList[0][0]))

                        elif len(v.outedgesList)==1:#if the shoot is an outedge at v
                            #if the edge is already incident to vcopy in delta_z, do nothing
                            if (edgesList[0][0],edgesList[0],[1]) not in vcopy.outedgesList:
                                delta_z.addEdge(vvcopy,vcopy,edgesList[0][0]) 
                                if verbose[3]>=1:
                                    output_log_file(logfile,"D0 (MakeComps):adding edge , edgesList[0] is "+ str(edgesList[0]))
                                    output_log_file(logfile,"k is "+ str(k)+ " v, vv = "+ str(vcopy)+ ", "+str(vvcopy)+ "; added edge from vv to v with label "+ str(edgesList[0][0]))
                        else:
                            error_message="Exiting from Makecomps: something is wrong at vertex v "+str(v)
                            sys.exit(error_message)
 
                        label=edgesList[0][0]
                        w=edgesList[0][1]
                        if (label,w) in v.inedgesList: #now remove the shoot from the in or out edges of the non-leaf end
                            v.removeInEdge(label,w)
                            w.removeOutEdge(label,v)
                        else:
                            v.removeOutEdge(label,w)
                            w.removeInEdge(label,v)

            shoots=ind
        for v in delta_k0k.vertices[::-1]:
            if len(v.inedgesList)+len(v.outedgesList)==0: # remove isolated vertices from k0k
                delta_k0k.removeVertex(v)
        for v in delta_k0k.vertices: #give vertices of k0k their new names
            v.nu_im={v.label} #part d
            v.name='({0},{1})'.format(v.label,k) #part c
            v.label='({0},{1})'.format(v.label,k) #part c

        #Next remove components of delta_k1k which have only edges of type Z
        #First construct the spanning forest, which also finds connected components (identified by col)
        bfs(delta_k0k,).forest()
        Dcomponents={}
        #construct a dictionary with key the components of delta_k0k and for such key a value list of vertices in that component
        #this should be made into a function
        for u in  delta_k0k.vertices:
            if str(u.colour) in Dcomponents:
                L=Dcomponents[str(u.colour)]
                L.append(u)
                L.sort(key=lambda x: x.length)
                Dcomponents[str(u.colour)]=L
            else:
                Dcomponents[str(u.colour)]=[u]

        for col in Dcomponents:
            col_edge_found=0
            #for each component check each vertex to see if it is incident to an edge of type X_k. If one such is found break out of this loop
            while True:
                for v in Dcomponents[col]:
                    for e in v.inedgesList:
                        if e[0] not in Z.mongens:
                            col_edge_found=1
                            break

                    for e in v.outedgesList:
                        if e[0] not in Z.mongens:
                            col_edge_found=1
                            break
                    
                break
            
            if col_edge_found==0: # if no edges of type X_k are found remove all vertices of this component
                for v in Dcomponents[col]:
                    delta_k0k.removeVertex(v)

                        




        delta_k0.append(delta_k0k) #append k0k to the list of delta1 and delta2
    return delta_k0[0],delta_k0[1],delta_z #these are distinct graphs built from copies of delta

def Mod1(delta_k0,Z,H,verbose,logfile):#input delta_k0(X1 and X2 components), Z gens, H subgroup and its folding. For each Z edge, add a corresponding path in X_k generators 
    flower1=H[0].flower
    flower2=H[1].flower
    flower=(flower1,flower2)
    delta_k1=[]
    for k in (1,2):
        delta_k1k=delta_k0[k-1]# 
        for v in delta_k1k.vertices: #for each vertex v of delta_k0, set original to 0
            v.original=0
        for v in delta_k1k.vertices: #for each vertex v of k1k  
            for outedges in v.outedgesList:# for each outedge e incident to v
                if outedges[0] in Z.mongens: #with a Z label
                    if verbose[4]>1:
                        output_log_file(logfile,"H"+ str(k)+ "free gens"+ str(H[k-1].subgroup_free_gens))
                        output_log_file(logfile,"v"+ str(v)+ "outedges [1]"+ str(outedges[1])+ "outedges [0]"+ str([outedges[0]])+ "k"+ str(k))
                        Xword=phi(H[k-1],[outedges[0]])[0]
                    xword=H[k-1].subgroup_free_gens[outedges[0]]
                    if verbose[4]>1:
                        output_log_file(logfile,"Xword is "+ str(Xword))
                        output_log_file(logfile,"xword is "+ str(xword))

                    test_for_path=graph_pass(delta_k1k,xword,v).acc_read_rem()
                    if test_for_path[2]!=[] or  test_for_path[3]!=outedges[1]:#if this path already exists -- do nothing
                        delta_k1k.addPath(v,outedges[1],xword)# add  a path of x's with the same end points as e
                        if verbose[4]>=1:
                            output_log_file(logfile,"Mod 1: new path "+str(xword)+" added from "+str(v)+" to "+str(outedges[1])+"\n")
                            
        
        for v in delta_k1k.vertices:# for each v in k1k
            if not hasattr(v,'original'):
                v.original=1 # original equals 1, for those vertices added in modification 1
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k) 
                v.label='({0},{1})'.format(v.label,k)
        go = True
        while go: #fold k1k, updating of v.nu_im in the process
            go = delta_k1k.fold()

        delta_k1.append(delta_k1k)#add k1k to delta_k1
    return (delta_k1[0],delta_k1[1]) #return delta_k1, both components


def Mod2(delta1,H,verbose,logfile): #each of delta1 and flower is a pair (delta1_1,delta1_2) and (flower1,flower2); the latter of Stallings foldings
#Mod2 constructs the product of delta_k and flowerk, then a spanning forest for this graph, then carries out Algorithm III steps D6 and D7
    Hflower1=H[0].flower
    Hflower2=H[1].flower
    Hflower=(Hflower1,Hflower2)
    delta2=[]
    Prod=[]
    Prod_components=[]# probably don't need this to be returned
    for k in (0,1):
        delta2k=delta1[k]# the new component to be constructed
        Prod.append(delta1[k].product(Hflower[k],1))
        Prod_bfs=bfs(Prod[k],sorted(Prod[k].vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
        Prod_bfs.forest()#assigns properties, like distance from root, path from root in forest, etc. to vertices of product

        Pcomponents={}
        #construct a dictionary with key the components of the product P_k and for such key a value list of vertices in that component
        for u in  Prod[k].vertices:
            if str(u.colour) in Pcomponents:
                L=Pcomponents[str(u.colour)]
                L.append(u)
                L.sort(key=lambda x: x.length)
                Pcomponents[str(u.colour)]=L
            else:
                Pcomponents[str(u.colour)]=[u]

                
        #if str(u.label).endswith('1'): #if the right hand label is 1, add this vertex to the dictionary entry for its component
        for col in Pcomponents:
            i=0
            for v in Pcomponents[col]:
                if str(v.label).endswith('1'): #if the right hand label is 1, 
                    if i==0:
                        v_base=v # this is the first vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        if verbose[5]>1:
                            output_log_file(logfile,"In mod 2, k is"+str(k)+ "v_base is "+ str(v)+" v_base.path is "+ str(v.path))
                        a=element(v.path).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        i=1 
                    else:
                        b=element(v.path).word # the path from the root of this component to the next vertex of type (*,*)-1
                        Xword=element(a+b).word # the path from v_base to v, in the spanning forest for Prod[k]
                        Gword=graph_pass(Hflower[k],Xword).acc_read_rem() #find the Z word corresponding to Xword
                        if verbose[5]>1:
                            output_log_file(logfile,"In mod 2, still, v is "+ str(v)+" v.path is "+ str(v.path)+ "Xword is"+ str(Xword)+"Gword is "+ str(Gword[4]))
                        if len(Gword[1])>0 or len(Gword[2])>0:
                            print("Something bad happened in Modification 2: tried to add a path not in H. Here is the output of graph_pass:", Gword)
                            print("and k is ", k, "colour is ", col," v is ",v.label,"path is ", v.path)
                            sys.exit("Exiting from Mod2 for the reasons above")
                        else:
                            Zword=Gword[4]
                            delta_v=v.memory[0] # the left hand (delta) part of the vertex v of the product Prod[k]
                            test_for_path=graph_pass(delta2k,Zword,delta_base).acc_read_rem()
                            if test_for_path[2]!=[] or  test_for_path[3]!=delta_v:#if this path already exists -- do nothing
                                delta2k.addPath(delta_base,delta_v,Zword)# add  a path of Z's from the root of component col to v
                                if verbose[5]>=1:
                                    output_log_file(logfile,"Mod 2: new path "+str(Zword)+" added from "+str(delta_base)+" to "+str(delta_v)+"\n")
                    
        for v in delta2k.vertices:# for each v in k1k
             if not hasattr(v,'original'): #these are the vertices added in Modification 2
                v.original=2 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)
         
        go = True
        while go: #fold k1k, updating of v.nu_im in the process
            go = delta2k.fold()
        Prod_components.append(Pcomponents)#probably don't need this
        delta2.append(delta2k)
        
            
    #print("in md2",Prod)
    return(delta2,Prod)


def Mod3(delta2,H,verbose,logfile): #each of delta2 and flower is a pair (delta2_1,delta2_2) and (flower1,flower2) as in Mod2.
    #Mod3 uses the product graph Prod[k] and its components Prod_components[k] from Mod2, as these are essentially the same, and carries out Algorithm III steps D8 and D10
    Hflower1=H[0].flower
    Hflower2=H[1].flower
    Hflower=(Hflower1,Hflower2)
    delta3=[]
    Prod=[]
    for k in (0,1):
        delta3k=delta2[k]# the new component to be constructed
        Prod.append(delta2[k].product(Hflower[k],1))
        Prod_bfs=bfs(Prod[k],sorted(Prod[k].vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
        Prod_bfs.forest()#assigns properties, like distance from root, path from root in forest, etc. to vertices of product

        Pcomponents={}
        #construct a dictionary with key the components of the product P_k and for such key a value list of vertices in that component
        for u in  Prod[k].vertices:
            if str(u.colour) in Pcomponents:
                L=Pcomponents[str(u.colour)]
                L.append(u)
                L.sort(key=lambda x: x.length)
                Pcomponents[str(u.colour)]=L
            else:
                Pcomponents[str(u.colour)]=[u]

        for col in Pcomponents: 
            if verbose[6]>1:
                output_log_file(logfile,"col is"+ str(col))
            i=0
            if len(Pcomponents[col])!=1: # if there is only one vertex in a component, go to the next component
                for v in Pcomponents[col]:
                    if str(v.label).endswith('1'):#find the first vertex with right hand label 1 in component col 
                        v_base=v # this is the first vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        a=element(v.path).word
                        A=element(a).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        i=1 #set this to 1 to show we found a vertex of type (*,*)-1
                        if verbose[6]>1:
                            output_log_file(logfile,"first (*,*)-1 is"+ str(v_base)+ " for col "+ str(col))
                        break
                if i==1: # if there are no vertices of form (*,*)-1 in this component; go to the next component (col)
                    for v in Pcomponents[col]:
                        if verbose[6]>1:
                            output_log_file(logfile,"v is "+ str(v))
                        for e in v.outedgesList:
                            if verbose[6]>1:
                                output_log_file(logfile,"e is"+ str(e))
                                output_log_file(logfile,"an edge "+ str(e)+"with out lab"+ str(v.outedges_write[e]))
                            if len(v.outedges_write[e])!=0:
                                b=element(v.path).word # path from root to v, the initial end of edge e
                                c=element([e[0]]).word # label of e
                                d=element(e[1].path).inverse() #path from terminal end of edge e to the root
                                Xword=element(a+b+c+d+A).word #loop in forest, based at v_base passing over edge e
                                Gword=graph_pass(Hflower[k],Xword).acc_read_rem() #find the Z word corresponding to Xword
                                if len(Gword[1])>0 or len(Gword[2])>0:
                                    print("Something bad happened in Modification 3: tried to add a path not in H. Here is the output of graph_pass:", Gword)                       
                                    print("and k is ", k, "colour is ", col," v is ",v.label,"path is ", v.path)
                                    sys.exit("Exiting from Mod 3 for the reason above")
                                else:
                                    Zword=Gword[4]
                                    test_for_path=graph_pass(delta3k,Zword,delta_base).acc_read_rem()
                                    if test_for_path[2]!=[] or  test_for_path[3]!=delta_base:#if this path already exists -- do nothing
                                        if verbose[6]>=1:
                                            output_log_file(logfile,"Mod 3: Zword"+ str(Zword)+ "added at"+ str(delta_base)+" \n")
               
        for v in delta3k.vertices:# for each v in k1k
            if not hasattr(v,'original'): #these are the vertices added in Modification 3
                v.original=3 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)

        
        go = True
        while go: #fold delta3k, updating of v.nu_im in the process
            go = delta3k.fold()
        

        delta3.append(delta3k)
        
            
    
    return(delta3,Prod)
#################################
#########
###########################
#Modification 4
def Mod4(delta3,H,verbose,logfile): #each of delta3 and H is a pair (delta2_1,delta2_2) and (H1,H2) as in Mod1, 2, 3.
    #Mod4 constructs  the product graph Prod[k] and its components Prod_components[k] as before, and carries out Algorithm III steps D12 and D13
    #The following should be made into a function, which can be used in each modification   
    Hflower1=H[0].flower
    Hflower2=H[1].flower
    Hflower=(Hflower1,Hflower2)
    delta4=[]
    Prod=[]
    for k in (0,1):
        delta4k=delta3[k]# the new component to be constructed
        Prod.append(delta3[k].product(Hflower[k],1))
        Prod_bfs=bfs(Prod[k],sorted(Prod[k].vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
        Prod_bfs.forest()#assigns properties, like distance from root, path from root in forest, etc. to vertices of product

        Pcomponents={}
        #construct a dictionary with key the components of the product P_k and for such key a value list of vertices in that component
        for u in  Prod[k].vertices:
            if str(u.colour) in Pcomponents:
                L=Pcomponents[str(u.colour)]
                L.append(u)
                L.sort(key=lambda x: x.length)
                Pcomponents[str(u.colour)]=L
            else:
                Pcomponents[str(u.colour)]=[u]

               
        #Prodk=Prod[k]
        #Pcomponents=Prod_components[k]
        #flowerk=flower[k]
        #print("Pcomponents ", Pcomponents, "\n")
        
        for col in Pcomponents: 
            if verbose[7]>1:
                output_log_file(logfile,"col is"+ str(col))
            #i=0
            if len(Pcomponents[col])!=1: # if there is only one vertex in a component, go to the next component
                for v in Pcomponents[col]:
                    if verbose[7]>1:
                        output_log_file(logfile,"component, vertex, v.label, lhs-original "+ str(col)+ str(v)+ str(v.label)+ str(v.memory[0].original))
                    #find the next vertex with right hand label 1, which is a vertex of delta_0, and in component col 
                    if str(v.label).endswith('1') and v.memory[0].original==0:
                        if verbose[7]>1:
                            output_log_file(logfile,str(v)+ " ends with 1 and original")
                        v_base=v # this is the current orginal vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        a=element(v.path).word
                        A=element(a).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        if verbose[7]>1:
                            output_log_file(logfile,"current  (*,*)-1 is  "+ str(v_base)+ " in component "+ str(col))
                        for u in Pcomponents[col]:
                            if verbose[7]>1:
                                output_log_file(logfile,"u vertex, u.label, lhs-original "+str(u)+ str(u.label)+ str(u.memory[0].original))
                            #find the next vertex with right hand label not 1, which is a vertex of delta_0, and  in component col 
                            if u.memory[0].original==0 and not str(u.label).endswith('1'):
                                if verbose[7]>1:
                                    output_log_file(logfile,str(u)+ " does not end with 1, and original")
                                u_goal=u # this is the current original vertex of type (*,*)-b found in this component
                                u_L=u.memory[0]#the left hand (delta) part of u_goal
                                u_R=u.memory[1]#the right hand (Hk) part of u_goal
                                b=element(u_R.path).word# path from the root of folding of Hk to u_R
                                if verbose[7]>1:
                                    output_log_file(logfile,"path b in delta"+ str(b)+ " and u_R "+ str(u_R))
                                b_test=graph_pass(Prod[k],b,v_base).acc_read_rem()
                                if verbose[7]>1:
                                    output_log_file(logfile,"b_test in prod"+ str(b_test))
                                if len(b_test[2])!=0 or b_test[3]!=u:
                                    if verbose[7]>1:
                                        output_log_file(logfile,"something to add in Mod 4 at base "+ str(v)+" goal "+ str(u))
                                    p=element(u.path).word# path from the root to u_goal
                                    if verbose[7]>1:
                                        output_log_file(logfile,"in delta, path p "+ str(p))
                                    vu_word=element(A+p).word # path from v_base to u_goal, in tree,
                                    if verbose[7]>1:
                                        output_log_file(logfile,"and path in gamma "+ str(vu_word))
                                    B=element(b).inverse()
                                    HX_word=element(vu_word+B).word # element of H, in terms of Xk
                                    HZ_word=graph_pass(Hflower[k],HX_word).acc_read_rem()[4] #the Z word corresponding to HX_word
                                    word=HZ_word+b

                                    test_for_path=graph_pass(delta4k,word,delta_base).acc_read_rem()
                                    if test_for_path[2]!=[] or  test_for_path[3]!=u_L:#if this path already exists -- do nothing
                                        if verbose[7]>=1:
                                            output_log_file(logfile,"Mod 4: path "+str(word)+" added from "+str(delta_base)+" to "+str(u_L)+"\n")
                                        delta4k.addPath(delta_base,u_L,word)# add  a path with label word from delta_base to u_L of
                                    
            else:#delete this after testing
                if verbose[7]>1:
                    text="only one tea in typhoo "+str(col)+" "+str(Pcomponents[col])
                    output_log_file(logfile,text)
        for v in delta4k.vertices:# for each v in k1k
            if not hasattr(v,'original'): #these are the vertices added in Modification 4
                v.original=4 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)
 
        
        go = True
        while go: #fold delta4k, updating of v.nu_im in the process
            go = delta4k.fold()
        

        delta4.append(delta4k)
        
            
    
    return(delta4,Prod)
#######################################
#Modification 5
def Mod5(delta4,H,verbose,logfile): #each of delta4 and H is a pair (delta4_1,delta4_2) and (H1,H2) as in Mod1, 2, 3, 4.
    #Mod5 constructs  the product graph Prod[k] and its components Prod_components[k] as before, and carries out Algorithm III steps D14 and D17
    #The following should be made into a function, which can be used in each modification   
    Hflower1=H[0].flower
    Hflower2=H[1].flower
    Hflower=(Hflower1,Hflower2)
    delta5=[]
    Prod=[]
    for k in (0,1):

        delta5k=delta4[k]# the new component to be constructed
        Prod.append(delta4[k].product(Hflower[k],1))
        Prod_bfs=bfs(Prod[k],sorted(Prod[k].vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
        Prod_bfs.forest()#assigns properties, like distance from root, path from root in forest, etc. to vertices of product
        
        #make a list of vertices of the original - delta0
        original_vertices=[]
        for v in delta5k.vertices:
            if v.original==0:
                original_vertices.append(v)
                
        Pcomponents={}
        Pcomp_1={}
        #construct a dictionary with key the components of the product P_k and for such key a value list of vertices in that component
        #simultaneously construct a dictionary with the same keys and value list vertices of the form v-1, where v is a vertex of delta0
        for u in  Prod[k].vertices:
            if str(u.colour) in Pcomponents:
                L=Pcomponents[str(u.colour)]
                L.append(u)
                L.sort(key=lambda x: x.length)
                Pcomponents[str(u.colour)]=L
            else:
                Pcomponents[str(u.colour)]=[u]
                
            if str(u.label).endswith('1'):#for vertices with right hand label 1 
                u_pair=u.label.split("-",1)#get hold of the left and right parts of the vertex label 
                for l in original_vertices:
                    if str(u_pair[0])==l.label:# if left part of u is original add u to the dictionary
                        if str(u.colour) in Pcomp_1:
                            L=Pcomp_1[str(u.colour)]
                            L.append((u,l))
                            #L.sort(key=lambda x: x.length)
                            Pcomp_1[str(u.colour)]=L
                        else:
                            Pcomp_1[str(u.colour)]=[(u,l)]
                        break

        for v in H[k].double.vertices:
            v_pair=v.label.split("-",1)#get hold of the left and right parts of the vertex label 
            v_l=int(v_pair[0])#left part of v
            v_r=int(v_pair[1])#right part of v
            if v_l!=v_r: #do not consider diagonal elements (v,v) of the double
                if verbose[8]>1:
                    output_log_file(logfile,"pair (e1,e2) "+str(v)+" "+str(v_pair)+" "+str(v_l)+str(v_r))
                c=element(v.path).inverse()
                v_root=H[k].double.components[v.colour] #the root of the double, containing (LHS_u,RHS_u)
                if verbose[8]>1:
                    output_log_file(logfile,"root "+str(v_root))
                v_root_pair=v_root.label.split("-",1)#get hold of the left and right parts of the vertex label 
                v_root_list=v_root.label.partition("-")
                v_root_l=int(v_root_pair[0])#left part of v
                v_root_r=int(v_root_pair[1])#right part of v
                for y in Hflower[k].vertices:
                    if y.label==v_root_l:
                        a_l=element(y.path).word
                        A_l=element(y.path).inverse()
                    elif y.label==v_root_r:
                        a_r=element(y.path).word
                        A_r=element(y.path).inverse()
                if a_l is None or a_r is None:
                    error_message="Exiting from Mod 5. Path a_l or a_r was not set at vertex "+str(v)+" with root "+str(v_root)+" a_l is "+str(a_l)+" a_r is "+str(a_r)
                    sys.exit(error_message)

                for m in original_vertices:
                    v1=m.label+"-"+str(v_l)
                    v2=m.label+"-"+str(v_r)
                    if verbose[8]>1:
                        output_log_file(logfile,"m is "+ str(m)+ " v1 and v2 "+str(v1)+ " and "+ str(v2))
                    w1_found=0
                    w2_found=0
                    for w in Prod[k].vertices:
                        if w1_found==0 and w.label==v1:
                            w1_found=1
                            w1=w
                        elif w2_found==0 and w.label==v2:
                            w2_found=1
                            w2=w
                        if w1_found==1 and w2_found==1:
                            break
                    col1=str(w1.colour)
                    col2=str(w2.colour)
                    if verbose[8]>1:
                        output_log_file(logfile,"w1 colour, w2 colour "+str(w1)+ ": " +str(col1)+ " and "+str(w)+ ": "+str(col2))
                    #find vertices u-1 and v-1 in the components col1 and col2 
                    if col1 in Pcomp_1 and col2 in Pcomp_1:
                        for (a_1,l_1) in Pcomp_1[col1]: #a_1 has format l_1-1
                            for (a_2,l_2) in Pcomp_1[col2]:#a_2 has format l_2-1
                                if verbose[8]>1:
                                    output_log_file(logfile,"a_1,a_2 is "+str(a_1)+" "+str(a_2))
                                t_1a=element(a_1.path).inverse()#path from a_1 to root
                                t_2a=element(a_2.path).inverse()#path from a_2 to root
                                t_1b=element(w1.path).word#path from root to w1
                                t_2b=element(w2.path).word#path from root to w2
                                t_1=element(t_1a+t_1b).word#path from a_1 to w1
                                t_2=element(t_2a+t_2b).word#path from a_2 to w2
                                Xleft=element(t_1+c+A_l).word
                                Zleft=graph_pass(Hflower[k],Xleft).acc_read_rem()[4] #the Z word corresponding to Xleft
                                Xright=element(t_2+c+A_r).inverse()
                                Zright=graph_pass(Hflower[k],Xright).acc_read_rem()[4] #the Z word corresponding to Xright
                                word=Zleft+a_l+A_r+Zright
                                    
                                test_for_path=graph_pass(delta5k,word,l_1).acc_read_rem()
                                if test_for_path[2]!=[] or  test_for_path[3]!=l_2:#if this path already exists -- do nothing
                                    delta5k.addPath(l_1,l_2,word)# add  a path with label word from l_1 to l_2 of delta5k 
                                    if verbose[8]>=1:
                                        output_log_file(logfile,"Mod 5:new path "+str(word)+" added from "+str(l_1)+" to "+str(l_2)+"\n")
                                #else:
                                #    if verbose[8]>=1:
                                #        output_log_file(logfile,"existing path not added "+str(word)+" from "+str(l_1)+" to "+str(l_2)+"\n\n")
                                
       
        for v in delta5k.vertices:# for each v in k1k
            if not hasattr(v,'original'): #these are the vertices added in Modification 5
                v.original=5 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)
 
        
        go = True
        while go: #fold delta5k, updating of v.nu_im in the process
            go = delta5k.fold()
                                
        #add newly constructed k component as kth element of delta5       
        delta5.append(delta5k)
            
    return(delta5,Prod)
