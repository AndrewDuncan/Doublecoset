from alg2 import *
from input import * #temporary, will eventually be included in the above import
import copy

def alg3_pre():#not used as far as I know
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
    return F,Z,H1,H2#,flower1,double1# this should return in a more systematic fashionnw=amalgam_normal_form(w,F1,F2,H1,H2)


def MakeComps(delta,F,Z,verbose,logfile): #input Delta, free groups F=(F1,F2) and Z generators
    delta_k0=[] # to become a pair of graphs, one for each X_i
    delta_z=Graph(False,'Delta Z') # the Z component, composed of edges labelled with letters of Z, removed in the process of pruning shoots
    for k in (1,2): #part a; do the following for X_1 and X_2 components
        #make a copy of delta, leaving out edges with labels in  X_[2-k]: to make a component
        delta_k0k=CopyGraph(delta,F[2-k].mongens)
		
        shoots=1  #part b, remove Z shoots
        while shoots!=0:
            ind=0
            for v in delta_k0k.vertices[::-1]: #for each vertex of k0k
                if verbose[3]>1:
                    output_log_file(logfile,"k is "+ str(k)+" v is "+str(v))
                v_in_delta_z=0
                for u in delta_z.vertices: #now test to see if this vertex v is in the Z component, delta_z
                    if v.label==u.label:
                        v_in_delta_z=1# set this flag to 1 if v is already in delta_z
                        vcopy=u # keep track of which vertex of delta_z is equal to v
                if len(v.inedgesList)+len(v.outedgesList)==1:# if we have a shoot with leaf v
                    if len(v.inedgesList)==1:
                        edge_found=v.inedgesList[0]
                        edge_dir='in'
                    else:
                        edge_found=v.outedgesList[0]
                        edge_dir='out'
                    if edge_found[0] in Z.mongens: # and the shoot has a label in Z
                        ind+=1
                        if verbose[3]>1:
                            output_log_file(logfile,"ind is "+ str(ind))
                            output_log_file(logfile,"we found an "+edge_dir+" edge to remove: "+ str(edge_found))
                        vv_in_delta_z=0
                        for u in delta_z.vertices:#search vertices of delta_z for the other end of the shoot
                            if verbose[3]>1:
                                output_log_file(logfile,"u is"+ str(u)+ " and edge_found is "+ str(edge_found))
                            if edge_found[1].label==u.label: 
                                vv_in_delta_z=1# set this flag to 1 if the other end of this edge is already in delta_z
                                vvcopy=u # and in this case keep track of the vertex of delta_z at the other end of the shoot with leaf v
                                if verbose[3]>1:
                                    output_log_file(logfile,"found that vertex "+ str(edge_found[0])+ " is already in delta_z")
                                break
                        if v_in_delta_z==0: # v is not already in delta_z
                            vcopy=delta_z.addVertex(v.name) # add a new vertex to delta_z with same descr as v
                            vcopy.label=v.label
                            v_in_delta_z=1 # record that v is now in delta_z
                            if verbose[3]>=1:
                                output_log_file(logfile,"D0 (MakeComps): k is "+ str(k)+ ", added vertex v  to delta_z with label: "+ str(vcopy.label))
                        if vv_in_delta_z==0: #if the other end of the shoot is not in delta_z
                            #vv=edgesList[0][1]
                            vv=edge_found[1]
                            vvcopy=delta_z.addVertex(vv.name)# add it to delta_z
                            vvcopy.label=vv.label
                            if verbose[3]>=1:
                                output_log_file(logfile,"D0 (MakeComps): k is "+ str(k)+ ", added vertex vv to  delta_z with label "+ str(vvcopy.label))
                            vv_in_delta_z=1 #record that this vertex is now in delta_z
                    
                        #if len(v.inedgesList)==1: #if the shoot is an inedge at v
                        if edge_dir=='in':
                            if verbose[3]>1:
                                output_log_file(logfile,"k is "+str(k)+" v is "+ str(v)+" inedges are "+ str(v.inedgesList)+ " outedges are "+ str(v.outedgesList))
                            #if the edge is already incident to vcopy in delta_z, do nothing
                            if (edge_found[0],edge_found[1]) not in vcopy.inedgesList:  
                                delta_z.addEdge(vvcopy,vcopy,edge_found[0])
                                if verbose[3]>=1:
                                    output_log_file(logfile,"D0 (MakeComps): adding edge to delta_z, edge_found is "+ str(edge_found))
                                    output_log_file(logfile,"k is "+ str(k)+ ", vv, v = "+ str(vcopy)+", "+ str(vvcopy)+ "; added edge from vv to v with label "+ str(edge_found[0]))

                        #elif len(v.outedgesList)==1:#if the shoot is an outedge at v
                        elif edge_dir=='out':#if the shoot is an outedge at v
                            #if the edge is already incident to vcopy in delta_z, do nothing
                            if (edge_found[0],edge_found[1]) not in vcopy.outedgesList:
                                delta_z.addEdge(vcopy,vvcopy,edge_found[0]) 
                                if verbose[3]>=1:
                                    output_log_file(logfile,"D0 (MakeComps):adding edge to delta_z, edge_found is "+ str(edge_found))
                                    output_log_file(logfile,"k is "+ str(k)+ " v, vv = "+ str(vcopy)+ ", "+str(vvcopy)+ "; added edge from v to vv with label "+ str(edge_found[0]))
                        else:
                            error_message="Exiting from Makecomps: something is wrong at vertex v "+str(v)
                            sys.exit(error_message)
 
                        label=edge_found[0]
                        w=edge_found[1]
                        w.boundary=1# as w has had a shoot removed from it, mark it as a boundary vertex
                        if verbose[3]>=1:
                            output_log_file(logfile,"set boundary of "+str(w)+" to 1")
                        if (label,w) in v.inedgesList: #now remove the shoot from the in or out edges of the non-leaf end
                            v.removeInEdge(label,w)
                            w.removeOutEdge(label,v)
                        elif (label,w) in v.outedgesList:
                            v.removeOutEdge(label,w)
                            w.removeInEdge(label,v)
                        else:
                            error_message="Exiting from Makecomps: something is wrong at vertex v "+str(v)+" shoot "+str(edge_found)+" an "+edge_dir+" edge"
                            sys.exit(error_message)
 

            shoots=ind
        for v in delta_k0k.vertices[::-1]:
            if len(v.inedgesList)+len(v.outedgesList)==0: # remove isolated vertices from k0k
                if verbose[3]>1:
                    output_log_file(logfile,"vertex "+str(v)+" has no edges: "+str(len(v.inedgesList))+" "+str(len(v.outedgesList)))
                delta_k0k.removeVertex(v)
        for v in delta_k0k.vertices: #give vertices of k0k their new names
            v.nu_im={v.label} #part d
            v.name='({0},{1})'.format(v.label,k) #make name different from label, for printing?
            v.label='({0},{1})'.format(v.label,k) #part c
            v.original=0#vertices of delta_k0k are all original vertices of delta

        #Next remove components of delta_k0k which have only edges of type Z
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

                        


          
        delta_k0.append(delta_k0k) #append k0k to the list of delta01 and delta02
    return delta_k0[0],delta_k0[1],delta_z #these are distinct graphs built from delta

