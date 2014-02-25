from main_loop import *
#import pickle 
###########################################################################
# #here begins ball main function, which constructs the ball of radius R
# #on the list L of words input ... it should be made to check these words are in F1*F2
##########################################################################
def ball(R,L,F1,F2,Hrank,H1,H2,logfile,verbose):        
    #make a list S of elements of L and their inverses
    S=[]
    for l in L:
        S.append(l)
    for l in L:
        linv=element(l).inverse()
        S.append(linv)
    
    #print("in ball S", S)
    #for each element s of S:  make a list of elements of S not equal to s^{-1} and add it to T 
    T=[]
    for s in S:
        s_list=[]
        for t in S:
            if s!=element(t).inverse():
                s_list.append(t)
        
        T.append(s_list)

    B=[]# B will be the list of spheres of radius 1 to R, of (possibly) undreduced words
    sphere=[]#make the sphere of length 1 words
    for s in S:
        sphere.append([s])
    
    B.append(sphere)#the first entry of B is the sphere of length one words (usually the generators of K and their inverses)
    #construct successive spheres and append them to B
    #print("in ball sphere 1 ",B[0])
    for r in range(1,R):#construct the sphere of radius r+1 (up to r=R-1)
        print("creating sphere of radius ", str(r+1))
        sphere=[]
        for w in B[-1]:#for each element w of the sphere of radius r
            w_last=w[-1]#find the element l of S with wich w ends
            ind=S.index(w_last) # find the position ind of l in S
            multipliers=T[ind]# find the list of elements not begining l^{-1}
            for m in multipliers:# add m to w on the right, for each such and add the result to the sphere  
                w_new=w+[m]
                sphere.append(w_new)
        B.append(sphere) #add the sphere of radius r to B
        #print("in ball sphere r+1 ",B[r])
    
    #make normal forms of the elements constructed
   
    B_nf=[]# the normal forms of elements of B
    for b in B:# for each sphere b
        C=[]
        for w in b: #for each word in b 
            wrd=[]#make the word into a word in the generators F1*F2
            for l in w:
                wrd=wrd+l
            
            wrd=element(wrd).word# freely reduce 
            #print("wrd ", wrd,"\n")
            nf_wrd=[]
            if len(wrd)>0:#find the dc normal form of wrd
                if verbose[-1]>0:
                    output_log_file(logfile,"ball.py: wrd is "+ str(wrd))
                #print("wrd ",wrd)
                lw=listsplitter(wrd,F1.mongens,F2.mongens)
                if verbose[-1]>0:
                    output_log_file(logfile,"ball.py: wrd is changed to lw by listsplitter: "+ str(lw))
                #print("lw ", lw)
                nw=amalgam_normal_form(lw,F1,F2,H1,H2)
                #print("nw ",nw)
                if verbose[-1]>0:
                    output_log_file(logfile,"ball.py: lw is changed to nw by amalgam_normal_form: "+ str(nw))              
                for s in nw[1]:
                    if verbose[-1]>0:
                        output_log_file(logfile,"ball.py: nw[1] item s is "+ str(s)) 
                        #print("s is ", s)
                    for q in s:
                        if verbose[-1]>0:
                            #print("q is ", q)
                            output_log_file(logfile,"ball.py: s item q is "+ str(q))
                        if q!=[]:
                            nf_wrd=nf_wrd+q
            C.append(nf_wrd)
            #print("nf_wrd ",nf_wrd,"\n")

        #print("C = ", C)
        B_nf.append(C)
    

    #save B_nf to outputfile
    #pickle.dump(B_nf, open(outputfile, "wb" ) )

    return(S,T,B,B_nf)


