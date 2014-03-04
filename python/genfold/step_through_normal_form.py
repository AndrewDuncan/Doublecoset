from ball import *
import pickle 
import time 
localtime = time.asctime(time.localtime(time.time()))
#this program generates a ball of a given radius in generators previously stored for a subgroup of a (previously stored) amalgam

#So that each run creates a new set of files: set the prefix for the name of all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
#prefix
prefix='cex/'
#testfile='input_K/ball/'
testfile=prefix+'nf_steps/'
##############
# function to find whether a letter is in F1, F2 or FZ 
def test_letter(l,F1,F2,FZ):
    
    F=(F1,F2,FZ)
    if F[0].is_element(l)==1:
        f=0
    elif F[1].is_element(l)==1:
        f=1
    elif F[2].is_element(l)==1:
        f=2
    else:
        error_message="step_through_normal_form.py, amalgam_normal_form, "+str(l)+" not in free group on "+str(F[0].alpha)+" or "+str(F[1].alpha)+" or "+str(F[2].alpha)
        sys.exit(error_message)
    
    return(f)
##############
# function to take a word in F1*F2*FZ and rewrite it in F1*F2
def remove_Z(w,F1,F2,FZ,H1,H2):
    if w==[]:
        print('w is the empty word')
        return([])
    F=(F1,F2)
    H=(H1,H2)
    n=len(w)-1  
    started=0
    LZ=[]
    LX=[]
    while started==0:
        if len(w)>0:
            l=w.pop()
            f=test_letter([l],F1,F2,FZ)
            if f==2:
                LZ.insert(0,l)
                print("adding ", l," to LZ and getting LZ = ",LZ)
            else:
                started=1
                k=f
                print("started ",started,k,l,w)
        else:
            print("w is 1 ",w," l is ", l)
            LX=phi(H1,LZ)
            if LX[1]!=1:# LX=(u,i) where u is the translated word and i is an error flag
                sys.exit("something bad happened in remove_Z while calling phi, given a word with only z letters: w is now "+str(w)+" LZ "+str(LZ))
            print("returning a word in H1, no x, or y ", LX)
            return(LX[0])
    
    
    LX=phi(H[k],LZ)
    if LX[1]!=1:# LX=(u,i) where u is the translated word and i is an error flag
        sys.exit("something bad happened in remove_Z while calling phi, given a word not all in Zs. w is now  "+str(w)+" l is "+str(l)+" LZ is "+str(LZ))
    LX=LX[0]
    LX.insert(0,l)
    print("out of start routine and LX is ",LX)
    
    while len(w)>0:
        syl=[]
        l=w.pop()
        f=test_letter([l],F1,F2,FZ)
        if f==2:
            syl=phi(H[k],[l])
            if syl[1]!=1:# LX=(u,i) where u is the translated word and i is an error flag
                sys.exit("something bad happened in remove_Z while calling phi, in post start loop. w is now  "+str(w)+" syl is "+str(syl)+" LX is "+str(LX))
            syl=syl[0]
        else:
            syl=[l]
            if f!=k:
                k=f
        
        LX=syl+LX

    return(LX)#note that LX is not necessarily reduced