def Mod1(delta_k0,Z,H,verbose,logfile):#input delta_k0(X1 and X2 components), Z gens, H subgroup and its folding. For each Z edge, add a corresponding path in X_k generators 
    flower1=H[0].flower
    flower2=H[1].flower
    flower=(flower1,flower2)
    delta_k1=[]
    for k in (1,2):
        delta_k1k=delta_k0[k-1]# 
        #for v in delta_k1k.vertices: #for each vertex v of delta_k0, set original to 0
        #    v.original=0
        for v in delta_k1k.vertices: #for each vertex v of k1k  
            for outedges in v.outedgesList:# for each outedge e incident to v
                if outedges[0] in Z.mongens: #with a Z label
                    if verbose[4]>1:
                        output_log_file(logfile,"H "+ str(k)+ " free gens "+ str(H[k-1].subgroup_free_gens))
                        output_log_file(logfile,"v "+ str(v)+ " outedges [1] "+ str(outedges[1])+ " outedges [0] "+ str([outedges[0]])+ " k "+ str(k))
                        Xword=phi(H[k-1],[outedges[0]])[0]
                    xword=H[k-1].subgroup_free_gens[outedges[0]]
                    if verbose[4]>1:
                        output_log_file(logfile,"Xword is "+ str(Xword))
                        output_log_file(logfile,"xword is "+ str(xword))

                    test_for_path=graph_pass(delta_k1k,xword,v).acc_read_rem()
                    if test_for_path[2]!=[] or  test_for_path[3]!=outedges[1]:#if this path already exists -- do nothing
                        delta_k1k.addPath(v,outedges[1],xword,"-")# add  a path of x's with the same end points as e
                        if verbose[4]>=1:
                            output_log_file(logfile,"Mod 1: new path "+str(xword)+" added from "+str(v)+" to "+str(outedges[1])+"\n")
                            
                   
        Vmax=0
        for v in delta_k1k.vertices:#find the max of the lhs of the vertex labels of delta_k0k
            if hasattr(v,'original') and v.original==0:
                  if int(v.label.split("(")[1].split(",")[0])> Vmax:
                      Vmax=int(v.label.split("(")[1].split(",")[0])

        Vmax+=1
        for v in delta_k1k.vertices:# for each v in k1k
            if not hasattr(v,'original'):
                v.original=1 # original equals 1, for those vertices added in modification 1
                v.nu_im=set()# the new vertices are not images of vertices of delta
                v.name='({0},{1})'.format(str(Vmax),k) 
                v.label='({0},{1})'.format(str(Vmax),k)
                v.boundary=0
                Vmax+=1

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
                            output_log_file(logfile,"In mod 2, k is "+str(k)+ " v_base is "+ str(v)+" v_base.path is "+ str(v.path))
                        a=element(v.path).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        i=1 
                    else:
                        b=element(v.path).word # the path from the root of this component to the next vertex of type (*,*)-1
                        Xword=element(a+b).word # the path from v_base to v, in the spanning forest for Prod[k]
                        Gword=graph_pass(Hflower[k],Xword).acc_read_rem() #find the Z word corresponding to Xword
                        if verbose[5]>1:
                            output_log_file(logfile,"In mod 2, still, v is "+ str(v)+" v.path is "+ str(v.path)+ " Xword is "+ str(Xword)+" Gword is "+ str(Gword[4]))
                        if len(Gword[1])>0 or len(Gword[2])>0:
                            print("Something bad happened in Modification 2: tried to add a path not in H. Here is the output of graph_pass:", Gword)
                            print("and k is ", k, "colour is ", col," v is ",v.label,"path is ", v.path)
                            sys.exit("Exiting from Mod2 for the reasons above")
                        else:
                            Zword=Gword[4]
                            delta_v=v.memory[0] # the left hand (delta) part of the vertex v of the product Prod[k]
                            test_for_path=graph_pass(delta2k,Zword,delta_base).acc_read_rem()
                            if test_for_path[2]!=[] or  test_for_path[3]!=delta_v:#if this path already exists -- do nothing
                                delta2k.addPath(delta_base,delta_v,Zword,"-")# add  a path of Z's from the root of component col to v
                                if verbose[5]>=1:
                                    output_log_file(logfile,"Mod 2: new path "+str(Zword)+" added from "+str(delta_base)+" to "+str(delta_v)+"\n")
            
        Vmax=0
        for v in delta2k.vertices:#find the max of the lhs of the vertex labels of delta_1k
            if hasattr(v,'original') and v.original<=1:
                  if int(v.label.split("(")[1].split(",")[0])> Vmax:
                      Vmax=int(v.label.split("(")[1].split(",")[0])

        Vmax+=1
        for v in delta2k.vertices:# for each v in k1k
             if not hasattr(v,'original'): #these are the vertices added in Modification 2
                v.original=2 # 
                v.nu_im=set()# the new vertices are not images of vertices of delta
                v.name='({0},{1})'.format(str(Vmax),k+1) 
                v.label='({0},{1})'.format(str(Vmax),k+1)
                v.boundary=0
                Vmax+=1
         
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
                output_log_file(logfile,"col is "+ str(col))
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
                            output_log_file(logfile,"first (*,*)-1 is "+ str(v_base)+ " for col "+ str(col))
                        break
                if i==1: # if there are no vertices of form (*,*)-1 in this component; go to the next component (col)
                    for v in Pcomponents[col]:
                        if verbose[6]>1:
                            output_log_file(logfile,"v is "+ str(v))
                        for e in v.outedgesList:
                            if verbose[6]>1:
                                output_log_file(logfile,"e is "+ str(e))
                                output_log_file(logfile,"an edge "+ str(e)+" with out lab "+ str(v.outedges_write[e]))
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
                                            output_log_file(logfile,"Mod3: Zword "+ str(Zword)+ " added at "+ str(delta_base)+" \n")
                                        delta3k.addPath(delta_base,delta_base,Zword,"-")# add  a path of Z's from the root of component col to itself 
                    
        Vmax=0
        for v in delta3k.vertices:
            if hasattr(v,'original') and v.original<=2:
                  if int(v.label.split("(")[1].split(",")[0])> Vmax:
                      Vmax=int(v.label.split("(")[1].split(",")[0])
                
           
        Vmax+=1
        for v in delta3k.vertices:# for each v in k1k
            if not hasattr(v,'original'): #these are the vertices added in Modification 3
                v.original=3 # 
                v.nu_im=set()# the new vertices are not images of vertices of delta
                v.name='({0},{1})'.format(str(Vmax),k+1) 
                v.label='({0},{1})'.format(str(Vmax),k+1)
                v.boundary=0
                Vmax+=1

        
        go = True
        while go: #fold delta3k, updating of v.nu_im in the process
            go = delta3k.fold()
                
        #for v in delta3k.vertices:
        #    output_log_file(logfile,"In Mod 3, k is "+str(k)+" v "+str(v)+" out edges "+str(v.outedgesList)+" in edges "+str(v.inedgesList))

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
                output_log_file(logfile,"col is "+ str(col)+" Pcomponent[col] length is "+str(len(Pcomponents[col])))
            #i=0
            if len(Pcomponents[col])!=1: # if there is only one vertex in a component, go to the next component
                for v in Pcomponents[col]:
                    if verbose[7]>1:
                        output_log_file(logfile,"component, vertex, v.label, lhs-original, lhs-boundary "+ str(col)+" "+ str(v)+" "+ str(v.label)+" "+ str(v.memory[0].original)+" "+str(v.memory[0].boundary))
                    #find the next vertex with right hand label 1, which is a vertex of delta_0 and a boundary vertex, and in component col 
                    if str(v.label).endswith('1') and v.memory[0].original==0 and v.memory[0].boundary==1:
                        if verbose[7]>1:
                            output_log_file(logfile,"v is "+str(v)+ " v ends with 1 and v.original =  "+str(v.memory[0].original)+" and v.boundary = "+str(v.memory[0].boundary))
                        v_base=v # this is the current orginal vertex of type (*,*)-1 found in this component
                        delta_base=v.memory[0]#the left hand (delta) part of v_base
                        a=element(v.path).word
                        A=element(a).inverse() # the path from v_base to the root of this component (which is usually trivial, as v_base is usually the root)
                        if verbose[7]>1:
                            output_log_file(logfile,"current  (*,*)-1 is  "+ str(v_base)+ " in component "+ str(col))
                        for u in Pcomponents[col]:
                            if verbose[7]>1:
                                output_log_file(logfile,"u vertex, u.label, lhs-original "+str(u)+" "+ str(u.label)+" "+ str(u.memory[0].original)+" "+str(u.memory[0].boundary))
                            #find the next vertex with right hand label not 1, which is a vertex of delta_0 and a boundary vertex, and  in component col 
                            if u.memory[0].original==0 and u.memory[0].boundary==1 and not str(u.label).endswith('1'):
                                if verbose[7]>1:
                                    output_log_file(logfile,str(u)+" does not end with 1, and original = "+str(u.memory[0].original)+" and boundary = "+str(u.memory[0].boundary))
                                u_goal=u # this is the current original vertex of type (*,*)-b found in this component
                                u_L=u.memory[0]#the left hand (delta) part of u_goal
                                u_R=u.memory[1]#the right hand (Hk) part of u_goal
                                b=element(u_R.path).word# path from the root of folding of Hk to u_R
                                if verbose[7]>1:
                                    output_log_file(logfile,"path b in delta "+ str(b)+ " and u_R "+ str(u_R))
                                b_test=graph_pass(Prod[k],b,v_base).acc_read_rem()
                                if verbose[7]>1:
                                    output_log_file(logfile,"b_test in prod "+ str(b_test))
                                if len(b_test[2])!=0 or b_test[3]!=u:
                                    if verbose[7]>1:
                                        output_log_file(logfile,"something to add in Mod 4 at base "+ str(v)+" with goal "+ str(u))
                                    p=element(u.path).word# path from the root to u_goal
                                    if verbose[7]>1:
                                        output_log_file(logfile,"in delta, path p "+ str(p))
                                    vu_word=element(A+p).word # path from v_base to u_goal, in tree,
                                    if verbose[7]>1:
                                        output_log_file(logfile,"and in gamma, path is "+ str(vu_word)+"\n")
                                    B=element(b).inverse()
                                    HX_word=element(vu_word+B).word # element of H, in terms of Xk
                                    HZ_word=graph_pass(Hflower[k],HX_word).acc_read_rem()[4] #the Z word corresponding to HX_word
                                    word=HZ_word+b

                                    test_for_path=graph_pass(delta4k,word,delta_base).acc_read_rem()
                                    if test_for_path[2]!=[] or  test_for_path[3]!=u_L:#if this path already exists -- do nothing
                                        if verbose[7]>=1:
                                            output_log_file(logfile,"Mod 4: path "+str(word)+" added from "+str(delta_base)+" to "+str(u_L)+"\n")
                                        delta4k.addPath(delta_base,u_L,word,"-")# add  a path with label word from delta_base to u_L of
                                 

        Vmax=0
        for v in delta4k.vertices:#find the max of the lhs of the vertex labels of delta4k
            if hasattr(v,'original') and v.original<=3:
                  if int(v.label.split("(")[1].split(",")[0])> Vmax:
                      Vmax=int(v.label.split("(")[1].split(",")[0])

        Vmax+=1
        for v in delta4k.vertices:# for each v in k1k
            if not hasattr(v,'original'): #these are the vertices added in Modification 4
                v.original=4 # 
                v.nu_im=set()# the new vertices are not images of vertices of delta
                v.name='({0},{1})'.format(str(Vmax),k+1) 
                v.label='({0},{1})'.format(str(Vmax),k+1)
                v.boundary=0
                Vmax+=1
 
        
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

        boundary_vertices=[]
        for v in delta5k.vertices:
            if v.boundary==1:
                boundary_vertices.append(v)

        if verbose[8]>1:
            output_log_file(logfile,"\n Mod 5: k = "+str(k)+"\n original vertices: "+str(original_vertices)+"\n boundary vertices : "+str(boundary_vertices))
                
        Pcomponents={}
        Pcomp_1={}
        #construct a dictionary with key the components of the product P_k and for such key a value list of vertices in that component
        #simultaneously construct a dictionary with the same keys and value list pairs of the form (v-1,v), 
        # where v is a boundary vertex of delta0, and v-1 is a vertex of P_k of colour = key 
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
                for l in boundary_vertices:
                    if str(u_pair[0])==l.label:# if left part of u is a boundary vertex add u to the dictionary
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
            if v_l!=v_r: #set a non-diagonal element of the double equal to (e1,e2) 
                if verbose[8]>1:
                    output_log_file(logfile,"\n"+"pair (e1,e2) "+str(v_pair))
                c=element(v.path).inverse()#the connecting element of (e1,e2)
                v_root=H[k].double.components[v.colour] #the root of the double, containing (LHS_u,RHS_u), is the representative (xi1,xi2) of (e1,e2)
                if verbose[8]>1:
                    output_log_file(logfile,"representative of (e1,e2) = v_root = "+str(v_root.label)+"; path c is "+str(c))
                v_root_pair=v_root.label.split("-",1)#get hold of the left and right parts of the vertex label of (xi1,xi2)
                #v_root_list=v_root.label.partition("-")
                v_root_l=int(v_root_pair[0])#left part of v; that is xi1
                v_root_r=int(v_root_pair[1])#right part of v; that is xi2
                for y in Hflower[k].vertices:
                    if y.label==v_root_l:
                        a_l=element(y.path).word#path a1 from xi1 to e1 in spanning tree for folding of Hk
                        A_l=element(y.path).inverse()
                    elif y.label==v_root_r:
                        a_r=element(y.path).word#path a2 from xi2 to e2 in spanning tree for folding of Hk
                        A_r=element(y.path).inverse()
                if a_l is None or a_r is None:
                    error_message="Exiting from Mod 5. Path a_l or a_r was not set at vertex "+str(v)+" with root "+str(v_root)+" a_l is "+str(a_l)+" a_r is "+str(a_r)
                    sys.exit(error_message)

                if verbose[8]>1:
                    output_log_file(logfile,"paths a1 and a2 = a_l and a_r are "+str(a_l)+" and "+str(a_r))

                for m in boundary_vertices:# for all boundary vertices beta
                    v1=m.label+"-"+str(v_l)# try (beta,e1) and 
                    v2=m.label+"-"+str(v_r)# (beta,e2)
                    if verbose[8]>1:
                        output_log_file(logfile,"vertex beta = m is "+ str(m)+ ";  (beta,e1) and (beta,e2) = v1 and v2 are "+str(v1)+ " and "+ str(v2))
                    w1_found=0
                    w2_found=0
                    for w in Prod[k].vertices:#find the vertices of Prod equal to (beta,e1) and (beta,e2): call them w1 and w2
                        if w1_found==0 and w.label==v1:
                            w1_found=1
                            w1=w
                        elif w2_found==0 and w.label==v2:
                            w2_found=1
                            w2=w
                        if w1_found==1 and w2_found==1:
                            break
                    col1=str(w1.colour)#the connected component of (beta,e1)
                    col2=str(w2.colour)#the connected component of (beta,e2)
                    if verbose[8]>1:
                        output_log_file(logfile,"(beta,e1) = w1 = "+str(w1)+ " is in component " +str(col1)+" of Prodk")
                        output_log_file(logfile,"(beta,e2) = w2 = "+str(w2)+ " is in component " +str(col2)+" of Prodk")
                    #find vertices u-1 and v-1 in the components col1 and col2 
                    if col1 in Pcomp_1 and col2 in Pcomp_1:
                        for (a_1,l_1) in Pcomp_1[col1]: #(alpha1,1) = a_1 has format a_1=l_1-1
                            for (a_2,l_2) in Pcomp_1[col2]:#(alpha2,1) = a_2 has format l_2-1
                                if verbose[8]>1:
                                    output_log_file(logfile,"(alpha1,1)=a_1 = "+str(a_1)+" and is in component "+str(col1))
                                    output_log_file(logfile,"(alpha2,1)=a_2 = "+str(a_2)+" and is in component "+str(col2))
                                t_1a=element(a_1.path).inverse()#path from (alpha1,1) = a_1 to root of component of Prodk
                                t_2a=element(a_2.path).inverse()#path from (alpha2,1) = a_2 to root of component of Prodk
                                t_1b=element(w1.path).word#path from root to (beta,e1) = w1
                                t_2b=element(w2.path).word#path from root to (beta,e2) = w2
                                t_1=element(t_1a+t_1b).word#path from (alpha1,1) = a_1 to (beta,e1) = w1
                                t_2=element(t_2a+t_2b).word#path from (alpha2,1) = a_2 to (beta,e2) = w2
                                if verbose[8]>1:
                                    output_log_file(logfile,"path t_1 is "+str(t_1))
                                    output_log_file(logfile,"path t_2 is "+str(t_2))
                                Xleft=element(t_1+c+A_l).word
                                Zleft=graph_pass(Hflower[k],Xleft).acc_read_rem()[4] #the Z word corresponding to Xleft
                                Xright=element(t_2+c+A_r).inverse()
                                Zright=graph_pass(Hflower[k],Xright).acc_read_rem()[4] #the Z word corresponding to Xright
                                word=Zleft+a_l+A_r+Zright
                                    
                                test_for_path=graph_pass(delta5k,word,l_1).acc_read_rem()
                                if test_for_path[2]!=[] or  test_for_path[3]!=l_2:#if this path already exists -- do nothing
                                    delta5k.addPath(l_1,l_2,word,"-")# add  a path with label word from l_1 to l_2 of delta5k 
                                    if verbose[8]>=1:
                                        output_log_file(logfile,"Mod 5:new path "+str(word)+" added from "+str(l_1)+" to "+str(l_2)+"\n")
                                #else:
                                #    if verbose[8]>=1:
                                #        output_log_file(logfile,"existing path not added "+str(word)+" from "+str(l_1)+" to "+str(l_2)+"\n\n")
                                
        Vmax=0
        for v in delta5k.vertices:#find the max of the lhs of the vertex labels of delta4k
            if hasattr(v,'original') and v.original<=4:
                  if int(v.label.split("(")[1].split(",")[0])> Vmax:
                      Vmax=int(v.label.split("(")[1].split(",")[0])

        Vmax+=1
        for v in delta5k.vertices:# for each v in k1k
            if not hasattr(v,'original'): #these are the vertices added in Modification 5
                v.original=5 # 
                v.nu_im=set()# the new vertices are not images of vertices of delta
                v.name='({0},{1})'.format(str(Vmax),k+1) 
                v.label='({0},{1})'.format(str(Vmax),k+1)
                v.boundary=0
                Vmax+=1
 
        
        go = True
        while go: #fold delta5k, updating of v.nu_im in the process
            go = delta5k.fold()
        
        #for v in delta5k.vertices:
        #    output_log_file(logfile,"In Mod 5, k is "+str(k)+" v "+str(v)+" out edges "+str(v.outedgesList)+" in edges "+str(v.inedgesList))
        #add newly constructed k component as kth element of delta5       
        delta5.append(delta5k)
            
    return(delta5,Prod)
