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


def MakeComps(delta,F,Z,verbose): #input Delta, free groups F=(F1,F2) and Z generators
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
                #print("k is ", k, " v name, v label ", v.name, v.label)
                edgesList=v.inedgesList+v.outedgesList # make a list of all edges incident to v
                v_in_delta_z=0
                for u in delta_z.vertices: #now test to see if this vertex v is in the Z component, delta_z
                            if v.label==u.label:
                                v_in_delta_z=1# set this flag to 1 if v is already in delta_z
                                vcopy=u # keep track of which vertex of delta_z is equal to v
                if len(edgesList)==1: # if we have a shoot with leaf v
                    #print(edgesList)
                    if edgesList[0][0] in Z.mongens: # and the shoot has a label in Z
                        ind+=1
                        #print("ind is ", ind)
                        #print("we found an edge to remove:", edgesList[0])
                        vv_in_delta_z=0
                        for u in delta_z.vertices:
                            #print("u is", u, " and edgesList[0] is ", edgesList[0])
                            if edgesList[0][1].label==u.label: 
                                vv_in_delta_z=1# set this flag to 1 if the other end of this edge is already in delta_z
                                vvcopy=u # and in this case keep track of the vertex of delta_z at the other end of the shoot with leaf v
                                #print("found that vertex ", edgesList[0][0], "is already in delta_z")
                                break
                        if v_in_delta_z==0: # v is not already in delta_z
                            vcopy=delta_z.addVertex(v.name) # add a new vertex to delta_z with same descr as v
                            vcopy.label=v.label
                            #print("v looks like",v.label,v.name)
                            #print("vcopy looks like",vcopy.label,vcopy.name)
                            v_in_delta_z=1 # record that v is now in delta_z
                            #print("k is", k, " added vertex v", vcopy.label)
                        if vv_in_delta_z==0: #if the other end of the shoot is not in delta_z
                            vv=edgesList[0][1]
                            vvcopy=delta_z.addVertex(vv.name)# add it to delta_z
                            vvcopy.label=vv.label
                            #print("k is", k, " added vertex to delta_z vv with label and name", vvcopy.label, vvcopy.label)
                            vv_in_delta_z=1 #record that this vertex is now in delta_z
                    
                        if len(v.inedgesList)==1: #if the shoot is an inedge at v
                            #print("k is ", k,"v is ", v," inedges are", v.inedgesList, "outedges are ",v.outedgesList)
                            #if the edge is already incident to vcopy in delta_z, do nothing
                            if (edgesList[0][0],edgesList[0][1]) not in vcopy.inedgesList:  #print("nothing to do")
                            #else:   #else add an edge to delta_z
                                delta_z.addEdge(vvcopy,vcopy,edgesList[0][0])#print("adding edge , edgesList[0] is ",edgesList[0],"vcopy.inedgesList is ", vcopy.inedgesList)   
                            #print("k is", k, "vcopy,vvcopy=", vcopy,vvcopy, " added edge vv to v with label", edgesList[0][0])
                        elif len(v.outedgesList)==1:#if the shoot is an outedge at v
                            #if the edge is already incident to vcopy in delta_z, do nothing#print("nothing doing")
                            if (edgesList[0][0],edgesList[0],[1]) not in vcopy.outedgesList:
                            #else:  #else add an edge to delta_z
                                delta_z.addEdge(vvcopy,vcopy,edgesList[0][0]) 
                                #print("adding edge , edgesList[0] is ",edgesList[0],
                                #     "vcopy.inedgesList is ", vcopy.inedgesList)
                                #print("k is", k, "vcopy,vvcopy=", vcopy,vvcopy, " added edge vv to v with label", edgesList[0][0])
                        else:
                            print("something is wrong in alg3_alt2 at vertex v", v)
                        #print("vcopy.inedgesList is ",vcopy.inedgesList)
                        #print("vcopy.outedgesList is ",vcopy.outedgesList)
                        #print("vvcopy.inedgesList is ",vvcopy.inedgesList)
                        #print("vvcopy.outedgesList is ",vvcopy.outedgesList)
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
            #print("v.label", v.label)
            v.nu_im={v.label} #part d
            v.name='({0},{1})'.format(v.label,k) #part c
            v.label='({0},{1})'.format(v.label,k) #part c
            #print("here we are in MakeComps and vertex v =", v.label, "has v-im set to", v.nu_im)

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