##############
# function to put a word w in double coset normal form in the amalgam of F_1*F_2, with H1=H2
# (main process starts below this function definition)
def amalgam_normal_form_with_steps(w,F1,F2,H1,H2,verbose,logfile):
    if w==[]:
        print('w is the empty word')
        return([])
    F=(F1,F2)
    n=len(w)-1
    if F[0].is_element(w[n])==1:
        f=0
    elif F[1].is_element(w[n])==1:
        f=1
    else:
        error_message="step_through_normal_form.py, amalgam_normal_form, "+str(w[n])+" not in free group on "+str(F[0].alpha)+" or "+str(F[1].alpha)
        sys.exit(error_message)
    ff=f
    for s in range(n-1,-1,-1):# 
        f=1-f
        if F[f].is_element(w[s])==0:
            error_message="step_through_normal_form.py, amalgam_normal_form, "+str(w[s])+" not in free group F "+str(f)
            sys.exit(error_message)

    
    H=(H1,H2)
    (flower1,double1)=(H1.flower,H1.double)
    (flower2,double2)=(H2.flower,H2.double)
    G=((flower1,double1),(flower2,double2))
    #
    f=ff# reset f as it was before the test that the word is in free product normal form
    #
    step=2
    v=['']*len(w) # initialise a list which will eventually contain the normal form
    for s in range(n,-1,-1):
        t=hf_test(w[s],H[f])# test to see if w[s] is in H[f] or not
        if t[0]==1: #if w[s] is in H[f]
            if len(w)==1:# if w is a single syllable then output the free group normal form of w
                if verbose[-1]>0:
                    output_log_file(logfile,"Step"+str(step)+". Free group normal form of  last and only syllable is ("+ str(w[s])+",,)")
                    output_log_file(logfile,"       Double coset normal form of w is "+str([t[1],[],[]])+"\n\n")
                #step+=1
                #print("t", t)
                v[0]=[t[1],[],[]] # the second argument of hf_test(w[s],H[f]) is the word w[s] written in F(Z) (+ 2 trivial words)
            else:# if w has more than one syllable then amalgamate with neighbouring syllables 
                if verbose[-1]>0:
                    output_log_file(logfile,"Step"+str(step)+". Syllable "+str(s)+" = "+str(w[s])+" is in H["+str(f)+"].")
                    output_log_file(logfile,"       Swap this syllable to H["+str(1-f)+"] and amalgamate with syllables either side.")
                w[s]=phi(H[1-f],t[1])[0] #swap w[s] from H[f] to H[1-f]
                if verbose[-1]>0:
                     output_log_file(logfile,"       Syllable "+str(s)+" = "+str(t[1])+" becomes "+str(w[s]))
                if s==0:#  if s is pointing at the first syllable and this is in H[f]
                    w[s]=w[s]+w[s+1] # replace w[0] with w[0]+w[1]
                    w[s]=element(w[s]).word
                    v[s+1].insert(0,t[1])# as s points at the first syllable, the left hand part is non-trivial
                    v[s]=v[s+1]
                    if verbose[-1]>0:
                        output_log_file(logfile,"       and amalgamating with syllable "+str(s+1)+" gives "+str(w[s]))
                        output_log_file(logfile,"       with normal form "+str(v[s])+".")
                    for i in range(s+2,len(w)):# move all syllables, from w[2] onwards, one place left, and do the same for v
                        w[i-1]=w[i]
                        v[i-1]=v[i]
                    w.pop(len(w)-1)#remove the last syllable of w 
                    v.pop(len(w)-1)#remove the last syllable of v
                    if verbose[-1]>0:
                        output_log_file(logfile,"       Moving all other syllables one place left gives w = "+str(w))
                        output_log_file(logfile,"       and final dc normal = "+str(v)+"\n\n")
                elif s==len(w)-1:# if s is pointing at the last syllable, and this is in H[f]
                    w[s-1]=w[s-1]+w[s]# replace w[s-1] with w[s-1]+w[s]
                    w[s-1]=element(w[s-1]).word
                    if verbose[-1]>0:
                        output_log_file(logfile,"       and amalgamating with syllable "+str(s-1)+" gives "+str(w[s-1]))
                    w.pop(s)#remove the last syllable of w
                    v.pop(s)# and of v
                    if verbose[-1]>0:
                        output_log_file(logfile,"       w is now "+str(w))
                        output_log_file(logfile,"       and output dc normal is unchanged at this step.\n\n")
                        #output_log_file(logfile,"       and the dc normal form so far is "+str(v))
                else: # the general case: s is pointing at a syllable which is in H[f], but not the 1st or last syll
                    w[s-1]=w[s-1]+w[s]+w[s+1]# replace w[s-1] with w[s-1]+w[s]+w[s+1]
                    w[s-1]=element(w[s-1]).word
                    if verbose[-1]>0:
                        output_log_file(logfile,"       and amalgamating with syllables "+str(s-1)+" and "+str(s+1)+" gives "+str(w[s-1]))
                    for i in range(s+2,len(w)): # move all syllables, from w[s+2] onwards, 2 places left, and do the same for v
                        w[i-2]=w[i]
                        v[i-2]=v[i]
                    w.pop(len(w)-1)# remove the last 2 syllables of w and v (pop twice)
                    v.pop(len(w)-1)
                    w.pop(len(w)-1)
                    v.pop(len(w)-1)
                    if verbose[-1]>0:
                        output_log_file(logfile,"       Moving all syllables of w to the right of s+1 two places left gives w = "+str(w))
                        output_log_file(logfile,"       and output dc normal is unchanged at this step.\n\n")
        else:   #if w[s] is not in H[f] 
            (left,Drep, right,left_Z,right_Z)=Normal_form(G[f][0],w[s],G[f][1]).spit_out_nf()#get the normal form of w[s]
            if s>0:# if w[s] is not the first syllable of w 
                v[s]=[Drep,right_Z]#syllable s of the normal form is (dc-repr, transversal element)
                swap=phi(H[1-f],left_Z)[0] #swap left hand part of w[s] from H[f] to H[1-f]
                if verbose[-1]>0:
                    fgnf=(left,Drep,right)
                    output_log_file(logfile,"Step"+str(step)+". Free group normal form of syllable "+str(s)+", "+ str(w[s])+" is "+str(fgnf))
                    output_log_file(logfile,"       add "+str(v[s])+" to left of output dc normal form")
                w[s-1]=element(w[s-1]+swap).word #right multiply w[s-1] by swap
                if verbose[-1]>0:
                    output_log_file(logfile,"       swap left part of nf to other factor: "+str(left)+" = "+str(left_Z)+" to "+str(swap))
                    output_log_file(logfile,"       and add to rhs of previous syllable of w to make syllable "+str(s-1)+" = "+str(w[s-1]))
                w[s]=element(Drep+right).word# left multiply w[s] by the inverse of it's left part
                if verbose[-1]>0:
                    output_log_file(logfile,"       syllable "+str(s)+" becomes "+str(w[s]))
                    output_log_file(logfile,"       so w becomes "+str(w))
                    output_log_file(logfile,"       and output dc normal form so far is  "+str(v)+"\n\n")
            else:
                v[s]=[left_Z,Drep,right_Z] #when s points at the 1st syllable the left hand part of w[s] becomes part of the normal form
                if verbose[-1]>0:
                    fgnf=(left,Drep,right)
                    output_log_file(logfile,"Step"+str(step)+". Free group normal form of syllable "+str(s)+", "+ str(w[s])+" is "+str(fgnf))
                    output_log_file(logfile,"       add "+str(v[s])+" to left of output dc normal form")
                    output_log_file(logfile,"       and final dc normal is  "+str(v)+".\n\n")

        f=1-f # swap from group 1 to 2 or vice-versa
        step+=1

    # output (w,v) consists of w, rewritten as a word in reduced form, by first writing w in dc normal form in the amalgam, 
    # and then rewriting each 
    # syllable of the result as a word in F1 or F2: 
    # and of v which has format [v0,....,vn], where v0 is a list of lth 3 and vi is a list of length 2 for i>0, 
    # v0 =[a,d,t], where a is in F(Z), d is a double coset rep and t is the right transversal Td,
    # and for i>0
    # vi =[d,t], with d and t as in the case i=0.
    return(w,v)
