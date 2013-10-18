import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#note: this program only works if the distance from 1 in the tree for gamma is 1, 
#nothing to add to theta to form theta1: so theta1=theta2
I=Graph(rooted=True,label='I')
I.addLoop(I.root,'bCaySrtxzAB')
I.addLoop(I.root,'yyxacaXyrSXYZYA')
I.addLoop(I.root,'zYY')

while I.fold() is True:
    I.fold()


y1list=[]
for i in range(0,4):
    y1list.append(I.vertices[i])

for i in range(8,24):
    y1list.append(I.vertices[i])

for v in y1list:
    I.removeVertex(v)   


vlist=I.vertices

while I.fold() is True:
    I.fold()
vlist=I.vertices

I.addPath(vlist[0],vlist[1],'s')

while I.fold() is True:
   I.fold()

G=Graph(label='G2')
a=G.addVertex(1)
b=G.addVertex(2)
c=G.addVertex(3)
d=G.addVertex(4)
e=G.addVertex(5)
f=G.addVertex(6)
G.addEdge(a,b,'t')
G.addEdge(b,a,'u')
G.addEdge(a,f,'s')
G.addEdge(f,a,'s')
G.addEdge(a,c,'r')
G.addEdge(c,d,'r')
G.addEdge(d,e,'t')
G.addEdge(f,e,'r')   

Tree = {'2':'t','3':'r','4':'rr','5':'Sr','1':''} #each vertex of G is associated to the path which  joins it to 1 in the spanning tree for G

SimReps =[('1','6'),('1','3'),('3','1'),('1','4'),('4','1'),('3','6'),('6','3'),('5','3'),('4','1'),('4','2'),('4','3'),('5','2'),('1','2'),('2','1'),('1','5'),('5','1'),('2','3'),('3','2'),('2','4'),('4','2'),('2','6'),('6','2'),('4','6'),('6','4'),('5','6'),('6','5')]

P=I.product(G)

plist=P.vertices # list of vertices of P

hitlist = []
for c in plist:
    if str(c.label)[str(c.label).index('-')+1:] == '1':
        hitlist.append(c)

   
hitlist = []
for c in plist:
    if str(c.label)[str(c.label).index('-')+1:] == '1':
        hitlist.append(c)
#        print "(",str(c.label)[0:str(c.label).index('-')], ",", str(c.label)[str(c.label).index('-')+1:], ")",

print hitlist

def allneighbours(v): #return all edges incident to a given vertex
    neighbourList = [] # a list of all edges incident to a given vertex
    for e in v.inedgesList:
        neighbourList.append((e,'in')) #append in edges
       
    for e in v.outedgesList:
        neighbourList.append((e,'out')) #append outedges
    return neighbourList


neighbours = dict()        


def indexneighbours(v): # make an index of all neighbours of a vertex
   n = str(v.label)
   nl=allneighbours(v)
   neighbours[n]=nl


def onelist(): #make an index of all neighbours of vertics with rhs label = 1
    for c in plist:
        if str(c.label)[str(c.label).index('-')+1:] == '1':
            indexneighbours(c)

onelist()
for a in range(len(hitlist)):
    v=hitlist[a]
    nl = neighbours[v.label]
    vl = v.label[0:v.label.index('-')]            #left hand side of label of v
    for i in range(len(nl)): #run through the list of neighbours of a  vertex
        l=str(nl[i][0][1].label) #l is the label of the vertex
        left = l[0:l.index('-')]            #left is the lhs of the label: from theta-n
        right = l[l.index('-')+1:]          #right is the rhs of the label: from gamma-k
        L=str(nl[i][0][0])       #L is the edge label
        d=str(nl[i][1])
        if d == 'out':
            Q = L             #Q is the label taking direction into account
        else:
            Q = L.capitalize() 
    
            for k in range(a+1,len(hitlist)): #run through the vertices in hitlist with bigger index than v
                w = hitlist[k]              #w is the kth on the list
                wl = w.label[0:w.label.index('-')]            #left hand side of label of w
                kl=  neighbours[w.label]    #kl is the list of vertices incident to w
                for j in range(len(kl)): #run through the list of neighbours of   vertex w
                    kl_l = str(kl[j][0][1].label) #kl_l is the label of the jth vertex of kl
                    kleft = kl_l[0:kl_l.index('-')] #left is the lhs of the label of the jth vertex of kl
                    kright = kl_l[kl_l.index('-')+1:]          #right is the rhs of the label of the jth vertex
                    if left == kleft: #when left = kleft a path might be added to theta4
                        kl_L=str(kl[j][0][0])       #kl_L is the edge label
                        kl_d=str(kl[j][1])
                        if kl_d == 'out':
                            kl_Q = kl_L              #kl_Q is the label taking direction into account
                        else:
                            kl_Q = kl_L.capitalize()
                            
                
                        if Q == Tree[right] and kl_Q == Tree[kright]:#second condition for a path to be added
                            if (right,kright) in SimReps: # final condition for a path to be added
                                pass
                            else:
                                print "Add path for ", v.label, "to ", l, " and ", w.label, "to", kl_l, "labels in tree are", Q, kl_Q 