def Mod1(delta_k0,Z,H,verbose):#input delta_k0(X1 and X2 components), Z gens, H subgroup and its folding. For each Z edge, add a corresponding path in X_k generators- probably don't need to input flower - it comes with H now
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
                    #print("H",k, "free gens", H[k-1].subgroup_free_gens)
                    #print("v", v, "outedges [1]", outedges[1], "outedges [0]", [outedges[0]], "k", k)
                    #Xword=phi(H[k-1],[outedges[0]])[0]
                    xword=H[k-1].subgroup_free_gens[outedges[0]]
                    #print("Xword is ", Xword)
                    #print("xword is ", xword)
                    #Try_to_read_Xword=graph_pass(delta_k1k,Xword,v).acc_read_rem()
                    #print("output of try to read", Try_to_read_Xword)
                    delta_k1k.addPath(v,outedges[1],xword)# add  a path of x's with the same end points as e

        
        for v in delta_k1k.vertices:# for each v in k1k
            #foundv=0
            if not hasattr(v,'original'):
                #print("here's a new vertex", v.label)
                v.original=1 # original equals 1, for those vertices added in modification 1
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k) 
                v.label='({0},{1})'.format(v.label,k)
                #print("v is", v," v.nu_im is", v.nu_im)
        go = True
        while go: #fold k1k, updating of v.nu_im in the process
            go = delta_k1k.fold()

        delta_k1.append(delta_k1k)#add k1k to delta_k1
    return (delta_k1[0],delta_k1[1]) #return delta_k1, both components


def Mod2(delta1,H,verbose): #each of delta1 and flower is a pair (delta1_1,delta1_2) and (flower1,flower2); the latter of Stallings foldings
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
            #for v in Pcomponents[col]:
            #   if v.parent=v:
            #       col_root=v #find the root of this component (as determined by the bfs function of alg1)
            #   break
            #delta_root=col_root.memory[0] #this is the left hand component of the vertex col_root (i.e. u, where col_root =(u,v)
            i=0
            for v in Pcomponents[col]:
                if str(v.label).endswith('1'): #if the right hand label is 1, 
                    if i==0:
                        v_base=v # this is the first vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        #print("In mod 2, k is", k, "v_base is ", v," v_base.path is ", v.path)
                        a=element(v.path).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        i=1 
                    else:
                        b=element(v.path).word # the path from the root of this component to the next vertex of type (*,*)-1
                        Xword=element(a+b).word # the path from v_base to v, in the spanning forest for Prod[k]
                        Gword=graph_pass(Hflower[k],Xword).acc_read_rem() #find the Z word corresponding to Xword
                        #print("In mod 2, still, v is ", v," v.path is ", v.path, "Xword is",Xword,"Gword is ",Gword[4])
                        if len(Gword[1])>0 or len(Gword[2])>0:
                            print("Something bad happened in Modification 2: tried to add a path not in H. Here is the output of graph_pass:", Gword)
                            print("and k is ", k, "colour is ", col," v is ",v.label,"path is ", v.path)
                            sys.exit("Exiting from Mod2 for the reasons above")
                        else:
                            Zword=Gword[4]
                            delta_v=v.memory[0] # the left hand (delta) part of the vertex v of the product Prod[k]
                            delta2k.addPath(delta_base,delta_v,Zword)# add  a path of Z's from the root of component col to v 
                    
        for v in delta2k.vertices:# for each v in k1k
            #print("k is", k, "v is", v.label, "and hasattr orig is", hasattr(v,'original'))
            if not hasattr(v,'original'): #these are the vertices added in Modification 2
                v.original=2 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)
                #print("v is", v," v.nu_im is", v.nu_im)
        
        go = True
        while go: #fold k1k, updating of v.nu_im in the process
            go = delta2k.fold()
        Prod_components.append(Pcomponents)#probably don't need this
        delta2.append(delta2k)
        
            
    #print("in md2",Prod)
    return(delta2,Prod)