#######
#############################################################
# here the main process begins
#####################
#open the log file and write an initial line 
logfile=testfile+'xy3_log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file step_through_normal_form.py: "+str(localtime)+"\n\n") #and write text to it
#set last entry of verbose to something > 0 to generate a log file listing words in the ball of radius R (could be a large file!)

#as in K_fix.py
#10th entry of verbose > 0 --- save ball in file for later use
#last entry of verbose > 1 --- output log file with dc normal forms saved
#                             1,1,1  
##########0,1,2,3,4,5,6,7,8,9,0,1,2
verbose =[0,0,0,0,1,1,1,1,1,1,1,0,1]
#verbose =[0,0,0,0,0,0,0,0,1,0,0,0]


#file to store results
outputfile=prefix+'nf_steps_yx3.txt'
#outputfile=testfile+'ball.txt'
with open(outputfile, "w") as out:#initialise outputile
    out.write("step_through_normal_form.py output file: "+str(localtime)+"\n\n") 


#directory of files in which inputs are stored
#
inputfile=prefix
getfile=inputfile+'input_save.txt'  
Hrank,Hname1,Hname2,Hgens1,Hgens2,F1,F2,words1,words2,Kname,Kgens= pickle.load( open(getfile, "rb" ) ) 
getfile=inputfile+'H1_save.txt'  
H1 = pickle.load( open(getfile, "rb" ) ) 
getfile=inputfile+'H2_save.txt'  
H2 = pickle.load( open(getfile, "rb" ) ) 
getfile=inputfile+'FZ_save.txt'  
FZ = pickle.load( open(getfile, "rb" ) )
getfile=inputfile+'K_save.txt'  
K = pickle.load( open(getfile, "rb" ) )
# 

