from wordmap import *

#set the name of  the output file for the relators of Collins' example
outfile='mihailova/collins.txt'

#open this file and write some initial text
with open(outfile, "w") as out: #create outfile 
    out.write("output file for Collins relators from mihailova.py \n\n") #and write text to it
#out.close()


#Enter the number of generators of the group to be mapped 
Grank=10

#Input "Collins" generators (there must be Grank of them)
a='x1'
b='x2'
c='x3'
d='x4'
e='x5'
p='x6'
q='x7'
r='x8'
t='x9'
k='x10'

#Enter the number of relators of the group to be mapped, and create a blank list of relators
#(this makes typing easier below)
num_rels=27
R=[]
for i in range(0,num_rels):
    R.append([]) # the ith relator, initially blank

print("len r", len(r))
#Input relators: words in the free group on the "Collins" generators:
# as words in Collins generators
R[0]=[(p,10),(a,1),(p,-1),(a,-1)]# the word p^10 a p^{-1} a^{-1}
R[1]=[(p,10),(b,1),(p,-1),(b,-1)]# p^10 b p^{-1} b^{-1}
R[2]=[(p,10),(c,1),(p,-1),(c,-1)]
R[3]=[(p,10),(d,1),(p,-1),(d,-1)]
R[4]=[(p,10),(e,1),(p,-1),(e,-1)]
R[5]=[(a,1),(q,10),(a,-1),(q,-1)]
R[6]=[(b,1),(q,10),(b,-1),(q,-1)]
R[7]=[(c,1),(q,10),(c,-1),(q,-1)]
R[8]=[(d,1),(q,10),(d,-1),(q,-1)]
R[9]=[(e,1),(q,10),(e,-1),(q,-1)]
R[10]=[(r,1),(a,1),(r,-1),(a,-1)]
R[11]=[(r,1),(b,1),(r,-1),(b,-1)]
R[12]=[(r,1),(c,1),(r,-1),(c,-1)]
R[13]=[(r,1),(d,1),(r,-1),(d,-1)]
R[14]=[(r,1),(e,1),(r,-1),(e,-1)]
R[15]=[(p,1),(a,1),(c,1),(q,1),(r,1),(q,-1),(a,-1),(c,-1),(p,-1),(r,-1)]
R[16]=[(p,2),(a,1),(d,1),(q,2),(r,1),(q,-2),(a,-1),(d,-1),(p,-2),(r,-1)]
R[17]=[(p,3),(b,1),(c,1),(q,3),(r,1),(q,-3),(b,-1),(c,-1),(p,-3),(r,-1)]
R[18]=[(p,4),(b,1),(d,1),(q,4),(r,1),(q,-4),(b,-1),(d,-1),(p,-4),(r,-1)]
R[19]=[(p,5),(c,1),(e,1),(q,5),(r,1),(q,-5),(a,-1),(c,-1),(e,-1),(p,-5),(r,-1)]
R[20]=[(p,6),(d,1),(e,1),(q,6),(r,1),(q,-6),(b,-1),(d,-1),(e,-1),(p,-6),(r,-1)]
R[21]=[(p,7),(c,1),(d,1),(c,1),(q,7),(r,1),(q,-7),(e,-1),(c,-1),(d,-1),(c,-1),(p,-7),(r,-1)]
R[22]=[(p,8),(c,1),(a,1),(a,1),(a,1),(q,8),(r,1),(q,-8),(a,-1),(a,-1),(a,-1),(p,-8),(r,-1)]
R[23]=[(p,9),(d,1),(a,1),(a,1),(a,1),(q,9),(r,1),(q,-9),(a,-1),(a,-1),(a,-1),(p,-9),(r,-1)]
R[24]=[(p,1),(t,1),(p,-1),(t,-1)]
R[25]=[(q,1),(t,1),(q,-1),(t,-1)]
R[26]=[(k,1),(a,-3),(t,1),(a,3),(k,-1),(a,-3),(t,-1),(a,3)]


#if required make a sublist of  relators to be processed
#List_rels=R[i:j] will process relators R[i] through to R[j] 

#List_rels=R[0:8]# to list all relators replace this line with 
List_rels=R
i=0
for R in List_rels:
    print(i," ", R,"\n\n")
    i+=1

#now call the function map_to_two_gens, in the file wordmap.py
#to translate the elements of List_rels into elements of F(a,b)
#... the output appears in outfile
######################
im_Grels,Trels,Xrels=map_to_two_gens(Grank,List_rels,outfile)
##################

### at the end of the process of formatting Collins relators close the output file
out.close()


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

#Enter the rank of the amalagamated subgroups
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

# Enter the first two words of the  free generating set for K: \{x_3y_3x_1, x_3y_4x_4x_2, R_i, 0\le i \le 26\}
k1=['x3','y3','x1']
k2=['x3','y4','x4','x2']

#make lists of the words in F1 and F2 used as factors in k1 and k2 (this is a pain and not really necessary but a result of how the prog was first written)
Kgens=[k1,k2]
#i=0
for w in Xrels:
    #for i in range(0,1):
    Kgens.append(w)
    #i=+1
#Kgens.append(Xrels[0])
print(Kgens)
#make lists of the words in F1 and F2 used as factors in k1 and k2 (this is needed only because this is how the prog was first set up)
words1,words2=list_factors(F1,F2,Kgens)
###############################
#maximum number of iterations of the main loop
max_iterations=5

######################
########### No user entry beyond this point
##################
delta_n,loop_count=main_loop(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile,change_tree,max_iterations)
### at the end close the log file
log.close()

#print("loop count ",loop_count)
