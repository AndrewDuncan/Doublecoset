#Theta 4 x Gamma1 
import copy
from graph import *
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#First copy Theta 4 (run it again)
K=Graph(rooted=True)
K.addLoop(K.root,'bCaySrtxzAB')
K.addLoop(K.root,'yyxacaXyrSXYZYA')
K.addLoop(K.root,'zYY')

while K.fold() is True:
    K.fold()

xlist=[]
for i in range(4,9):
    xlist.append(K.vertices[i])

for i in range(16,23):
    xlist.append(K.vertices[i])

for v in xlist:
    K.removeVertex(v)

vlist=K.vertices
#print vlist

z1=K.addVertex()
z2=K.addVertex()
z3=K.addVertex()
z4=K.addVertex()
z5=K.addVertex()
K.addEdge(vlist[0],z1,'b')
K.addEdge(vlist[5],z2,'b')
K.addEdge(vlist[6],z3,'b')
K.addEdge(z1,z2,'c')
K.addEdge(z2,z3,'c')
K.addEdge(vlist[6],z4,'a')
K.addEdge(vlist[7],z5,'A')
K.addEdge(z4,z5,'a')
K.addPath(vlist[0],vlist[6],'abc')

while K.fold() is True:
    K.fold()

vlist=K.vertices

#add new paths as necessary
K.addPath(vlist[8],vlist[14],'X')

while K.fold() is True:
   K.fold()
    
K.addPath(vlist[11],vlist[6],'yb')
K.addPath(vlist[12],vlist[0],'Za')
K.addPath(vlist[12],vlist[11],'ZxA')
K.addPath(vlist[15],vlist[8],'xA')
K.addPath(vlist[15],vlist[6],'Xa')
K.addPath(vlist[15],vlist[13],'XzC')
K.addPath(vlist[0],vlist[2],'Yb')
K.addPath(vlist[13],vlist[5],'Za')


while K.fold() is True:
   K.fold()

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


P=K.product(G)

plist=P.vertices # list of vertices of P
for c in plist:
    print "(",str(c.label)[0:str(c.label).index('-')], ",", str(c.label)[str(c.label).index('-')+1:], ")",

print  "\n --------------------------------\n"

hitlist = []
for c in plist:
    if str(c.label)[str(c.label).index('-')+1:] == '1':
        hitlist.append(c)
#        print "(",str(c.label)[0:str(c.label).index('-')], ",", str(c.label)[str(c.label).index('-')+1:], ")",

print hitlist
#for i in range(len(plist)):
#    for j in range(i+1,len(plist)):
#        print  i, j,
#print  "\n --------------------------------\n"

#for c in plist:
#    if str(c.label)[str(c.label).index('-')+1:] == '1':
#        print str(c.inedges)
#        print "\n ***\n"
#        print str(c.inedgesList)
#        print "\n ***************************\n"
        



def allneighbours(v): #return all edges incident to a given vertex
    neighbourList = [] # a list of all edges incident to a given vertex
    for e in v.inedgesList:
        neighbourList.append((e,'in')) #append in edges
       
    for e in v.outedgesList:
        neighbourList.append((e,'out')) #append outedges
    return neighbourList

v=0
nl = allneighbours(plist[v])

print "\n and now "
print nl

for i in range(len(nl)): #run through the list of neighbours of a  vertex
    l=str(nl[i][0][1].label) #l is the label of the vertex
    print l
    left = l[0:l.index('-')]            #left is the lhs of the label: from theta-n
    print left
    right = l[l.index('-')+1:]          #right is the rhs of the label: from gamma-k
    print right
    L=str(nl[i][0][0])       #L is the edge label
    d=str(nl[i][1])
    if d == 'out':
        Q = L.capitalize()              #Q is the label taking direction into account
        print Q
    else:
        Q = L
        print Q

neighbours = dict()        
Z=allneighbours(plist[0])
n = str(plist[0].label)
print "here is " 
#neighbours[n]=[Z]
#print neighbours
#neighbours[n].append('dfd')
#neighbours['2-2']=['aaa']
#print neighbours
#print n in neighbours 

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

v=plist[0]
#print v.label in neighbours
nl = neighbours[v.label]
#print nl
#print nl[0]
for i in range(len(nl)): #run through the list of neighbours of a  vertex
    l=str(nl[i][0][1].label) #l is the label of the vertex
#    print l
    left = l[0:l.index('-')]            #left is the lhs of the label: from theta-n
#    print left
    right = l[l.index('-')+1:]          #right is the rhs of the label: from gamma-k
#    print right
    L=str(nl[i][0][0])       #L is the edge label
    d=str(nl[i][1])
    if d == 'out':
        Q = L.capitalize()              #Q is the label taking direction into account
#        print Q
    else:
        Q = L
#        print Q

    
    for k in range(1,len(hitlist)): #run through the vertices in hitlist with bigger index than v
        w = hitlist[k]              #w is the kth on the list
        kl=  neighbours[w.label]    #kl is the list of vertices incident to w
        for j in range(len(kl)): #run through the list of neighbours of   vertex w
            kl_l = str(kl[j][0][1].label) #kl_l is the label of the jth vertex of kl
            kleft = kl_l[0:kl_l.index('-')] #left is the lhs of the label of the jth vertex of kl
            if left == kleft: #when left = kleft a path might be added to theta4
                print "left is ", left, "kleft is", kleft
#if left == 
#       print "v is ", v.label, "l is",   l, "k is ", k, "kl is", kl
         
#len(Z)
#for s in range(len(Z)):
#    if not q in neighbours:
#        neighbours[q]=['afa']
#    else:
#        neighbours[q].append('fff')

#indexneighbours(plist[0])
#      neighbours[q] = [n]
# elif not n in neighbours[q]:
#    neighbours[q].append(n)

#    for i in range(len(nl)): #run through the list of neighbours 
#       l=str(nl[i][0][1].label) #l is the label of the vertex i of the list
#      left = l[0:l.index('-')]            #left is the lhs of the label: from theta-n
#     right = l[l.index('-')+1:]          #right is the rhs of the label: from gamma-k
#    L=str(nl[i][0][0])       #L is the edge label
#   d=str(nl[i][1])
# if d == 'out':
#      Q = L.capitalize()              #Q is the label taking direction into account
#  else:
#     Q = L
#neighbours(plist[1])
           

    
#print "digraph P {"
#print (str(P))
#print "}"

