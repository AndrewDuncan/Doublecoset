from main_loop import *

###########################################################################
# #here begins ball main function, which constructs the ball of radius R
# #on the list L of words input ... it should be made to check these words are in F1*F2
##########################################################################
def ball(R,L,F1,F2,Hrank,H1,H2,outfile):        
    #make a list of elements of L and their inverses
    S=[]
    for l in L:
        S.append(l)
    for l in L:
        linv=element(l).inverse()
        S.append(linv)
    
    #for each element s of S:  make a list S \ s^{-1} and add it to T 
    T=[]
    for s in S:
        s_list=[]
        for t in S:
            if s!=element(t).inverse():
                s_list.append(t)
        
        T.append(s_list)

    B=[]
    sphere=[]
    for s in S:
        sphere.append([s])
    
    B.append(sphere)
    #print("S is ", S)
    #print("B -1 is ", B[-1])
    for r in range(1,R):
        sphere=[]
        for w in B[-1]:
            w_last=w[-1]
            #print("r is ", r," w is ",w, " w_last ",w_last)
            ind=S.index(w_last)
            #print("ind of w_last ",ind)
            multipliers=T[ind]
            #print("multipliers ",multipliers)
            for m in multipliers:
                w_new=w+[m]
                sphere.append(w_new)
        B.append(sphere)
        #for b in B:
        #    for w in b:
        #        print("w  is ",w,"\n")

    for w in B[-1]:
        wrd=[]
        for l in w:
            wrd=wrd+l
            
        wrd=element(wrd).word
        print("wrd is ",wrd,"\n")
        if len(wrd)>0:
            lw=listsplitter(wrd,F1.mongens,F2.mongens)
            nw=amalgam_normal_form(lw,F1,F2,H1,H2)
            print("  ",nw[1],"\n")
    return(S,T,B)