def Mod3(delta2,H,verbose): #each of delta2 and flower is a pair (delta2_1,delta2_2) and (flower1,flower2) as in Mod2.
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

               
        #Prodk=Prod[k]
        #Pcomponents=Prod_components[k]
        #flowerk=flower[k]
        #print("Pcomponents ", Pcomponents, "\n")
        
        for col in Pcomponents: 
            if verbose==1:
                print("col is", col)
            i=0
            if len(Pcomponents[col])!=1: # if there is only one vertex in a component, go to the next component
                for v in Pcomponents[col]:
                    if str(v.label).endswith('1'):#find the first vertex with right hand label 1 in component col 
                        v_base=v # this is the first vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        a=element(v.path).word
                        A=element(a).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        i=1 #set this to 1 to show we found a vertex of type (*,*)-1
                        if verbose==1:
                            print("first (*,*)-1 is", v_base, " for col ", col)
                        break
                if i==1: # if there are no vertices of form (*,*)-1 in this component; go to the next component (col)
                    for v in Pcomponents[col]:
                        if verbose==1:
                            print("v is ", v)
                        for e in v.outedgesList:
                            if verbose==1:
                                print("e is", e)
                                print("an edge ", e,"with out lab",v.outedges_write[e])
                            if len(v.outedges_write[e])!=0:
                                #if verbose==1:
                                #    print("an edge ", e,"with out lab",v.outedges_write[e])
                                #delta_root=col_root.memory[0]
                                b=element(v.path).word # path from root to v, the initial end of edge e
                                c=element([e[0]]).word # label of e
                                d=element(e[1].path).inverse() #path from terminal end of edge e to the root
                                Xword=element(a+b+c+d+A).word #loop in forest, based at v_base passing over edge e
                                #print("Xword", Xword)
                                Gword=graph_pass(Hflower[k],Xword).acc_read_rem() #find the Z word corresponding to Xword
                                if len(Gword[1])>0 or len(Gword[2])>0:
                                    print("Something bad happened in Modification 3: tried to add a path not in H. Here is the output of graph_pass:", Gword)                       
                                    print("and k is ", k, "colour is ", col," v is ",v.label,"path is ", v.path)
                                    sys.exit("Exiting from Mod 3 for the reason above")
                                else:
                                    Zword=Gword[4]
                                    if verbose==1:
                                        print("Zword", Zword, "added at", delta_base," \n\n")
                                    delta3k.addPath(delta_base,delta_base,Zword)# add  a path of Z's from the root of component col to itself      
                #else:
                    #print("Pcomponent ", col," has no (*,1) ", Pcomponents[col])
            #else:
                #print("Pcomponent", col,"can be missed as it is ",Pcomponents[col])
                
        for v in delta3k.vertices:# for each v in k1k
            #print("k is", k, "v is", v.label, "and hasattr orig is", hasattr(v,'original'))
            if not hasattr(v,'original'): #these are the vertices added in Modification 3
                v.original=3 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)
                #print("v is", v," v.nu_im is", v.nu_im)
        
        go = True
        while go: #fold delta3k, updating of v.nu_im in the process
            go = delta3k.fold()
        

        delta3.append(delta3k)
        
            
    
    return(delta3,Prod)
#################################
#########
###########################
#Modification 4
def Mod4(delta3,H,verbose): #each of delta3 and H is a pair (delta2_1,delta2_2) and (H1,H2) as in Mod1, 2, 3.
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
            if verbose==1:
                print("col is", col)
            #i=0
            if len(Pcomponents[col])!=1: # if there is only one vertex in a component, go to the next component
                for v in Pcomponents[col]:
                    print("component, vertex, v.label, lhs-original ",col, v, str(v.label),v.memory[0].original)
                    #find the next vertex with right hand label 1, which is a vertex of delta_0, and in component col 
                    if str(v.label).endswith('1') and v.memory[0].original==0:
                        print(v, " ends with 1 and original")
                        v_base=v # this is the current orginal vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        a=element(v.path).word
                        A=element(a).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        if verbose==1:
                            print("current  (*,*)-1 is  ", v_base, " in component ", col)
                        for u in Pcomponents[col]:
                            print("u vertex, u.label, lhs-original ",u, str(u.label),u.memory[0].original)
                            #find the next vertex with right hand label not 1, which is a vertex of delta_0, and  in component col 
                            if u.memory[0].original==0 and not str(u.label).endswith('1'):
                                print(u, " does not end with 1, and original")
                                u_goal=u # this is the current orginal vertex of type (*,*)-b found in this component
                                u_L=u.memory[0]#the left hand (delta) part of u_goal
                                u_R=u.memory[1]#the right hand (Hk) part of u_goal
                                b=element(u_R.path).word# path from the root of folding of Hk to u_R
                                b_test=graph_pass(Prod[k],b,v_base).acc_read_rem() 
                                if len(b_test[2])!=0 or b_test[3]!=u_R:
                                    if verbose==1:
                                        print("something to add in Mod 4 at base ", v," goal ", u)
                                    p=element(u.path).word# path from the root to u_goal
                                    vu_word=element(A+p).word # path from v_base to u_goal, in tree,
                                    B=element(b).inverse()
                                    HX_word=element(vu_word+B).word # element of H, in terms of Xk
                                    HZ_word=graph_pass(Hflower[k],HX_word).acc_read_rem()[4] #the Z word corresponding to HX_word
                                    word=HZ_word+b
                                    
                                    if verbose==1:
                                        print("path", word, "added from", delta_base," to ", u_L, "\n\n")
                                    delta4k.addPath(delta_base,delta_base,word)# add  a path with label word from delta_base to u_L of 
                               
        for v in delta4k.vertices:# for each v in k1k
            #print("k is", k, "v is", v.label, "and hasattr orig is", hasattr(v,'original'))
            if not hasattr(v,'original'): #these are the vertices added in Modification 4
                v.original=4 # 
                v.nu_im={v.label}
                v.name='({0},{1})'.format(v.label,k+1) 
                v.label='({0},{1})'.format(v.label,k+1)
                #print("v is", v," v.nu_im is", v.nu_im)
        
        go = True
        while go: #fold delta4k, updating of v.nu_im in the process
            go = delta4k.fold()
        

        delta4.append(delta4k)
        
            
    
    return(delta4,Prod)
