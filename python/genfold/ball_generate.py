from ball import *
import pickle 
sys.setrecursionlimit(1500)
import time 
localtime = time.asctime(time.localtime(time.time()))

########################################
#this program generates a ball of a given radius in generators previously stored for a subgroup of a (previously stored) amalgam
#before running it 
#alg3_cex.py or K_fix.py should have been run, with 10th item of verbose set to 1 (to store H1 and H2 and K) 
#and testfile = cex or input_K; 
# and the following must be set (instructions below):
#prefix
#verbose
#R
#########################################
########################################


#Set the prefix for the name of all files here:
#this should be the name of the directory where H1 and H2 were stored by alg3_cex or K_fix  
# ... the log file will also have this prefix
prefix='input_K/'
#prefix='cex/'
#
#whatever prefix is, the results of ball_generate will be stored in  directory prefix/ball/ which must be a subdir of prefix
testfile=prefix+'ball/'


#####################
#open the log file and write an initial line 
logfile=testfile+'ball_generate_log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file ball_generate.py: "+str(localtime)+"\n\n") #and write text to it
#set last entry of verbose to something > 0 to generate a log file listing words in the ball of radius R (could be a large file!)

#as in K_fix.py
#10th entry of verbose > 0 --- save ball in file for later use
#last entry of verbose > 1 --- output log file with dc normal forms saved
#                             1,1,1 
##########0,1,2,3,4,5,6,7,8,9,0,1,2
verbose =[0,0,0,0,1,1,1,1,1,1,1,0,1]
#verbose =[0,0,0,0,0,0,0,0,1,0,0,0]
#

#file to store results
outputfile=testfile+'ball.txt'
with open(outputfile, "w") as out:#initialise outputile
    out.write("ball_generate.py output file: "+str(localtime)+"\n\n") 


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

#set the radius R
R=5# radius of ball to generate
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
