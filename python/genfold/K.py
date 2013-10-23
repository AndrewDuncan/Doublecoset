from adjust_generators import *

#set verbose =1 to see lots of information and to 0 for a quiet run
verbose =1
#So that each test creates a new set of graphs: set the prefix for all file names for your particular test here:
#if this name is the name of a directory - then that directory must exist as a sub-directory of the home dir of this file
testfile='input_K/'

#define the free groups F1 and F2, by giving the number of generators, and letter for the generators
F1=free_group(3,"x")
F2=free_group(4,"y")


# Enter a free generating set for K - in stages, first enter words in the factor groups, then concatenate.
#First enter words in F1
f1=['x2','x3','x3','X2','x1','x1','x1','x1','x3','x3','x3','X1','X1','X3','X2','X1']
f2=['X3','X2','X1','x2','X3','X2','X1']
f3=['x2','X3','x1']
f4=['x1','x1','x1','x1','x2','x3','X1','X2']
f5=['x1','x2','x3','x2','X3','X3','X2']

#Make a list of theses words and 
#Test that these words are in F1
words1=[f1,f2,f3,f4,f5]
##########
g1=['y1','y1','y3','Y1','y2','y3','y4','y1','y2','y3','y4','y2','y2']
g2=['y3','y4','Y2','y1','y3']
#h1=['X1','x3','x4','X2']
#h2=['x2','X1','x3','x4','x2']
#h3=['x2','x2','x2']
#h4=['X2','x1','x3','x2']
#
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
#h5=['x2','x1','x1']
