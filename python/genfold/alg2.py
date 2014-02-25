from adjust_generators import *

####
# a function which takes a word w in generators f1gens and f2gens and splits it
# into syllables of the free product <f1gens>*<f2gens>
def listsplitter(w,f1gens,f2gens):
    w=element(w).word #freely reduce w
    l=len(w)
    ww=[] #ww is the "list of lists"
    ww.append([w[0]])
    if w[0] in f1gens:
        j=1
    else:
        j=2
    for c in range(1,l):
        if j==1:
                if w[c] in f1gens:
                    ww[-1]=ww[-1]+[w[c]]
                else:
                    j=2
                    ww.append([w[c]])
        else:
                if w[c] in f2gens:
                    ww[-1]=ww[-1]+[w[c]]
                else:
                    j=1
                    ww.append([w[c]])
    #print (ww)
    for c in range(1,l):
        if w[c]==[]:
            w.remove(w[c])
    #print(ww)
    return(ww)

##############################
# a function which takes a list of words and freely reduces each element
def reducelist(w):
    for c in w: #freely reducing each fi in w
        c=element(c).word
    return(w)

#########################################################
# a function which tests that a word belongs to the 
# monoid generated by f1gens, f2gens 
def listtest(w,f1gens,f2gens):
    i=1
    genset=f1gens+f2gens
    #print(genset)
    for c in w:
        if c not in genset:
            #print(c,' isn\'t an element of either free group')
            error_message="alg2.py, listtest, "+str(c)+" isn\'t an element of either free group"
            sys.exit(error_message)
            i=0
#   if i==0:
#       print(w,' isn\'t a word in the free (amalgamated) product')
    return(i)

#######################################################
# a function to take a list of triples, and make it into a list of words,
# by concatenating the 3rd item of the ith triple with the 1st item of the 
# i+1 st triple (not used anywhere at present)
def joiner(w):
    if w==[[[],[],[]]]:
        return []
    elif len(w)==1:
        ww=w[0][0]+w[0][1]+w[0][2]
        return ww
    ww=[w[0][0]]
    #print('ww=[w[0][0]]= ', ww)
    for i in range(0,len(w)-1):
        #print('i is ', i)
        ww.append(w[i][1])
        #print('after appending w[i][1], ww is ', ww)
        t = [w[i][2] + w[i+1][0]]
        #print('t is ', t)
        ww = ww + t
        #print('ww becomes', ww)
        #ww.append(t)
    ww.append(w[-1][1])
    ww.append(w[-1][2])
    #print('so now ww is\n',ww)
    w=[]
    for c in ww:
        w.extend(c)
    #print('and w becomes ',w)
    w=element(w).word
    #print('which reduces to',w)
    #print('joiner returns\n',w)
    return(w)

### obsolete?
def quickreduce(w): #reduces only the necessary elements in dcnf, not needed due to change to joiner function
        for i in range(0,len(w)):
            if w%2==0:
                w[i]=element(w[i]).word
        #print(w)
        return(w)



def nf_in_list(w,flower1,flower2,double1,double2,F1,F2):
    ww = []
    for c in w:
        #print("here  1, F1.is_element(c), F2.is_element(c)", F1.is_element(c), F2.is_element(c))
        if F1.is_element(c)!=0:
            #print("c is ",c, "in F1", F1.is_element(c))
            d = Normal_form(flower1,c,double1).spit_out_nf()
            #e = [d[3],d[1],d[4]]
            e = [d[0],d[1],d[2]]
            #print("here  2")
        elif F2.is_element(c)!=0:
            #print("c is ",c, "in F2",F2.is_element(c))
            d = Normal_form(flower2,c,double2).spit_out_nf()
            #e = [d[3],d[1],d[4]]
            e = [d[0],d[1],d[2]]
            #print("here  3")
        else:
            error_message="alg2.py, nf_in_list, "+str(c)+" isn\'t an element of either free group"
            sys.exit(error_message)
            print(c," isn't a word in either free group")
        #print("Syllable in normal form is ",e)
        ww.append(e)
        #print("here  4")
    return(ww)

def popper(w):
    return [e for e in w if e!=""]