#L=[['y1','y1'], ['x3','X2'],['x1','z1']]
#L1=[['a'],['b'],['c']]
#L2=[['y1','y1'], ['Y1','y2'],['Y2','Y1']]
#Kgrs=K.subgp_gens # not used at present - the generators for K in normal form 


#input the words to test
#words should be expressed as products of the generators of K: so should be readable by the folding of K
#such words can be found in prefix/ball/ball.txt
#
#v=[['z1', 'z2', 'Z3', 'y2', 'x2'],['z1', 'z2', 'Z3', 'y2', 'x2'],['z4'],['Z4', 'Z2', 'z3', 'X2', 'Y2'],['Z4', 'Z2', 'z3', 'X2', 'Y2']]
#v=['z1', 'z2', 'Z3', 'y2', 'x2','z1', 'z2', 'Z3', 'y2', 'x2', 'Z2', 'z3', 'X2', 'Y2','Z4', 'Z2', 'z3', 'X2', 'Y2']
#v=['z1', 'z2', 'Z3', 'y2', 'x2','z1', 'z2', 'Z3', 'y2', 'x2', 'Z2', 'z3', 'X2', 'Y2','Z4', 'Z2', 'z3', 'X2', 'Y2','y1','x1']
#v=['Z3', 'y2','y2', 'x2','x1','Z1','y1','x1','X2','z1', 'Z3']
#v=['Z2','z1']
#v=[]
#v=['X2','y1','x1','X2','Y2','Z4']
#v=['y1','x1','y1','x1','y1','x1']
v=['z1', 'z2', 'Z3', 'y2', 'x2','z1', 'z2', 'Z3', 'y2', 'x2','z1', 'z2', 'Z3', 'y2', 'x2']
#first rewrite v as a word in generators of F1 and F2
if verbose[-1]>0:
    output_log_file(logfile,"Input word is "+str(v)+"\n\n")

LX=remove_Z(v,F1,F2,FZ,H1,H2)

#if verbose[-1]>0:
#    output_log_file(logfile,"Step 1. Replace Z letters by X1 or X2 letters:\n v= "+str(LX)+"\n\n")

w=listsplitter(LX,F1.mongens,F2.mongens)
if verbose[-1]>0:
    output_log_file(logfile,"Step 1. Replace Z letters by X1 or X2 letters to give w:\n        "+str(w)+"\n\n")
    w=amalgam_normal_form_with_steps(w,F1,F2,H1,H2,verbose,logfile)
    if verbose[-1]>0:
        output_log_file(logfile,"To confirm: after amalgam_normal_form_with_steps w = "+ str(w[0])+"\n wv = "+str(w[1])+"\n")
    w=w[1]
#root=delta_n.root
if verbose[-1]>5:
    i=0
    with open(outputfile, "a") as out: #write to outputfile 
        for b in B:
            j=0
            out.write("list B: "+str(i)+"\n") 
            for w in b:
                out.write(" j "+str(j)+": "+str(w)+"\n")
                j+=1
            i+=1
    i=0
    with open(outputfile, "a") as out: #append to outputfile 
        out.write("\n\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n\n")
        for b in B_nf:
            j=0
            out.write("list B_nf: "+str(i)+"\n") 
            for w in b:
                out.write(" j "+str(j)+": "+str(w)+"\n") 
                j+=1
            i+=1
  
### at the end close files
log.close()
out.close()
