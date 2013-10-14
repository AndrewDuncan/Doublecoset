from alg3 import *

G=Graph(False,'',1)
a=G.addVertex()
b=G.addVertex()
c=G.addVertex()
d=G.addVertex()
e=G.addVertex()
f=G.addVertex()
G.addEdge(a,b,'x')
G.addEdge(a,b,'y')
G.addEdge(b,c,'x')
G.addEdge(b,c,'y')
G.addEdge(c,d,'x')
G.addEdge(c,d,'y')
G.addEdge(d,a,'x')
G.addEdge(d,a,'y')
G.addEdge(a,e,'w')
G.addEdge(e,a,'w')
G.addEdge(e,f,'x')
G.addEdge(f,e,'y')
F1=free_group(2,"x")
Z=free_group(4,"z")
h1=['x1','X2']
h2=['x2','x1','x2']
h3=['x2','x2','x2']
h4=['X2','x1']
H1=subgroup('H1',[h1,h2,h3,h4],['z1','z2','z3','z4'])
(flower1,double1,forest1,bfs1)=alg2_pre(H1)

testfile='outlabels_test/'
# Open outlabels_test/display_outlabels.gv in write mode
with open(testfile+"display_outlabels.gv", "w") as Gr:
    Gr.write("digraph G {\n") #and write to it
with open(testfile+"display_outlabels.gv", "a") as Gr: #then open it in append mode
    Gr.write(str(flower1)) #and continue to write to it
    Gr.write("}")
Gr.close()

#D= G.double()
#print ("digraph SxS {")
#print (str(D))
#print ("}")