##############
# function to put a word w in double coset normal form in the amalgam of F_1*F_2, with H1=H2
def amalgam_normal_form(w,F1,F2,H1,H2):
    if w==[]:
        print('w is the empty word')
        return([])
    F=(F1,F2)
    #error=0
    n=len(w)-1
    if F[0].is_element(w[n])==1:
        f=0
        #print('f is ',f)
    elif F[1].is_element(w[n])==1:
        f=1
        #print('f is ',f)
    else:
        error_message="alg2.py, amalgam_normal_form, "+str(w[n])+" not in free group on "+str(F[0].alpha)+" or "+str(F[1].alpha)
        sys.exit(error_message)
        #print('Error: ',w[n],'not in free group on', F[0].alpha, 'or', F[1].alpha)
        #return
    ff=f
    for s in range(n-1,-1,-1):# 
        f=1-f
        #print('s is',s,'f is',f)
        if F[f].is_element(w[s])==0:
            #print("Error: ",w[s],'is not in F',f)
            error_message="alg2.py, amalgam_normal_form, "+str(w[s])+" not in free group F "+str(f)
            sys.exit(error_message)
            #error=1
            #print('error becomes 1')
            #break
        
    #if error==1:
    #    return
    
    H=(H1,H2)
    (flower1,double1)=(H1.flower,H1.double)
    (flower2,double2)=(H2.flower,H2.double)
    G=((flower1,double1),(flower2,double2))
    #
    f=ff# reset f as it was before the test that the word is in free product normal form
    #
    v=['']*len(w) # initialise a list which will eventually contain the normal form
    #print("v, len(v), len(w)",v,len(v), len(w))
    for s in range(n,-1,-1):
        #print('Start of a_n_f loop. w is', w)  
        #print('s is',s)
        #print('w[s] is',w[s])
        #print("H[f] is ", H[f].name)
        t=hf_test(w[s],H[f])# test to see if w[s] is in H[f] or not
        if t[0]==1: #if w[s] is in H[f]
            #print("w[s] is in ", H[f].name)
            if len(w)==1:# if w is a single syllable then output the free group normal form of w
                #print(" and len(w)==1, here it is", len(w))
                v[0]=[t[1],[],[]] # the second argument of hf_test(w[s],H[f]) is the word w[s] written in F(Z) (+ 2 trivial words)
            else:# if w has more than one syllable then amalgamate with neighbouring syllables 
                w[s]=phi(H[1-f],t[1])[0] #swap w[s] from H[f] to H[1-f]
                if s==0:#  if s is pointing at the first syllable and this is in H[f]
                    w[s]=w[s]+w[s+1] # replace w[0] with w[0]+w[1]
                    w[s]=element(w[s]).word
                    #print("pre shuffle: a,len(w), len(v), w, v", len(w), len(v), w,v)
                    v[s+1].insert(0,t[1])# as s points at the first syllable, the left hand part is non-trivial
                    v[s]=v[s+1]
                    for i in range(s+2,len(w)):# move all syllables, from w[2] onwards, one place left, and do the same for v
                        w[i-1]=w[i]
                        v[i-1]=v[i]
                    #print("pre pop: a,len(w), len(v), w, v", len(w), len(v), w,v)
                    w.pop(len(w)-1)#remove the last syllable of w 
                    v.pop(len(w)-1)#remove the last syllable of v
                    #print("post pop: a,len(w), len(v), w, v", len(w), len(v), w,v)
                    #print("b, len(w)", len(w))
                elif s==len(w)-1:# if s is pointing at the last syllable, and this is in H[f]
                    w[s-1]=w[s-1]+w[s]# replace w[s-1] with w[s-1]+w[s]
                    w[s-1]=element(w[s-1]).word
                    #print("c, len(w)",len(w))
                    w.pop(s)#remove the last syllable of w
                    v.pop(s)# and of v
                    #print("d,len(w)", len(w))
                else: # the general case: s is pointing at a syllable which is in H[f], but not the 1st or last syll
                    w[s-1]=w[s-1]+w[s]+w[s+1]# replace w[s-1] with w[s-1]+w[s]+w[s+1]
                    w[s-1]=element(w[s-1]).word
                    for i in range(s+2,len(w)): # move all syllables, from w[s+2] onwards, 2 places left, and do the same for v
                        w[i-2]=w[i]
                        v[i-2]=v[i]
                        #print("len(w)", len(w)," and i,w[i-2], w[i]", i,w[i-2],w[i])
                    #print("e,len(w)", len(w))
                    w.pop(len(w)-1)# remove the last 2 syllables of w and v (pop twice)
                    v.pop(len(w)-1)
                    #print("f,len(w)", len(w))
                    w.pop(len(w)-1)
                    v.pop(len(w)-1)
                    #print("g,len(w)", len(w))
        else:   #if w[s] is not in H[f] 
            #print("G[f][0],w[s],G[f][1]",G[f][0],"\n\n",w[s],"\n\n",G[f][1])
            (left,Drep, right,left_Z,right_Z)=Normal_form(G[f][0],w[s],G[f][1]).spit_out_nf()#get the normal form of w[s]
            #print("in amal_n_f left,Drep, right,left_Z,right_Z is", left,Drep, right,left_Z,right_Z)
            if s>0:# if w[s] is not the first syllable of w 
                v[s]=[Drep,right_Z]#syllable s of the normal form is (dc-repr, transversal element)
                swap=phi(H[1-f],left_Z)[0] #swap left hand part of w[s] from H[f] to H[1-f]
                w[s-1]=element(w[s-1]+swap).word #right multiply w[s-1] by swap
                w[s]=element(Drep+right).word# left multiply w[s] by the inverse of it's left part
            else:
                v[s]=[left_Z,Drep,right_Z] #when s points at the 1st syllable the left hand part of w[s] becomes part of the normal form

        f=1-f # swap from group 1 to 2 or vice-versa

    # output (w,v) consists of w, rewritten as a word in reduced form, by first writing w in dc normal form in the amalgam, 
    # and then rewriting each 
    # syllable of the result as a word in F1 or F2: 
    # and of v which has format [v0,....,vn], where v0 is a list of lth 3 and vi is a list of length 2 for i>0, 
    # v0 =[a,d,t], where a is in F(Z), d is a double coset rep and t is the right transversal Td,
    # and for i>0
    # vi =[d,t], with d and t as in the case i=0.
    return(w,v)
#######

def hf_test(w,H):
    t=graph_pass(H.flower,w).acc_read_rem()
    #print("in hf_test t is ", t)
    #print("H name, gens, free_gens", H.name, H.subgp_gens, H.subgroup_free_gens, "and t[4] is ", t[4])
    if len(t[1])==0 and len(t[2])==0:# in this case w[s] is in H[f]
        j=1
    else:
        j=0
    #print("after hf_test j is",j)
    return(j,t[4])