########################################
########################################
def Reassemble(delta_5,delta_z,H,verbose,logfile,loop_count):

    delta_n=Graph(False,'Delta_n')#make a new graph; to be the union of delta_5[0], delta_5[1] and delta_z
    root_set=0
    root_found=0
    for k in (0,1): # add vertices of delta[k] to delta_n, k=0,1
        if root_set==0:#set n_root  equal to the root of delta_5[0] --- for later use
            if hasattr(delta_5[k],'root'):
                root_found=1
                n_root=delta_5[k].root
            
        for v in delta_5[k].vertices:#add a vertex to delta_n for each vertex of delta_5[k]
            u=delta_n.addVertex(v.name)
            u.label=v.label
            u.original=v.original
            u.nu_im=v.nu_im
            if root_set==0 and root_found==1 and v==n_root:# when v=n_root, make the  vertex with label v.label the root of delta_n 
                delta_n.root=u
                root_set=1
                if verbose[9]>1:
                    output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": k is "+str(k)+"root of delta_n set to "+str(u))
            if verbose[9]>2:
                output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": k is "+str(k)+" v is "+str(v)+" u is "+str(u)+" label, name, nu_im "+str(u.label)+" "+str(u.name)+" "+str(u.nu_im))
            
    if root_set==0:
        if hasattr(delta_z,'root'):#if no root has been set, set n_root = to the root of delta_z
                root_found=1
                n_root=delta_z.root

    for v in delta_z.vertices:# add vertices of delta_z to delta_n
        name='({0},{1})'.format(v.name,3) 
        label='({0},{1})'.format(v.label,3)
        u=delta_n.addVertex(name)
        u.label=label
        u.original=0
        u.nu_im={v.label}
        if root_set==0 and root_found==1 and v==n_root:
            delta_n.root=u
            root_set=1
            if verbose[9]>1:
                output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": reading in delta_z and root of delta_n set to "+str(u))
        if verbose[9]>2:
             output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": delta_z v is "+str(v)+" u is "+str(u)+" label, name, nu_im  "+str(u.label)+" "+str( u.name)+" "+str(u.nu_im))

    #for z in delta_n.vertices:#test only -remove when pgm is working
        #if z.label=='(58,1)':
        #output_log_file(logfile,str(z)+" now has these edges: out "+str(z.outedgesList)+" and in "+str(z.inedgesList))


    for k in (0,1): # add edges of delta_5[k] to delta_n
        for v in delta_5[k].vertices:
            if verbose[9]>2:
                output_log_file(logfile,"k is "+str(k)+" delta 5 v is "+str(v)+" out edges "+str(v.outedgesList)+" in edges "+str(v.inedgesList))
            for x in delta_n.vertices:#find the vertex of delta_n corresponding to v
                if x.label==v.label:
                    v_new=x
                    if verbose[9]>2:
                        output_log_file(logfile," delta 5 v is "+str(v)+"deltan x=v_new is "+str(x))
                    break
            
            for (label,w) in v.outedgesList:
                for x in delta_n.vertices:
                    if x.label==w.label:
                        w_new=x
                        if verbose[9]>2:
                            output_log_file(logfile," v_new is "+str(v_new)+" D5 edge is "+str((label,w))+" w_new is "+str(w_new))
                        break
                delta_n.addEdge(v_new,w_new,label)
                if verbose[9]>2:
                    output_log_file(logfile,"v_new is "+str(v_new)+" D5 edge is "+str((label,w))+" w_new is "+str(w_new)+" adding edge v_new >> w_new with label "+str(label))

            for (label,w) in v.inedgesList:
                for x in delta_n.vertices:
                    if x.label==w.label:
                        w_new=x
                        break
                delta_n.addEdge(w_new,v_new,label)



    for v in delta_z.vertices:# add edges of delta_z to delta_n
        v_label='({0},{1})'.format(v.label,3)# set v_label to the label of v in the format of delta_n
        for x in delta_n.vertices:#find the vertex of delta_n corresponding to v
            if x.label==v_label:
                v_new=x
                break
        
        for (label,w) in v.outedgesList:
            w_label='({0},{1})'.format(w.label,3)# set w_label to the label of w in the format of delta_n
            for x in delta_n.vertices:#find the vertex of delta_n corresponding to w
                if x.label==w_label:
                    w_new=x
                    break
            delta_n.addEdge(v_new,w_new,label)#add an edge to delta_n
        for (label,w) in v.inedgesList:
            w_label='({0},{1})'.format(w.label,3)# set w_label to the label of w in the format of delta_n
            for x in delta_n.vertices:#find the vertex of delta_n corresponding to w
                if x.label==w_label:
                    w_new=x
                    break
            delta_n.addEdge(w_new,v_new,label)#add an edge to delta_n


    vertex_merge_list={}# a dictionary  of vertices that have become redundant and will be merged at the end of reassembly
    for v in [w for w in delta_n.vertices if len(w.nu_im)>0]:
        if verbose[9]>2:
            output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": found nu-im >0; v is "+str(v)+" nu_im is "+str(v.nu_im))
        for u in [w for w in delta_n.vertices[delta_n.vertices.index(v)+1:] if len(w.nu_im)>0]:
            if verbose[9]>2:
                 output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": v is "+str(u))
            if len(v.nu_im.intersection(u.nu_im))>0:#u is added to the list of vertices to be merged with v
                if v in vertex_merge_list:
                    vertex_merge_list[v].append(u)#
                else:
                    vertex_merge_list[v]=[u]
                if verbose[9]>1:
                    output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": something to do:  v is "+str(v)+" u is "+str(u)+" nu-im int is "+str(v.nu_im.intersection(u.nu_im)))
                    output_log_file(logfile,"   v edges "+str(v.outedgesList)+str(v.inedgesList)+" u edges "+str(u.outedgesList)+str(u.inedgesList))
                v.nu_im=v.nu_im.union(u.nu_im)
                #print("union ",  v.nu_im)
                u.nu_im=set()#make this empty so that u will not be considered again (is this necessary with u on vertex_delete_list?)


    if verbose[9]>1:
        output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": vertex_merge_list is "+str(vertex_merge_list))
                
    #end of find merges loop        
    ###########


    for v in vertex_merge_list:
        for u in vertex_merge_list[v]:
            delta_n.mergeVertices(v,u)
            if verbose[9]>1:
                output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": u= "+str(u.label)+" merged with "+str(v)+" and u deleted")
                output_log_file(logfile,"   v edges now in "+str(v.outedgesList)+" and out "+str(v.inedgesList))

    for v in delta_n.vertices:#test routine only - remove once pgm is working correctly
        if len(v.inedgesList)+len(v.outedgesList)==0: # 
            if verbose[9]>1:
                output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": after merge before fold, v= "+str(v)+" no edges")
    go = True
    while go: #fold delta_n, updating v.nu_im in the process
        go = delta_n.fold()

    i=1 # reformat vertices of delta_n
    for v in delta_n.vertices:
        if len(v.inedgesList)+len(v.outedgesList)==0: # 
            if verbose[9]>1:
                output_log_file(logfile,"Reassemble, iteration "+str(loop_count)+": v= "+str(v)+" i "+str(i)+" no edges")

        v.original=None 
        v.nu_im=set()
        v.name=i 
        v.label=v.name
        i+=1

    #print("dels ", vertex_merge_list)
    #print("count ", count)
    #print("delta_n root", delta_n.root)
    return(delta_n)


