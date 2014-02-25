from ball import *
import pickle 
#this program generates a ball of a given radius in generators previously stored for a subgroup of a (previously stored) amalgam

#So that each run creates a new set of files: set the prefix for the name of all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
#prefix
prefix='cex/'
#testfile='input_K/ball/'
testfile=prefix+'ball/'


#####################
#open the log file and write an initial line 
logfile=testfile+'log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file ball_generate.py \n\n") #and write text to it
#set last entry of verbose to something > 0 to generate a log file listing words in the ball of radius R (could be a large file!)

#as in K_fix.py
#10th entry of verbose > 0 --- save ball in file for later use
#last entry of verbose > 1 --- output log file with dc normal forms saved
#                             1,1  
##########0,1,2,3,4,5,6,7,8,9,0,1
verbose =[0,0,0,0,1,1,1,1,1,1,1,0]
#verbose =[0,0,0,0,0,0,0,0,1,0,0,0]
#change_tree=0#only needed if foldings are to be generated here

#file to store results
outputfile=testfile+'ball.txt'
with open(outputfile, "w") as out:#initialise outputile
    # do nothing


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

R=10# radius of ball to generate
S,T,B,B_nf=ball(R,Kgens,F1,F2,Hrank,H1,H2,logfile,verbose)

#w=B_nf[0][0]
#print(w)
if verbose[10]>0:
    ball_save=testfile+'ball_save.txt'
    pickle.dump(B_nf, open(ball_save, "wb" ))
#
if verbose[-1]>0:
    i=0
    with open(outputfile, "a") as out: #write to outputfile 
        for b in B:
            out.write("list B: "+str(i)+"\n") 
            for w in b:
                out.write(str(w)+"\n")
            i+=1
    i=0
    with open(outputfile, "a") as out: #append to outputfile 
        for b in B_nf:
            out.write("list B_nf: "+str(i)+"\n") 
            for w in b:
                out.write(str(w)) 
  
### at the end close files
log.close()
out.close()
