from alg3 import *

###################
## To get the spanning trees for H1 and H2 as in the paper (as near as possible)
## set change_tree = 1 and then 
## when this program is run answer the questions with the
## sequence of answers: n, y, 1, 1, 3
###################

#verbose is a list (currently of length 10) of 0's and 1's. List entries correspond to 
#functions or files as below. When the corresponding entry is set to one the program (or file) will
#produce "helpful" output. When it is set to 0 nothin unecessary is output.
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
#
#  
#last entry --- this file
##########0,1,2,3,4,5,6,7,8,9
verbose =[1,1,1,1,1,1,1,1,1,1]

#if any of the entries of verbose are equal 1, set the name of  the log file
logfile='tmp.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file K_fix \n\n") #and write text to it
log.close()

#if you have run the program, and the spanning tree gives the correct generators, but is not the tree you want,
#then set change_tree to 1, to allow user editing of the output labels
change_tree=1


#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='input_K/'

#define the free groups F1 and F2, by giving the number of generators, and letter for the generators
F1=free_group(3,"x")
F2=free_group(4,"y")#do not make both these letters the same

#Enter the rank of the subgroup
Hrank=3

#construct the group FZ
FZ=free_group(int(Hrank),"z")        
#
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

#find the folding corresponding to the generators entered
#
H1=construct_required_folding(Hname1,Hgens1,testfile,F1,Hrank,verbose,FZ,change_tree,logfile)

#write the final folding as a graph
filename=testfile+"stallings1.gv"
output_graph_file(H1.flower,filename,"stallings1",verbose,logfile)
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

#find the folding corresponding to the generators entered
#
H2=construct_required_folding(Hname2,Hgens2,testfile,F2,Hrank,verbose,FZ,change_tree,logfile)

#write the final folding as a graph
filename=testfile+"stallings2.gv"
output_graph_file(H2.flower,filename,"stallings2",verbose,logfile)

#########################################################
#########  now enter K
######################

# Enter a free generating set for K - in stages, first enter words in the factor groups, then concatenate.
#First enter some words in F1
kf1=['x2','x3','x3','X2','x1','x1','x1','x1','x3','X1','X1','X3','X2','X1']
kf2=['X3','X2','X1','x2','X3','X2','X1']
kf3=['x2','X3','x1']
kf4=['x1','x1','x1','x1','x2','x3','X1','X2']
kf5=['x1','x2','x3','x2','X3','X3','X2']

#Make a list of these words and 
#test that they are in F1
words1=[kf1,kf2,kf3,kf4,kf5]
words_in_F=generators_in_free_group(F1,words1)# this will be 0 if all elements of words1 are in F1, and 1 otherwise
if words_in_F!=0: #if some of words1 are not in F1: halt with an error message
    error_message="the first list of words entered must only contain elements of F1"
    sys.exit(error_message)
##########
#Next enter some words in F2
kg1=['y1','y1','y3','Y1','y2','y3','y4','y1','y2','y3','y4','y2','y2']
kg2=['y3','y4','Y2','y1','y3']

#Make a list of these words and 
#test that they are in F2
words2=[kg1,kg2]
words_in_F=generators_in_free_group(F2,words2)# this will be 0 if all elements of words2 are in F2, and 1 otherwise
if words_in_F!=0: #if some of words2 are not in F2: halt with an error message
    error_message="the second list of words entered must only contain elements of F2"
    sys.exit(error_message)


Kl=[]
kfs=[kf1,kf2,kf3,kf4,kf5]
for w in kfs:
    if verbose[-1]==1:
        print('\n',w,' becomes \n')
    w=listsplitter(w,F1.mongens,F2.mongens)
    if verbose[-1]==1:
        print(w, "\n after listsplitter and then \n")
    w=amalgam_normal_form(w,F1,F2,H1,H2)
    if verbose[-1]==1:
        print("after amalgam_normal_form w and wv are", w[0], "\n and ", w[1],'\n')
    Kl.append(w[1])

if verbose[-1]==1:
    for w in Kl:
        print("w is ", w)

Kr=[]
kgs=[kg1,kg2]
for w in kgs:
    if verbose[-1]==1:
        print('\n',w,' becomes \n')
    w=listsplitter(w,F1.mongens,F2.mongens)
    if verbose[-1]==1:
        print(w, "\n after listsplitter and then \n")
    w=amalgam_normal_form(w,F1,F2,H1,H2)
    if verbose[-1]==1:
        print("after amalgam_normal_form w and wv are", w[0], "\n and ", w[1],'\n')
    Kr.append(w[1])

if verbose[-1]==1:
    for w in Kr:
        print("w is ", w)

