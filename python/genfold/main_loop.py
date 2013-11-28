from alg3 import *

def Main_Loop(Delta,F,FZ,H,verbose,logfile,testfile,max_iterations):

    loop_count=1
    changed=True
    while changed:
        changed=False
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
    
    
        print("now D4")
        (delta_4,Prod)=Mod4(delta_3,H,verbose,logfile)
    
        # Open D4_1.gv in write mode
        output_graph_file(delta_4[0],testfile+"D4_1_v"+str(loop_count)+".gv","D4_1",verbose,logfile)
    
        # Open D4_2.gv in write mode
        output_graph_file(delta_4[1],testfile+"D4_2_v"+str(loop_count)+".gv","D4_2",verbose,logfile)

        # Open P_3_1.gv in write mode
        output_graph_file(Prod[0],testfile+"P_3_1_v"+str(loop_count)+".gv","P31",verbose,logfile)
    
        # Open P_3_2.gv in write mode
        output_graph_file(Prod[1],testfile+"P_3_2_v"+str(loop_count)+".gv","P32",verbose,logfile)
    
    
    
        print("now D5")
        (delta_5,Prod)=Mod5(delta_4,H,verbose,logfile)
        
        # Open D5_1.gv in write mode
        output_graph_file(delta_5[0],testfile+"D5_1_v"+str(loop_count)+".gv","D5_1",verbose,logfile)
    
        # Open D5_2.gv in write mode
        output_graph_file(delta_5[1],testfile+"D5_2_v"+str(loop_count)+".gv","D5_2",verbose,logfile)
    
        # Open P_4_1.gv in write mode
        output_graph_file(Prod[0],testfile+"P_4_1_v"+str(loop_count)+".gv","P41",verbose,logfile)
    
        # Open P_4_2.gv in write mode
        output_graph_file(Prod[1],testfile+"P_4_2_v"+str(loop_count)+".gv","P42",verbose,logfile)
    
        ##############################################
        delta_n=Reassemble(delta_5,D0[2],H,verbose,logfile)
    
        # Open Dn.gv in write mode
        output_graph_file(delta_n,testfile+"Dn_v"+str(loop_count)+".gv","Delta_n",verbose,logfile)
        #output_graph_file(Delta,testfile+"Dorig_v"+str(loop_count)+".gv","Delta_orig",verbose,logfile)
        if Delta!=delta_n and loop_count<=max_iterations:
            changed=True
            loop_count+=1
            Delta=delta_n# delta_n is input to the next iteration

    return(delta_n,loop_count)
        
