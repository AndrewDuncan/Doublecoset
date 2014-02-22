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
#set log_needed to 1 to generate a log file listing words in the ball of radius R (could be a large file!)
log_needed=0

#file to store results
outputfile=testfile+'ball.txt'


getfile='input_K/input_save.txt'  
Hrank,Hname1,Hname2,Hgens1,Hgens2,F1,F2,words1,words2,Kname,Kgens= pickle.load( open(getfile, "rb" ) ) 
getfile='input_K/H1_save.txt'  
H1 = pickle.load( open(getfile, "rb" ) ) 
getfile='input_K/H2_save.txt'  
H2 = pickle.load( open(getfile, "rb" ) ) 
getfile='input_K/FZ_save.txt'  
FZ = pickle.load( open(getfile, "rb" ) )
getfile='input_K/K_save.txt'  
K = pickle.load( open(getfile, "rb" ) )
# 
#(H1,H2,FZ)=construct_H_foldings(Hrank,Hname1,Hname2,Hgens1,Hgens2,testfile,F1,F2,verbose,logfile,change_tree)
#K=construct_K(H1,H2,FZ,testfile,F1,F2,words1,words2,Kname,Kgens,verbose,logfile)

#L=[['y1','y1'], ['x3','X2'],['x1','z1']]
#L1=[['a'],['b'],['c']]
#L2=[['y1','y1'], ['Y1','y2'],['Y2','Y1']]
Kgrs=K.subgp_gens

R=7# radius of ball to generate
S,T,B,B_nf=ball(R,Kgens,F1,F2,Hrank,H1,H2,logfile,outputfile)

#w=B_nf[0][0]
#print(w)
ball_save=testfile+'ball_save.txt'
pickle.dump(B_nf, open(ball_save, "wb" ))
if log_needed==1:
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
                        
#print("B")
#for i in range(0,len(B)):
#    print(len(B[i]))
#print("B_nf")
#for i in range(0,len(B_nf)):
#    print(len(B_nf[i]))
#with open(outputfile, 'r') as output:
#    B_data = output.read()

#for b in B_data:
#    print(b,"\n\n\n")
#pickle.dump(B_nf, open(outputfile, "wb" ) )
#print("\n\nB_data ", B_data)
#print("\n\n B_data[-1]", B_data[-1])

#print("B[2][10]", B[2][10])
#print("B_nf[2][10]", B_nf[2][10])
#print("11 th word of ball of radius 2")
#for w in B[2][10]:
#    gi=B[2][10].index(w)
#    print(gi+1," ")
#print("Kgens ",Kgens)
#print("Kgrs ", Kgrs)
