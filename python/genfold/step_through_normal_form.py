from ball import *
import pickle 
import time 
localtime = time.asctime(time.localtime(time.time()))
#this program generates a ball of a given radius in generators previously stored for a subgroup of a (previously stored) amalgam

#So that each run creates a new set of files: set the prefix for the name of all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
#prefix
prefix='cex/'
#testfile='input_K/ball/'
testfile=prefix


#####################
#open the log file and write an initial line 
logfile=testfile+'nf_steps_log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file step_through_normal_form.py: "+str(localtime)+"\n\n") #and write text to it
#set last entry of verbose to something > 0 to generate a log file listing words in the ball of radius R (could be a large file!)

#as in K_fix.py
#10th entry of verbose > 0 --- save ball in file for later use
#last entry of verbose > 1 --- output log file with dc normal forms saved
#                             1,1  
##########0,1,2,3,4,5,6,7,8,9,0,1
verbose =[0,0,0,0,1,1,1,1,1,1,1,1]
#verbose =[0,0,0,0,0,0,0,0,1,0,0,0]


#file to store results
outputfile=prefix+'nf_steps.txt'
#outputfile=testfile+'ball.txt'
with open(outputfile, "w") as out:#initialise outputile
    out.write("step_through_normal_form.py output file: "+str(localtime)+"\n\n") 


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


#input the words to test
#ballfile=testfile+'ball_save.txt'
#B_nf = pickle.load( open(ballfile,"rb") )
#w=[['z1', 'z2', 'Z3', 'y2', 'x2'],['z1', 'z2', 'Z3', 'y2', 'x2'],['z4'],['Z4', 'Z2', 'X2', 'Y2'],['Z4', 'Z2', 'X2', 'Y2']]
w=['z1', 'z2', 'Z3', 'y2', 'x2','z1', 'z2', 'Z3', 'y2', 'x2', 'Z2', 'X2', 'Y2','Z4', 'Z2', 'X2', 'Y2']
        w=listsplitter(w,F1.mongens,F2.mongens)
        if verbose[-1]>1:
            output_log_file(logfile,"output by alg2.py, listsplitter is "+ str(w))
            #print(w, "after listsplitter and then")
        w=amalgam_normal_form(w,F1,F2,H1,H2)
        if verbose[-1]>1:
            output_log_file(logfile,"and output of alg2.py, amalgam_normal_form is w = "+ str(w[0])+" wv "+str(w[1]))
            #print(" and after amalgam_normal_form w and wv are", w[0], "and ", w[1],'\n') 
        w=w[1]
root=delta_n.root
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
