#from main_loop import *
from wordmap import *

###################
## To get the spanning trees for H1 and H2 as required it may be necessary to
## set change_tree = 1 and then 
## when this program is run answer the questions with the
## sequence of answers: ????
###################

#verbose is a list (currently of length 11) of integers. List entries correspond to 
#functions or files as below. When the corresponding entry is set to one the program (or file) will
#produce "helpful" output. When it is set to 0 nothing unecessary is output. When it's more than 1
#alot of lines, designed to keep track of the program flow, are output to the log file
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
#last entry --- this file
##########0,1,2,3,4,5,6,7,8,9,0
verbose =[0,0,0,0,0,0,0,0,0,0,0]

#set the name of  the log file
logfile='mihailova/log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file from mihailova.py \n\n") #and write text to it
#log.close()

#if you have run the program, and the spanning tree gives the correct generators, but is not the tree you want,
#then set change_tree to 1, to allow user editing of the output labels
change_tree=0


#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='mihailova/graphs/'

#define the free groups F1 and F2, by giving the number of generators, and letter for the generators
F1=free_group(4,"x")
F2=free_group(4,"y")#do not make both these letters the same

#Enter the rank of the subgroup
Hrank=6

####################
#### enter H1
################
#Choose the 1st subgroup name
Hname1='H1'

# Enter some elements of F1, a selection of which can be used to generate the subgroup H1
#
h1=['X3','x1','x3']
h2=['X3','x2','x3']
h3=['x1']
h4=['x2']
h5=['x4','x1','X4']
h6=['x4','x2','X4']
#make the generators into a list
Hgens1=[h1,h2,h3,h4,h5,h6]

################
### enter H2
##############
#Choose the 2nd subgroup name
Hname2='H2'

# Enter some elements of F2, a selection of which can be used to generate the subgroup H2
#$h'_1= y_1$, 
#$h'_2 = y_2$, 
#$h'_3 = y_3^{-1} y_1 y_3 $, 
#$h'_4 = y_3^{-1} y_2 y_3$,
#$h'_5= y_4^{-1} y_1 y_4$, 
#$h'_6 = y_4^{-1} y_2 y_4$.

g1=['y1']
g2=['y2']
g3=['Y3','y1','y3']
g4=['Y3','y2','y3']
g5=['Y4','y1','y4']
g6=['Y4','y2','y4']
#make the generators into a list
Hgens2=[g1,g2,g3,g4,g5,g6]

#########################################################
#########  now enter K
######################
#enter name of subgroup K
Kname='K'

# Enter a free generating set for K: \{x_3y_3x_1, x_3y_4x_4x_2, R_i, 0\le i \le 26\}
k1=['x3','y3','x1']
k2=['x3','y4','x4','x2']
k3=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2']
k4=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'X2', 'x1']
k5=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'X2', 'x1', 'x1']
k6=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x2', 'X1', 'X1', 'X2', 'x1', 'x1', 'X2', 'x1', 'x1', 'x1']
k7=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x2', 'X1', 'X2', 'x1', 'X2', 'x1', 'x1', 'x1', 'x1']
k8=['x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k9=['X1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k10=['X1', 'X1', 'x2', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k11=['X1', 'X1', 'X1', 'x2', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k12=['X1', 'X1', 'X1', 'X1', 'x2', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k13=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2']
k14=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'x1']
k15=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'x1', 'x1']
k16=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'X2', 'x1', 'x1', 'x1']
k17=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'X2', 'x1', 'x1', 'x1', 'x1']
k18=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'x2', 'X1', 'X1', 'X1', 'X1', 'x2', 'X1', 'x2', 'x1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X2', 'X1', 'X1', 'X1', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k19=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'X1', 'x2', 'X1', 'X1', 'X1', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X1', 'X2', 'X1', 'X1', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k20=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'x2', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X2', 'X1', 'X1', 'X1', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k21=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'x2', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X2', 'X1', 'X1', 'X2', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k22=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x2', 'X1', 'X1', 'x2', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X2', 'X1', 'X1', 'X2', 'X1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k23=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x2', 'X1', 'x2', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X2', 'X1', 'X2', 'X1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k24=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x2', 'X1', 'x2', 'x1', 'x2', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'x1', 'x1', 'X2', 'x1', 'x1', 'X2', 'X1', 'X2', 'x1', 'X2', 'X1', 'X1', 'X1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k25=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x1', 'x2', 'x1', 'x1', 'x2', 'x2', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X2', 'X2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k26=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x1', 'x1', 'x2', 'x1', 'x1', 'x1', 'x2', 'x2', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'x2', 'X1', 'x2', 'x1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X2', 'X2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k27=['X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'X2', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k28=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'X1', 'X1', 'x2', 'x1', 'x1', 'X2', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1']
k29=['X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X2', 'X2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'x2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'x2', 'x2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'X2', 'X2', 'X2', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X1', 'X2', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x1', 'x2', 'x2', 'x2']
#make list of generators of K
Kgens=[k1,k2,k3,k4,k5,k6,k7,k8,k9,k10,k11,k12,k13,k14,k15,k16,k17,k18,k19,k20,k21,k22,k23,k24,k25,k26,k27,k28,k29]
#make lists of the words in F1 and F2 used as factors in k1 and k2 (this is needed only because this is how the prog was first set up)
words1,words2=list_factors(F1,F2,Kgens)
###############################
#maximum number of iterations of the main loop
max_iterations=1

######################
########### No user entry beyond this point
##################
delta_n,loop_count=main_loop(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile,change_tree,max_iterations)


### at the end close the log file
log.close()

print("loop count ",loop_count)
