from main_loop import *

###################
## To get the spanning trees for H1 and H2 as in the paper (as near as possible)
## set change_tree = 1 and then 
## when this program is run answer the questions with the
## sequence of answers: n, y, 1, 1, 3
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
verbose =[0,0,0,0,1,1,1,1,1,1,0]

#if any of the entries of verbose are equal 1, set the name of  the log file
logfile='malnormal/output/log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file K_malnormal \n\n") #and write text to it
#log.close()

#if you have run the program, and the spanning tree gives the correct generators, but is not the tree you want,
#then set change_tree to 1, to allow user editing of the output labels
change_tree=1


#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='malnormal/output/'

#define the free groups F1 and F2, by giving the number of generators, and letter for the generators
F1=free_group(4,"x")
F2=free_group(4,"y")#do not make both these letters the same

#Enter the rank of the subgroup
Hrank=2

####################
#### enter H1
################
#Choose the 1st subgroup name
Hname1='H1'

# Enter some elements of F1, a selection of which can be used to generate the subgroup H1
h1=['X1','X2','x1','x2']
h2=['X1','X1','X2','X2','x1','x1','x2','x2']

#make the generators into a list
Hgens1=[h1,h2]

################
### enter H2
##############
#Choose the 2nd subgroup name
Hname2='H2'

# Enter some elements of F2, a selection of which can be used to generate the subgroup H2
g1=['Y1','Y2','y1','y2']
g2=['y3','y4']

#make the generators into a list
Hgens2=[g1,g2]

#########################################################
#########  now enter K
######################
#enter name of subgroup K
Kname='K'

# Enter a free generating set for K - in stages, first enter words in the factor groups, then concatenate.
#First enter some words in F1
kf1=h1+['x3']+h1+h2+element(h1).inverse()+['x1']+element(h2).inverse()#this is g1 in the text
kf2=h1+h2+h1+h1+element(h2).inverse()+element(h1).inverse()#this is g3 in the text
kf3=h2+['x2','x3','x1','X3','X2','X2']+h1#this is g4 in the text

#print("kf1 ", kf1)
#print("kf2 ", kf2)
#print("kf3 ", kf3)

#Make a list of these words
words1=[kf1,kf2,kf3]

#####################
#Next enter some words in F2
kg1=g1+['y3','y4']+element(g1).inverse()#this is g2 in the text
kg2=g2+g2+['Y2','Y4','Y4','y2']+element(g1).inverse()#this is g5 in the text

#Make a list of these words 
words2=[kg1,kg2]

#Now form some generators for K
k1=kf1+kg2
k2=kf2
k3=kf1+kf1+kf1
k4=kg2+kf1+kg1
k5=element(kg2).inverse()
k6=kf2+kf1+kg1
#Make a list of these words: i.e. a list of generators of K
Kgens=[k1,k2,k3,k4,k5]

###############################
#maximum number of iterations of the main loop
max_iterations=5

######################
########### No user entry beyond this point
##################
delta_n,loop_count=main_loop(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile,change_tree,max_iterations)


### at the end close the log file
log.close()

print("loop count ",loop_count)
