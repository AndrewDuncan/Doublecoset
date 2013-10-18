#Theta 4 x Gamma1 
import copy
from graph import *
import ex_K
ex = ex_K
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#First copy Theta 4 (run it again)

while ex.K.fold() is True:
    ex.K.fold()

xlist=[]
for i in range(4,9):
    xlist.append(ex.K.vertices[i])

for i in range(16,23):
    xlist.append(ex.K.vertices[i])

for v in xlist:
    ex.K.removeVertex(v)

vlist=ex.K.vertices
#print vlist

z1=ex.K.addVertex()
z2=ex.K.addVertex()
z3=ex.K.addVertex()
z4=ex.K.addVertex()
z5=ex.K.addVertex()
ex.K.addEdge(vlist[0],z1,'b')
ex.K.addEdge(vlist[5],z2,'b')
ex.K.addEdge(vlist[6],z3,'b')
ex.K.addEdge(z1,z2,'c')
ex.K.addEdge(z2,z3,'c')
ex.K.addEdge(vlist[6],z4,'a')
ex.K.addEdge(vlist[7],z5,'A')
ex.K.addEdge(z4,z5,'a')
ex.K.addPath(vlist[0],vlist[6],'abc')

while ex.K.fold() is True:
    ex.K.fold()

vlist=ex.K.vertices

#add new paths as necessary
ex.K.addPath(vlist[8],vlist[14],'X')

while ex.K.fold() is True:
   ex.K.fold()
    
ex.K.addPath(vlist[11],vlist[6],'yb')
ex.K.addPath(vlist[12],vlist[0],'Za')
ex.K.addPath(vlist[12],vlist[11],'ZxA')
ex.K.addPath(vlist[15],vlist[8],'xA')
ex.K.addPath(vlist[15],vlist[6],'Xa')
ex.K.addPath(vlist[15],vlist[13],'XzC')
ex.K.addPath(vlist[0],vlist[2],'Yb')
ex.K.addPath(vlist[13],vlist[5],'Za')


while ex.K.fold() is True:
   ex.K.fold()

#now input the graph from example 3.7

G=Graph()
a=G.addVertex(1)
b=G.addVertex(2)
c=G.addVertex(3)
d=G.addVertex(4)
e=G.addVertex(5)
G.addEdge(b,a,'a')  #label x1
G.addEdge(c,b,'a')  #label x1
G.addEdge(a,c,'a') #label x1
G.addEdge(c,d,'b') #label x2
G.addEdge(d,a,'c') #label x3
G.addEdge(a,e,'b') #label x2
G.addEdge(e,e,'c') #label x3

Tree = {'5':'b','2':'A','3':'a','4':'C','1':''} #each vertex of G is associated to the path which  joins it to 1 in the spanning tree for G

SimReps =[('3','1'),('1','3'),('3','4'),('2','4'),('3','5'),('1','4'),('2','5'),('5','3'),('4','1'),('4','2'),('4','3'),('5','2')]

P=ex.K.product(G)

plist=P.vertices # list of vertices of P
#for c in plist:
#    print "(",str(c.label)[0:str(c.label).index('-')], ",", str(c.label)[str(c.label).index('-')+1:], ")",
#
#print  "\n --------------------------------\n"

hitlist = []
for c in plist:
    if str(c.label)[str(c.label).index('-')+1:] == '1':
        hitlist.append(c)
#        print "(",str(c.label)[0:str(c.label).index('-')], ",", str(c.label)[str(c.label).index('-')+1:], ")",


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

v=plist[1]
indexneighbours(v)

def onelist(): #make an index of all neighbours of vertics with rhs label = 1
    for c in plist:
        if str(c.label)[str(c.label).index('-')+1:] == '1':
            indexneighbours(c)

onelist()        
#print neighbours

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
