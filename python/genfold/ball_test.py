from ball import *
import pickle 
#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
testfile='ball/'
#####################
#open the log file and write an initial line 
logfile=testfile+'log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file ball_test.py \n\n") #and write text to it


#file to store results
outputfile=testfile+'ball.txt'

#log.close()
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


#if you have run the program, and the spanning tree gives the correct generators, but is not the tree you want,
#then set change_tree to 1, to allow user editing of the output labels
change_tree=1


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

#Make a list of these words
words1=[kf1,kf2,kf3,kf4,kf5]

#####################
#Next enter some words in F2
kg1=['y1','y1','y3','Y1','y2','y3','y4','y1','y2','y3','y4','y2','y2']
kg2=['y3','y4','Y2','y1','y3']

#Make a list of these words 
words2=[kg1,kg2]

#Now form some generators for K
k1=kf1+kg1+kf2
k2=kf3+kg2+kf4
k3=kf5
#Make a list of these words: i.e. a list of generators of K
Kgens=[k1,k2,k3]
    
(H1,H2,FZ)=construct_H_foldings(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,verbose,logfile,change_tree)
K=construct_K(H1,H2,FZ,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile)

#L=[['y1','y1'], ['x3','X2'],['x1','z1']]
#L1=[['a'],['b'],['c']]
#L2=[['y1','y1'], ['Y1','y2'],['Y2','Y1']]

R=3# radius of ball to generate
S,T,B,B_nf=ball(R,Kgens,F1,F2,Hrank,H1,H2,logfile,outputfile)

#w=B_nf[0][0]
#print(w)

#input delta_n, saved by the previous run of K_fix.py
graphfile='input_K/delta_n_save.txt'
delta_n = pickle.load( open(graphfile, "rb" ) )
root=delta_n.root
for i in range(0,len(B_nf)):
    for w in B_nf[i]:
        test_w=graph_pass(delta_n,w,root).acc_read_rem()
        if len(test_w[1])+len(test_w[2])!=0:
            #        print("w in K", w)
            #    else:
            # print("w not accepted ", w,"\n")
            #print("TA",test_w,"\n\n")
            ind=B_nf[i].index(w)
            print("i is ", i,"ind ",ind)
            #B_word=B[i][ind]
            #print("original word ",B_word)
#       Apref=[] #this will be the max accepted prefix
#        Rpref=[] #this will be the max readable prefix following Apref
#        Apref_in_Z=[] #this will be Apref written in Z generators instead of X generators
#        suffix=self.word # this will be the remainder of the word
#        return(Apref,Rpref,suffix,u,Apref_in_Z)
#print("S = ", S,"\n\n T is \n")
i=0
with open(logfile, "a") as log: #write to logfile 
    for b in B:
        log.write("list B: "+str(i)+"\n") 
        for w in b:
            log.write(str(w)+"\n")
        i+=1
i=0
with open(logfile, "a") as log: #append to logfile 
    for b in B_nf:
        log.write("list B_nf: "+str(i)+"\n") 
        for w in b:
            log.write(str(w)) 

print("B")
for i in range(0,len(B)):
    print(len(B[i]))
print("B_nf")
for i in range(0,len(B_nf)):
    print(len(B_nf[i]))
#with open(outputfile, 'r') as output:
#    B_data = output.read()

#for b in B_data:
#    print(b,"\n\n\n")
#pickle.dump(B_nf, open(outputfile, "wb" ) )
#print("\n\nB_data ", B_data)
#print("\n\n B_data[-1]", B_data[-1])

print("B[2][10]", B[2][10])
print("B_nf[2][10]", B_nf[2][10])
