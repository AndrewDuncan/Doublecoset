from alg3 import *

#define verbose, test and log files for compatibility with K_fix
##########0,1,2,3,4,5,6,7,8,9,0
verbose =[0,0,0,0,0,0,0,0,0,0,2]
#
#may need to change the folding to get the gens we want
change_tree=1
#
logfile="K_words/log.txt"
with open(logfile, "w") as log: #create logfile 
    log.write("log file K_words_in_nf \n\n") #and write text to it
testfile="K_words/"
#define the free groups F1 and F2, by giving the number of generators, and letter for the generators
F1=free_group(3,"x")
F2=free_group(4,"y")#do not make both these letters the same

#Enter the rank of the subgroup
Hrank=3

####################
#### enter H1
################
#Choose the 1st subgroup name
Hname1='H1'

# Enter some elements of F1, a selection of which can be used to generate the subgroup H1
#h1=['X1','x3','x4','X2']
#h2=['x2','X1','x3','x4','x2']
#h3=['x2','x2','x2']
#h4=['X2','x1','x3','x2']
#
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
h5=['x1','x1','x1']
h6=['x2','x3','X2']
h7=['x1','x2','x3']
#make the generators into a list
Hgens1=[h5,h6,h7]#,h5]

################
### enter H2
##############
#Choose the 2nd subgroup name
Hname2='H2'

# Enter some elements of F2, a selection of which can be used to generate the subgroup H2
g1=['y2','y2']
g2=['y3','y4']
g3=['y1','y1','y3','Y1','y2']

#make the generators into a list
Hgens2=[g1,g2,g3]

#########################################################
#########  now enter K
######################
#enter name of subgroup K
Kname='K'

# Enter a free generating set for K - in stages, first enter words in the factor groups, then concatenate.
#First enter some words in F1
kf1=['x2','x3','x3','X2','x1','x1','x1','x1','x3','X1','X1','X3','X2','X1']
kf2=['X3','X2','X1','x2','X3','X2','X1']
kf3=['x2','X3','x1']
kf4=['x1','x1','x1','x1','x2','x3','X1','X2']
kf5=['x1','x2','x3','x2','X3','X3','X2']
kf6=['x2','x1']

#Make a list of these words
words1=[kf1,kf2,kf3,kf4,kf5,kf6]

#####################
#Next enter some words in F2
kg1=['y1','y1','y3','Y1','y2','y3','y4','y1','y2','y3','y4','y2','y2']
kg2=['y3','y4','Y2','y1','y3']
kg3=['y1','y2','y3','y4','y2','y2']

#Make a list of these words 
words2=[kg1,kg2,kg3]

#Now form some generators for K
k1=kf1+kg1+kf2
k2=kf3+kg2+kf4
k3=kf5
k4=kg3
k5=kg3+kf3
#Make a list of these words: i.e. a list of generators of K
Kgens=[k5]

###############################
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


# ###############################################################
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
        
g=[]
for w in Kgens:
    if verbose[-1]>1:
        print('\n\n\n',w,' becomes')
    w=listsplitter(w,F1.mongens,F2.mongens)
    if verbose[-1]>1:
        print(w, "after listsplitter and then")
    w=amalgam_normal_form(w,F1,F2,H1,H2)
    if verbose[-1]>1:
        print(" and after amalgam_normal_form w and wv are", w[0], "and ", w[1],'\n') 
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

#return(F1,F2,H1,H2,K,FZ)
# ########################
#write normal forms of powers of k4 to the log file
#with open(logfile, "w") as log: #create logfile 
#    log.write("log file K_words_in_nf \n\n") #and write text to it
output_log_file(logfile,"Kgens: "+str(Kgens))
#for q in Kgens:
#    output_log_file(logfile,str(q))

#v=Kgens[0]
v=k5
u=v
#if verbose[-1]>=1:
#    for q in Kgens:
#        output_log_file(logfile,"Kgens "+str(q))
for i in range(0,2):
    u=element(u+v).word
    if verbose[-1]>=1:
        output_log_file(logfile,"i "+str(i+2)+" v^i "+str(u)+"\n")
    U=listsplitter(u,F1.mongens,F2.mongens)
    if verbose[-1]>1:
        print(U, "= v^i after listsplitter and then \n")
    U=amalgam_normal_form(U,F1,F2,H1,H2)
    if verbose[-1]>=1:
        output_log_file(logfile," and after amalgam_normal_form v^i and v^i(z) are "+str(U[0])+" and "+str(U[1]))
    #w=w[1]
    # g.append(w)

### at the end close the log file
log.close()