#######################################################
#function to make a distinct copy of graph G, ignoring edges with label in L.
#If a vertex has an edge with label in L it is marked as a boundary=1
#otherwise it has boundary =0
########################################################
def CopyGraph(G,L):

	Clabel=G.label# the label of the copy C is the label of G
	C=Graph(rooted=False,label=Clabel,Olabel=0) #creat copy
	for v in G.vertices:#create vertices of the copy
		vname=v.name
		vlabel=v.label
		if G.root==v:
			C.root=C.addVertex(vname)#if v is the root of G make it root of the copy
			Cv=C.root 
		else:
			Cv=C.addVertex(vname)#and in both cases add a vertex

		Cv.label=vlabel
		Cv.boundary=0#initialise the boundary, which will be set to 1 later if necessary

	for v in G.vertices:#now add edges 
		found=0
		for u in C.vertices: #find the vertex of C corresponding to v in G
			if v.label==u.label:
				Cv=u
				found=1
				break

		if found==0:
			error_message="Exiting from CopyGraph: a vertex of original was not recreated in the copy. Original vertex "+str(v)
			sys.exit(error_message)
			
		#now v is equal to Cv and an edge is added at Cv for each edge at v (unless the label is in L)
		for (label,s) in  v.outedgesList:
			if label in L:
				Cv.boundary = 1
			else:
				o=v.outedges_write[(label,s)]
				found=0
				for u in C.vertices:
					if s.name==u.name:
						C.addEdge(Cv,u,label,o) #add a labelled edge
						found=1
						break
				if found==0:
					error_message="Exiting from CopyGraph: a edge of original was not recreated in the copy. Original vertex "+str(v)+" original edge "+str((label,s))
					sys.exit(error_message)

		for (label,s) in  v.inedgesList:# in edges with label in L also make the bounary of Cv =1 
			if label in L:
				Cv.boundary = 1
				

	return(C)
