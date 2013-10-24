from adjust_generators import *

#set verbose =1 to see lots of information and to 0 for a quiet run
verbose =1

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
H1=construct_required_folding(Hname1,Hgens1,testfile,F1,Hrank,verbose,FZ,change_tree)

#write the final folding as a graph
filename=testfile+"stallings1.gv"
output_graph_file(H1.flower,filename,"stallings1",verbose)
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
H2=construct_required_folding(Hname2,Hgens2,testfile,F2,Hrank,verbose,FZ,change_tree)

#write the final folding as a graph
filename=testfile+"stallings2.gv"
output_graph_file(H2.flower,filename,"stallings2",verbose)

#########################################################
#########  now enter K
######################

# Enter a free generating set for K - in stages, first enter words in the factor groups, then concatenate.
#First enter some words in F1
kf1=['x2','x3','x3','X2','x1','x1','x1','x1','x3','x3','x3','X1','X1','X3','X2','X1']
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


kfs=[kf1,kf2,kf3,kf4,kf5]
for w in kfs:
    print('\n',w,' becomes \n')
    w=listsplitter(w,F1.mongens,F2.mongens)
    print(w, "\n after listsplitter and then \n")
    w=amalgam_normal_form(w,F1,F2,H1,H2)
    print("after amalgam_normal_form w and wv are", w[0], "\n and ", w[1],'\n')

kgs=[kg1,kg2]
for w in kgs:
    print('\n',w,' becomes \n')
    w=listsplitter(w,F1.mongens,F2.mongens)
    print(w, "\n after listsplitter and then \n")
    w=amalgam_normal_form(w,F1,F2,H1,H2)
    print("after amalgam_normal_form w and wv are", w[0], "\n and ", w[1],'\n')

k1=kf1+kg1+kf2
print('\n\n\n',k1,' becomes')
k1=listsplitter(k1,F1.mongens,F2.mongens)
print(k1, "after listsplitter and then")
k1=amalgam_normal_form(k1,F1,F2,H1,H2)
print(" and after amalgam_normal_form k1 and k1v are", k1[0], "and ", k1[1],'\n')
