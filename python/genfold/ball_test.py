from main_loop import *
import pickle 
#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
prefix='cex/'
#results of tests and files of words lie in subdirectories of prefix - name the subdir required as testfile
testfile=prefix+'special_words/'
#####################
#open the log file and write an initial line 
logfile=testfile+'ball_test_log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file for ball_test.py \n\n") #and write text to it


#file to store results
outputfile=testfile+'ball_test_results.txt'
with open(outputfile, "w") as out: #create logfile 
    out.write("output file for ball_test.py \n\n") #and write text to it

#input delta_n, saved by the previous run of K_fix.py
graphfile=prefix+'delta_n_save.txt'
delta_n = pickle.load( open(graphfile, "rb" ) )

#input the ball to test
ballfile=testfile+'ball_save.txt'
B_nf = pickle.load( open(ballfile,"rb") )
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
            with open(outputfile, "a") as out:
                out.write("word not accepted: i is "+str(i)+" ind is "+str(ind)+" "+str(w)+"\n") 
            #print("i is ", i,"ind ",ind)
            #B_word=B[i][ind]
            #print("original word ",B_word)
#       Apref=[] #this will be the max accepted prefix
#        Rpref=[] #this will be the max readable prefix following Apref
#        Apref_in_Z=[] #this will be Apref written in Z generators instead of X generators
#        suffix=self.word # this will be the remainder of the word
#        return(Apref,Rpref,suffix,u,Apref_in_Z)
#print("S = ", S,"\n\n T is \n")
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
