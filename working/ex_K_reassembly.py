import copy
from graph import *

#input F_1 component
import ex_K
ex = ex_K
#edge labels: a=x1, b=x2, c=x3, r=y1,s=y2, t=y3, x=z1,y=z2,z=z3
#First copy Theta 1 (run it again)

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
#print vlist

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

vlist = ex.K.vertices

#now make theta-5
z6=ex.K.addVertex()
z7=ex.K.addVertex()
z8=ex.K.addVertex()
z6.label = 48
z6.name = 48
z7.label = 49
z7.name = 49
z8.label = 45
z8.name = 45

ex.K.addEdge(z6,z7,'a')
ex.K.addEdge(z6,z7,'a')
vlist = ex.K.vertices


ex.K.addEdge(z6,vlist[2],'z')
ex.K.addEdge(z7,vlist[23],'y')
ex.K.addEdge(z8,vlist[23],'a')
ex.K.addEdge(z8,vlist[1],'z')
ex.K.addEdge(vlist[11],vlist[13],'y')

while ex.K.fold() is True:
   ex.K.fold()


#Input first F_2 component
I=Graph(rooted=True,label='I')
I.addLoop(I.root,'bCaySrtxzAB')
I.addLoop(I.root,'yyxacaXyrUXYZYA')
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

I.addPath(vlist[0],vlist[1],'sX')

while I.fold() is True:
   I.fold()

#input 2nd F_2 component
J=Graph(rooted=True,label='J')
J.addLoop(J.root,'bCaySrtxzAB')
J.addLoop(J.root,'yyxacaXyrUXYZYA')
J.addLoop(J.root,'zYY')

while J.fold() is True:
    J.fold()

 

y2list=[]
for i in range(-4,17):
    y2list.append(J.vertices[i])

for v in y2list:
    J.removeVertex(v)

vlist=J.vertices

J.addPath(vlist[1],vlist[2],'Yt')

while J.fold() is True:
   J.fold()


Z=Graph(label='Z') #Z edges to be added back in reassembly
z18=Z.addVertex()
z22=Z.addVertex()
z24=Z.addVertex()
z9=Z.addVertex()
Z.addPath(z22,z24,'YZ')


Xlist = ex.K.vertices 
Y1list = I.vertices
Y2list = J.vertices
#Zlist = Z.vertices
#i = 0
#elist=Zlist
#for i in range(len(elist)):
#    print "(", i, ",",elist[i], ")",


#u=Xlist[3]
#v=Y1list[0]
#l='y'
joinList=[('K',Xlist[3],'I',Y1list[0],'y'),
          ('Z',z18,'K',Xlist[10],'x'),
          ('Z',z18,'J',Y2list[0],'y'),
          ('Z',z22,'J',Y2list[2],'x'),
          ('K',Xlist[11],'Z',z24,'y'),
          ('I',Y1list[3],'Z',z9,'x'),
          ('Z',z9,'K',Xlist[4],'z')]

out=[]

#print "\n items", u.outedges.items(), "\n in", u.inedges, "list in", u.inedgesList

#out.append('"%s%s" [label="%s",fontsize=7,width=.01,height=.01];' % (name1,u,u.name))
#out.append('"%s%s" [label="%s",fontsize=7,width=.01,height=.01];' % (name2,v,v.name))
for e in joinList:
    out.append( '"%s%s" -> "%s%s" [label="%s",fontsize=8];' % e) #(nameX,u,nameY1,v,l) )

ident = '\n'.join(out)
#print  "\n", ident

print "digraph R {"
print '\n'.join([(str(ex.K)),(str(I)),(str(J)),(str(Z)),(str(ident))])
print "}"

