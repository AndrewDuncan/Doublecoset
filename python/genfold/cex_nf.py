from wordmap import *

#print('digraph g1 {')
#print(str(g1))
#print('}')

####from alg3_cex

#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
testfile='cex_nf/'
#####################

###################
## To get the spanning trees for H1 and H2 as in written notes
## set change_tree = 0 and then 
###################

#verbose is a list (currently of length 11) of 0's and 1's. List entries correspond to 
#functions or files as below. When the corresponding entry is set to one the program (or file) will
#produce "helpful" output. When it is set to 0 nothin unecessary is output. When it's more than 1
#alot of lines, designed to keep track of the program flow, are output to the log file. 
#Entries correspond to files or functions as follows
#0 graph.py
#1 alg1.py
#2 adjust_generators.py
#3 alg3.py all functions except Modx, x=1,2,3,4,5
#4 Mod1 (alg3.py)
#5 Mod2 (alg3.py)
#6 Mod3 (alg3.py)
#7 Mod4 (alg3.py)
#8 Mod5 (alg3.py)
#9 Reassemble (alg3.py)
#
#  
#last entry --- this file
##########0,1,2,3,4,5,6,7,8,9,0
verbose =[0,0,0,0,0,0,0,0,0,0,0]

#open the log file and write an initial line
logfile=testfile+'log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file alg3_cex.py \n\n") #and write text to it


#if you have run the program, and the spanning tree gives the correct generators, but is not the tree you want,
#then set change_tree to 1, to allow user editing of the output labels
change_tree=0


#define the free groups F1 and F2, by giving the number of generators, and letter for the generators
F1=free_group(2,"x")
F2=free_group(2,"y")#do not make both these letters the same

#Enter the rank of the subgroup
Hrank=4
####################
#### enter H1
################
#Choose the 1st subgroup name
Hname1='H1'

############
#################

# Enter some elements of F1, a selection of which can be used to generate the subgroup H1
#
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
h5=['x2','x1','x1']

#make the generators into a list
Hgens1=[h1,h2,h3,h4]

################
### enter H2
##############
#Choose the 2nd subgroup name
Hname2='H2'

# Enter some elements of F2, a selection of which can be used to generate the subgroup H2
#
g1=['y1','Y2']
g2=['y2','y1','y2']
g3=['y2','y2','y2']
g4=['Y2','y1']
#make the generators into a list
Hgens2=[g1,g2,g3,g4]

#########################################################
#########  now enter K
#####################
#enter name of subgroup K
Kname='K'

# Enter a free generating set for K - in stages, first enter words in the factor groups, then concatenate.
#First enter some words in F1
kf1=['x1']
kf2=['X1','x2']
kf3=['x2','X3','x1']
kf4=['x1','x1','x1','x1','x2','x3','X1','X2']
kf5=['x1','x2','x3','x2','X3','X3','X2']

#Make a list of these words and 
#test that they are in F1
words1=[kf1,kf2]

##########
#Next enter some words in F2
kg1=['y1']
kg2=['y3','y4','Y2','y1','y3']

#Make a list of these words and 
#test that they are in F2
words2=[kg1]


#Now form some generators for K
k1=kg1+kf1
k2=kf2

#enter a list of generators of K
Kgens=[k1,k2]

### end alg3_cex
###put in stuff from main loop 
FZ=free_group(int(Hrank),"z")        
#
# find the folding corresponding to the generators entered
#
H1=construct_required_folding(Hname1,Hgens1,testfile,F1,Hrank,verbose,FZ,change_tree,logfile)

# find the folding corresponding to the generators entered
#
H2=construct_required_folding(Hname2,Hgens2,testfile,F2,Hrank,verbose,FZ,change_tree,logfile)
#
#
#
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
#####################################################
####################################################
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
############### end stuff from main loop
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2
d1=phi(H1,['z1','z2','Z3'])
print('d1 = ', d1)
c1=element(d1[0]).word
c2=element(['y2','x2']).word
c=element(c1+c2).word
#r=element(['y2']).word
r=element(phi(H1,['z4'])[0]).word
C=element(c).inverse()
w=element(c1+c2+r+C).word
print('w = ',w)
w=popper(w)
print('w=popper(w)\n',w)
w=listsplitter(w,F1.mongens,F2.mongens)
nw=amalgam_normal_form(w,F1,F2,H1,H2)
print('normal form of w = ',nw)
w=['x2','X1']
#w.append('xss')
for i in range(0,5):
    w.insert(0,'x1')
    w.append('X1')
    print(i," ",w)
    lw=listsplitter(w,F1.mongens,F2.mongens)
    nw=amalgam_normal_form(lw,F1,F2,H1,H2)
    print("  ",nw[1][0][0])

### at the end close the log file
log.close()