#Now form some generators for K
k1=kf1+kg1+kf2
if verbose[-1]==1:
    print('\n\n\n',k1,' becomes')
k1=listsplitter(k1,F1.mongens,F2.mongens)
if verbose[-1]==1:
    print(k1, "after listsplitter and then")
k1=amalgam_normal_form(k1,F1,F2,H1,H2)
if verbose[-1]==1:
    print(" and after amalgam_normal_form k1 and k1v are", k1[0], "and ", k1[1],'\n')

k2=kf3+kg2+kf4
if verbose[-1]==1:
    print('\n\n\n',k2,' becomes')
k2=listsplitter(k2,F1.mongens,F2.mongens)
if verbose[-1]==1:
    print(k2, "after listsplitter and then")
k2=amalgam_normal_form(k2,F1,F2,H1,H2)
if verbose[-1]==1:
    print(" and after amalgam_normal_form k2 and k2v are", k2[0], "and ", k2[1],'\n')

k1=k1[1]
k2=k2[1]
k3=Kl[4]
if verbose[-1]==1:
    print("k1 = ",k1)
    print("k2 = ",k2)
    print("k3 = ",k3)

#enter name of subgroup K
Kname='K'
#enter list of generators for K
Kgens=[k1,k2,k3]
#extract the normal form version of these
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

#form the subgroup K
K=subgroup(Kname,Kgens)
#make the Stallings folding of the gens of K
K.stallings()
#and a spanning tree
bfs(K.flower,).forest()
#output the folding to a file
output_graph_file(K.flower,testfile+"Kfolding.gv","Kfold",verbose,logfile)
#########################

F=(F1,F2)
H=(H1,H2)
flower1=H1.flower
flower2=H2.flower
flower=(flower1,flower2)
#
print("now D0")
D0=MakeComps(K.flower,F,FZ,verbose,logfile) # returnsdelta_k0[0],delta_k0[1],delta_z

# Open D0_1.gv in write mode
output_graph_file(D0[0],testfile+"D0_1.gv","D0_1",verbose,logfile)

# Open D0_2.gv in write mode
output_graph_file(D0[1],testfile+"D0_2.gv","D0_2",verbose,logfile)

# Open D0_Z.gv in write mode
output_graph_file(D0[2],testfile+"D0_Z.gv","D0_Z",verbose,logfile)

delta_0=[D0[0],D0[1]] # take the first two components of D0, that is the X1 and X2 components
#
print("now D1")
delta_1=Mod1(delta_0,FZ,H,verbose,logfile)

# Open D1_1.gv in write mode
output_graph_file(delta_1[0],testfile+"D1_1.gv","D1_1",verbose,logfile)

# Open D1_2.gv in write mode
output_graph_file(delta_1[1],testfile+"D1_2.gv","D1_2",verbose,logfile)

print("now D2")
(delta_2,Prod)=Mod2(delta_1,H,verbose,logfile)

# Open P_1_1.gv in write mode
output_graph_file(Prod[0],testfile+"P_1_1.gv","P11",verbose,logfile)

# Open P_1_2.gv in write mode
output_graph_file(Prod[1],testfile+"P_1_2.gv","P12",verbose,logfile)

# Open D2_1.gv in write mode
output_graph_file(delta_2[0],testfile+"D2_1.gv","D2_1",verbose,logfile)

# Open D2_2.gv in write mode
output_graph_file(delta_2[1],testfile+"D2_2.gv","D2_2",verbose,logfile)


print("now D3")
(delta_3,Prod)=Mod3(delta_2,H,verbose,logfile)

# Open D3_1.gv in write mode
output_graph_file(delta_3[0],testfile+"D3_1.gv","D3_1",verbose,logfile)

# Open D3_2.gv in write mode
output_graph_file(delta_3[1],testfile+"D3_2.gv","D3_2",verbose,logfile)

# Open P_2_1.gv in write mode
output_graph_file(Prod[0],testfile+"P_2_1.gv","P21",verbose,logfile)

# Open P_2_2.gv in write mode
output_graph_file(Prod[1],testfile+"P_2_2.gv","P22",verbose,logfile)


print("now D4")
(delta_4,Prod)=Mod4(delta_3,H,verbose,logfile)

# Open D4_1.gv in write mode
output_graph_file(delta_4[0],testfile+"D4_1.gv","D4_1",verbose,logfile)

# Open D4_2.gv in write mode
output_graph_file(delta_4[1],testfile+"D4_2.gv","D4_2",verbose,logfile)

# Open P_3_1.gv in write mode
output_graph_file(Prod[0],testfile+"P_3_1.gv","P31",verbose,logfile)

# Open P_3_2.gv in write mode
output_graph_file(Prod[1],testfile+"P_3_2.gv","P32",verbose,logfile)

