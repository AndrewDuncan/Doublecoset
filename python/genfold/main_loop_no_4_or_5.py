from alg3 import *
import pickle
###########################################
# a function to construct stallings foldins of H1 and H2
##########################################
def construct_H_foldings(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,verbose,logfile,change_tree):
    # construct the group FZ
    FZ=free_group(int(Hrank),"z")        
    #
    # find the folding corresponding to the generators entered
    #
    H1=construct_required_folding(Hname1,Hgens1,testfile,F1,Hrank,verbose,FZ,change_tree,logfile)
    
    # write the final folding as a graph
    filename=testfile+"stallings1.gv"
    output_graph_file(H1.flower,filename,"stallings1",verbose,logfile)
    # write the double of the folding as a graph
    filename=testfile+"double1.gv"
    output_graph_file(H1.double,filename,"double1",verbose,logfile)
    #    for e in v.out
    
    
    # find the folding corresponding to the generators entered
    #
    H2=construct_required_folding(Hname2,Hgens2,testfile,F2,Hrank,verbose,FZ,change_tree,logfile)
    
    # write the final folding as a graph
    filename=testfile+"stallings2.gv"
    output_graph_file(H2.flower,filename,"stallings2",verbose,logfile)
    # write the double of the folding as a graph
    filename=testfile+"double2.gv"
    output_graph_file(H2.double,filename,"double2",verbose,logfile)

    return(H1,H2,FZ)
# ###############################################################
# a function to construct the initial folding of the subgroup K
###############################################################
def construct_K(H1,H2,FZ,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile):
    # test that elements of words1 are in F1
    words_in_F=generators_in_free_group(F1,words1)# this will be 0 if all elements of words1 are in F1, and 1 otherwise
    if words_in_F!=0: #if some of words1 are not in F1: halt with an error message
        error_message="the first list of words entered must only contain elements of F1"
        sys.exit(error_message)
        # #########
        
    # test that elements of words2 are in F2
    words_in_F=generators_in_free_group(F2,words2)# this will be 0 if all elements of words2 are in F2, and 1 otherwise
    if words_in_F!=0: #if some of words2 are not in F2: halt with an error message
        error_message="the second list of words entered must only contain elements of F2"
        sys.exit(error_message)

    # add inverse of each generator to Kgens (the normal form of w^{-1} is not necessarily the free monoid inverse of the nf of w)
    L=[]
    for w in Kgens:
        inv=element(w).inverse()
        L.append(inv)

    Kgens=Kgens+L
    if verbose[-1]>1:
            output_log_file(logfile,"Main loop, construct_K, after adding inverses, Kgens is "+ str(Kgens))

    g=[]
    for w in Kgens:
        if verbose[-1]>1:
            output_log_file(logfile,"Main loop: construct_K, w in Kgens is "+ str(w)+" and its free product normal form  ")
            #print('\n\n\n',w,' becomes')
        w=listsplitter(w,F1.mongens,F2.mongens)
        if verbose[-1]>1:
            output_log_file(logfile,"output by alg2.py, listsplitter is "+ str(w))
            #print(w, "after listsplitter and then")
        w=amalgam_normal_form(w,F1,F2,H1,H2)
        if verbose[-1]>1:
            output_log_file(logfile,"and output of alg2.py, amalgam_normal_form is w = "+ str(w[0])+" wv "+str(w[1]))
            #print(" and after amalgam_normal_form w and wv are", w[0], "and ", w[1],'\n') 
        w=w[1]
        g.append(w)

    Kgens=g
    # extract the normal form version of these
    v=[]
    g=[]
    for q in Kgens:
        for r in q:
            for s in r:
                for t in s:
                    v.append(t)
        g.append(v)
        v=[]

    Kgens=g
    
    # form the subgroup K
    K=subgroup(Kname,Kgens)
    # make the Stallings folding of the gens of K
    K.stallings()
    # and a spanning tree
    bfs(K.flower,).forest()
    # output the folding to a file
    output_graph_file(K.flower,testfile+"Kfolding.gv","Kfold",verbose,logfile)

    return(K)
