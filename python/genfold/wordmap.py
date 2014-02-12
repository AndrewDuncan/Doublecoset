from main_loop import *

# #################################
# function to:
# make inverses of generators x1, ...
def invert(g):
    G=g[0].upper()+g[1::]
    return(G)

# #################################
# function to:
# expand words input using pairs

def expand_word(w):
    ex_w=[]
    for x in w:
        if int(x[1])>0:
            for i in range(0,int(x[1])):
                ex_w.append(x[0])
        else:
            G=invert(x[0])
            for i in range(x[1],0):
                ex_w.append(G)

    return(ex_w)
# #################################
# function to:
# make image words a^-i b a^i, for i = 0 to n-1
def make_im(n):
    Im=[]
    Im_inv=[]
    for i in range(0,n):
        Im.append(['b'])
        for k in range(0,i):
            Im[i].append('a')
            Im[i].insert(0,'A')

        Im_inv.append(copy.deepcopy(Im[i]))
        Im_inv[i][i]='B'
        
    return(Im,Im_inv)

# ###############################
# function to:
# take a word in F(x1,...) and map it to a word in F(a,b) by
# mapping generator xi to a^{-i+1} b a^{i-1}, for i=1,... ,n
def morph(F,w,images,IMAGES):
    W=[]
    for x in w:
        i=F.gens.index(x.lower())
        if x==x.lower():
            W.extend(images[i])
        else:
            W.extend(IMAGES[i])
            
    W=element(W).word
    
    return(W)

# ###############################
# function to:
# take a word in F(a,b) and map it to a word in  F(x1,...) by
# mapping generator a to x1 and  b to x2.
#This assumes the word w is written in a, A, b, B, and if not, every letter which is not in this set is 
#treated as though it were B
def AtoX(F,w):
    W=[]
    for x in w:
        if x=='a':
            W.append('x'+str(1))
        elif x=='A':
            W.append('X1')
        elif x=='b':
            W.append('x2')
        else:
            W.append('X2')
            
    W=element(W).word
    
    return(W)

# ###############################
# function to:
# #write a word in latex format 
def word_to_tex(w):
    S=''
    if w==[]:
        S='1'
    else:
        current=w[0]
        power=1
        for x in range(1,len(w)):
            if w[x]==current:
                power=power+1
            else:
                if current==current.lower():
                    if power==1:
                        S=S+current
                    else:
                        S=S+current+'^{'+str(power)+'}'
                else:
                    S=S+current.lower()+'^{-'+str(power)+'}'
                current=w[x]
                power=1
    if current==current.lower():
        if power==1:
            S=S+current
        else:
            S=S+current+'^{'+str(power)+'}'
    else:
        S=S+current.lower()+'^{-'+str(power)+'}'
                

    return(S)
##########################################################################
#a function which takes a word in $F(x1,...)*F(y1,...) and makes a list
# of its factors from F1 and another of its factors from F2
def word_factors(F1,F2,w):
    factors1=[]
    factors2=[]
    if len(w)==0:
        return(factors1,factors2)
    if w[0] in F1.mongens:
        
        factor_switch=0
    else:
        factor_switch=1
    current=[]
    for l in w:
        if l in F1.mongens:
            if factor_switch==0:
                current.append(l)
            else:
                factors2.append(current)
                current=[l]
                factor_switch=0
        else:
            if factor_switch==1:
                current.append(l)
            else:
                factors1.append(current)
                current=[l]
                factor_switch=1
    if factor_switch==0:
        factors1.append(current)
    else:
        factors2.append(current)
        
    return(factors1,factors2)
#############################################################
#a function which takes a list of  words in $F(x1,...)*F(y1,...) and makes a list
# of their factors from F1 and another of  factors from F2
def list_factors(F1,F2,L):
    factors1=[]
    factors2=[]
    for w in L:
        [facs1,facs2]=word_factors(F1,F1,w)
        for w in facs1:
            if w not in factors1:
                factors1.append(w)
        for w in facs2:
            if w not in factors2:
                factors2.append(w)
    return(factors1,factors2)
#################################
###########################################################################
# #here begins wordmap main function
##########################################################################
def map_to_two_gens(Grank,List_rels,outfile):        
    #define the free group F on Grank generators x1, ...
    F=free_group(Grank,"x")
    
    # ###############################################################
    #
    # expand the relators into the usual word format
    Grels=[]
    for r in List_rels:
        R=expand_word(r)
        Grels.append(R)
    
    # ###############################################################
    # make all relators reduced 
    # and 
    # test that all elements of Grels are in F
    for r in Grels:
        r=element(r).word
        words_in_F=generators_in_free_group(F,Grels)# this will be 0 if all elements of Grels are in F, and 1 otherwise
        if words_in_F!=0: #if some of Grels are not in F: halt with an error message
            error_message="the list of relators entered must only contain elements of the free group of rank "+str(Grank)
            sys.exit(error_message)

            
    # ###################
    (images,IMAGES)=make_im(Grank)
    
    im_Grels=[]
    for r in Grels:
        R=morph(F,r,images,IMAGES)
        im_Grels.append(R)

    Trels=[]
    for R in im_Grels:
        S=word_to_tex(R)
        Trels.append(S)
        #open output file
        with open(outfile, "a") as out: #in append mode
            out.write(str(R)+"\n\n") #and  write unformatted relators to it

    for S in Trels:
        with open(outfile, "a") as out: #in append mode
            out.write("$"+str(S)+"$"+"\n%\n") #and  write formatted relators to it

    Xrels=[]
    for r in im_Grels:
        xr=AtoX(F,r)
        Xrels.append(xr)

    
    k=1
    for w in Xrels:
        with open(outfile, "a") as out: #in append mode
            out.write(str(w)+"\n\n") #and  write unformatted relators in generators x_1, x_2, to it

    return(im_Grels,Trels,Xrels)


