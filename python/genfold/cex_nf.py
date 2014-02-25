from main_loop import *
import pickle 
#this program generates a ball of a given radius in generators previously stored for a subgroup of a (previously stored) amalgam

#So that each run creates a new set of files: set the prefix for the name of all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
# ... the log file will also have this prefix
prefix='cex/'
testfile=prefix+'special_words/'


#####################
#open the log file and write an initial line 
logfile=testfile+'log.txt'
with open(logfile, "w") as log: #create logfile 
    log.write("log file cex_nf.py \n\n") #and write text to it

#as in K_fix.py
#                             1,1  
##########0,1,2,3,4,5,6,7,8,9,0,1
verbose =[0,0,0,0,1,1,1,1,1,1,1,1]
#verbose =[0,0,0,0,0,0,0,0,1,0,0,0]

#file to store results
outputfile=testfile+'test_results.txt'
with open(outputfile, "w") as out: #append to outputfile 
     x=1

#directory of files in which inputs are stored
inputfile='cex/'
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
############### end stuff from main loop
#	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2
d1=phi(H1,['z1','z2','Z3'])
print('d1 = ', d1)
c1=element(d1[0]).word
c2=element(['y2','x2']).word
c=element(c1+c2).word
#r=element(['y2']).word
r=element(phi(H1,['z4'])[0]).word
C=element(c).inverse()
w=element(c1+c2+r+C).word
print('w = ',w)
w=popper(w)
print('w=popper(w)\n',w)
w=listsplitter(w,F1.mongens,F2.mongens)
nw=amalgam_normal_form(w,F1,F2,H1,H2)
print('normal form of w = ',nw)
w=['X2','x1']
#w.append('xss')
C=[]
for i in range(0,5):
    nf_wrd=[]
    w.insert(0,'x1')
    w.insert(0,'x1')
    w.append('X1')
    w.append('X1')
    if verbose[-1]>0:
        output_log_file(logfile,"cex_nf.py: i is "+str(i)+" w is "+ str(w))
    #print(i," ",w)
    lw=listsplitter(w,F1.mongens,F2.mongens)
    if verbose[-1]>0:
        output_log_file(logfile,"cex_nf.py: w is changed to lw by listsplitter: "+ str(lw))
    #print("  ",nw[1][0][0])
    nw=amalgam_normal_form(lw,F1,F2,H1,H2)
    #nw=amalgam_normal_form(lw,F1,F2,H1,H2)
    #print("nw ",nw)
    if verbose[-1]>0:
        output_log_file(logfile,"cex_nf.py: lw is changed to nw by amalgam_normal_form: "+ str(nw))              
    for s in nw[1]:
        if verbose[-1]>0:
            output_log_file(logfile,"cex_nf.py: nw[1] item s is "+ str(s)) 
        for q in s:
            if verbose[-1]>0:
                output_log_file(logfile,"cex_nf.py: s item q is "+ str(q))
            if q!=[]:
                nf_wrd=nf_wrd+q
    
    C.append(nf_wrd)

B_nf=[C]
    
if verbose[10]>0:
    ball_save=testfile+'ball_save.txt'
    pickle.dump(B_nf, open(ball_save, "wb" ))
#
if verbose[-1]>0:
    i=0
    with open(outputfile, "a") as out: #append to outputfile 
        for b in B_nf:
            out.write("list B_nf: "+str(i)+"\n") 
            for w in b:
                out.write(str(w)) 
                        
### at the end close files
log.close()
out.close()