# ########################
# main loop
###########################
def main_loop(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile,change_tree,max_iterations):
#
    (H1,H2,FZ)=construct_H_foldings(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,verbose,logfile,change_tree)
    K=construct_K(H1,H2,FZ,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile)

    #save files for later use
    if verbose[10]>0:
        H1_save=testfile+'H1_save.txt'
        pickle.dump(H1, open(H1_save, "wb" ))
        H2_save=testfile+'H2_save.txt'
        pickle.dump(H2, open(H2_save, "wb" ))
        FZ_save=testfile+'FZ_save.txt'
        pickle.dump(FZ, open(FZ_save, "wb" ))
        K_save=testfile+'K_save.txt'
        pickle.dump(K, open(K_save, "wb" ))
    
    

    F=(F1,F2)
    H=(H1,H2)
    flower1=H1.flower
    flower2=H2.flower
    flower=(flower1,flower2)
    
  
    Delta=K.flower
    loop_count=1
    changed=True
    while changed:
        changed=False
        print("\n iteration number ", loop_count)
        print("now D0")
        D0=MakeComps(Delta,F,FZ,verbose,logfile) # returnsdelta_k0[0],delta_k0[1],delta_z
        
        # Open alg3_test_D0_1.gv in write mode
        output_graph_file(D0[0],testfile+"D0_1_v"+str(loop_count)+".gv","D0_1",verbose,logfile)
        
        # Open alg3_test_D0_2.gv in write mode
        output_graph_file(D0[1],testfile+"D0_2_v"+str(loop_count)+".gv","D0_2",verbose,logfile)
        
        # Open alg3_test_D0_Z.gv in write mode
        output_graph_file(D0[2],testfile+"D0_Z_v"+str(loop_count)+".gv","D0_Z",verbose,logfile)
        
        delta_0=[D0[0],D0[1]] # take the first two components of D0, that is the X1 and X2 components
        #
        print("now D1")
        #D1=Mod1(delta_0,FZ,H,flower)
        delta_1=Mod1(delta_0,FZ,H,verbose,logfile)
        
        # Open alg3_test_D1_1.gv in write mode
        output_graph_file(delta_1[0],testfile+"D1_1_v"+str(loop_count)+".gv","D1_1",verbose,logfile)
        
        # Open alg3_test_D1_2.gv in write mode
        output_graph_file(delta_1[1],testfile+"D1_2_v"+str(loop_count)+".gv","D1_2",verbose,logfile)
        
        print("now D2")
        (delta_2,Prod)=Mod2(delta_1,H,verbose,logfile)
        
        # Open alg3_test_P_1_1.gv in write mode
        output_graph_file(Prod[0],testfile+"P_1_1_v"+str(loop_count)+".gv","P11",verbose,logfile)
        
        # Open alg3_test_P_1_2.gv in write mode
        output_graph_file(Prod[1],testfile+"P_1_2_v"+str(loop_count)+".gv","P12",verbose,logfile)
        
        # Open alg3_test_D2_1.gv in write mode
        output_graph_file(delta_2[0],testfile+"D2_1_v"+str(loop_count)+".gv","D2_1",verbose,logfile)
        
        # Open alg3_test_D2_2.gv in write mode
        output_graph_file(delta_2[1],testfile+"D2_2_v"+str(loop_count)+".gv","D2_2",verbose,logfile)
        
        
        print("now D3")
        (delta_3,Prod)=Mod3(delta_2,H,verbose,logfile)
        
        # Open alg3_test_D3_1.gv in write mode
        output_graph_file(delta_3[0],testfile+"D3_1_v"+str(loop_count)+".gv","D3_1",verbose,logfile)
        
        # Open alg3_test_D3_2.gv in write mode
        output_graph_file(delta_3[1],testfile+"D3_2_v"+str(loop_count)+".gv","D3_2",verbose,logfile)
        
        # Open alg3_test_P_2_1.gv in write mode
        output_graph_file(Prod[0],testfile+"P_2_1_v"+str(loop_count)+".gv","P21",verbose,logfile)
        
        # Open alg3_test_P_2_2.gv in write mode
        output_graph_file(Prod[1],testfile+"P_2_2_v"+str(loop_count)+".gv","P22",verbose,logfile)
        
        

        
        

        
        ##############################################
        print("now Reassemble")
        delta_n=Reassemble(delta_3,D0[2],H,verbose,logfile,loop_count)
        
        # Open Dn.gv in write mode
        output_graph_file(delta_n,testfile+"Dn_v"+str(loop_count)+".gv","Delta_n",verbose,logfile)
        #output_graph_file(Delta,testfile+"Dorig_v"+str(loop_count)+".gv","Delta_orig",verbose,logfile)

        if str(Delta)!=str(delta_n) and loop_count<max_iterations:
            changed=True
            loop_count+=1
            Delta=delta_n# delta_n is input to the next iteration

    return(delta_n,loop_count)
        
