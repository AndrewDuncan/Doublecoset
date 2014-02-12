from wordmap import *

#set the name of  the output file
outfile='mihailova/collins.txt'

with open(outfile, "w") as out: #create outfile 
    out.write("output file wordmap \n\n") #and write text to it
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

### at the end close the output file
out.close()
