import string
from graph import *


class element(object): #reduced word 
    def __init__(self,word):
       self.word = word
       
    def freely_reduce(self): 
        i=0
	while i<len(self.word)-1:
		if (self.word[i]==self.word[i].lower() and self.word[i].upper()==self.word[i+1]) or (self.word[i]==self.word[i].upper() and self.word[i].lower()==self.word[i+1]):
			self.word = self.word[:i]+self.word[i+2:]
			if i>0: i-=1
		else:
			i+=1
	return self.word
    
    def inverse(self): #inverse of word, not necessarily reduced
	return ''.join([c.upper() if c==c.lower() else c.lower() for c in self.word[::-1]])


class free_group(object):
    def __init__(self, rank, alpha): # alpha = "alpha", or a single alpanumeric letter 
        self.rank = rank
        self.alpha = alpha
        self.gens =[]
        self.GENS =[]
        self.mongens =[]
        self.Alph =  string.ascii_lowercase
                
    def make_gens(self): #make generators and their inverses (a and A or x1 and X1
        for x in range(0, self.rank):
             if self.alpha == "alpha":
                self.gens.append(self.Alph[x])
                self.GENS.append(self.Alph[x].upper())
             else:
                self.gens.append(self.alpha.lower()+str(x+1))
                self.GENS.append(self.alpha.upper()+str(x+1))
             
             self.mongens = self.gens + self.GENS
             
    def is_element(self,word): #test is word is written in X union X^{-1}
        i = 1
        for c in word:
            if not (c in self.mongens):
              i = 0
            
        if i == 0:
            print("Warning word", word, "is not in the free group")

        return(i) # i = 0 if word is not in given gens


class subgroup(object): #subgroup of freegroup, given by a set of generators, mapped to a set of generators of a free group of rank = rank of subgroup
   def __init__(self, name, subgp_gens, basis=None):
       self.name = name
       self.subgp_gens = subgp_gens
       self.flower = Graph(rooted=True,label= self.name)
       self.coherent = True
       
       if basis is None:
          self.basis =[]
       else:
          self.basis = basis
          
       if not self.basis == []:
          if not len(self.basis) == len(self.subgp_gens):
             print("number of generators of subgroup", len(self.subgp_gens),
                   "not equal to rank of basis", len(self.basis))
             self.coherent = False

   def make_flower(self): #flower automaton for given generators
       for w in self.subgp_gens:
          if not self.basis ==[]:
             i_w = self.subgp_gens.index(w)
             v = self.basis[i_w]
          else:
             v = None 

          print(v)
          self.flower.addLoop(self.flower.root,w)

       return(self.flower)

   def stallings(self): #stallings automaton for given generators
       go = True
       R=self.make_flower()
       while go:
          go = R.fold()

   
   

class bfs_plain(object): # breadth first search of given connected graph to return, with each vertex its distance from the given root
    #its parent and the time it was added to the tree
    def  __init__(self, graph):#this must be a rooted graph
        self.graph = graph
        self.root = self.graph.root
        
    def tree(self):
        i = 1
        q = []
        N = {}
        for v in self.graph.vertices:
            v.colour = 0
            N[v]=[]
            for x in itertools.chain(v.outedges.values(),v.inedges.values()):
                for y in x:
                    if not (y in N[v]):
                        N[v].append(y)
                
        v =self.root    
        v.colour = 1
        v.length = 0
        v.time = i
        v.parent = v
        q.append(v)
        while q:
            u=q[0]
            for x in N[u]:
                if x.colour == 0:
                    i += 1
                    x.colour = 1
                    x.parent = u
                    x.length = u.length + 1
                    x.time = i
                    q.append(x)
               
            q.pop(0)
                    

class bfs(object): # breadth first search of given (possibly disconnected) graph to return, with each vertex its
    #connected component, its distance from the root of its connected component
    #its parent, the time it was added to the forest
    #and the label of the path back to the root
    #for a graph and a list of vertices L of this graph it will select the root of a conn comp C to be the
    #first element of L which is in C
    def  __init__(self, graph, vertices=None):#this must be a graph and a list of its vertices; so far the version with the list of vertices has not been tested
        self.graph = graph
        self.root = self.graph.root
        if vertices is None:
           self.vertices = self.graph.vertices
           self.root = self.graph.root
        else:
           self.vertices = vertices
           self.root = self.vertices[0]
        
    def forest(self):
        i = 0 #time a vertex is added
        q = [] #queue of vertices to be processed within a connected component
        N = {} #dictionary of adjacent edges to a vertex
        for v in self.vertices:
           v.colour = 0 #colour is synonomous with connected component. Here is is initialised
           N[v]=[]
           for (a,b) in v.outedgesList: 
              N[v].append((a,b))
              
           for (a,b) in v.inedgesList:
              N[v].append((a.swapcase(),b))

        Nout = list(self.vertices) #list of all vertices. When a vertex is added to a tree it is removed from this list
        c = 0
        while Nout:
           c += 1
           i += 1
           v =Nout[0]
           Nout.remove(v)
           v.colour = c
           v.length = 0
           v.time = i
           v.parent = v
           v.path =""
           q.append(v)
           while q:
              u=q[0]
              for (a,b) in N[u]:
                 if b.colour == 0:
                    i += 1
                    b.colour = c
                    b.parent = u
                    b.length = u.length + 1
                    b.time = i
                    b.path =u.path + a
                    q.append(b)
                    Nout.remove(b)
                    
              q.pop(0)

class normal_form(object): # write a word in double coset normal form with respect to a given folding of a subgroup
     def  __init__(self, graph, word):#graph is a stallings folding
        self.graph = graph
        self.word = element(word).freely_reduce()

     def acc_read_rem(self):
        Apref=""
        Rpref=""
        suffix=self.word
        u=self.graph.root
        #print("u.out.keys", u.outedges.keys())
        #print("suff 0", suffix[0])
        while len(suffix)>0 and (suffix[0] in u.outedges.keys() or suffix[0].swapcase() in u.inedges.keys()):
           if suffix[0] in u.outedges.keys():
              #print("why", u.outedges[suffix[0]])
              #print("u keys",u.outedges.keys())
              #print("u oulist", u.outedgesList)
              for x in u.outedgesList:
                 #print x[0]
                 #print x[1].outedgesList
                 if suffix[0] == x[0]:
                   u=x[1]
                   
           if suffix[0].swapcase() in u.inedges.keys():
              for x in u.inedgesList:
                 #print x[0]
                 #print x[1].inedgesList
                 if suffix[0].swapcase() == x[0]:
                   u=x[1]

           Rpref=Rpref+suffix[0]
           if u==self.graph.root:
              Apref=Apref+Rpref
              Rpref=""
              
           #print("u outedges", u.outedges)
           #print("u at end of loop", u)
                         
           suffix = suffix[1:]
           #print("fff",suffix)
               
        return(Apref,Rpref,suffix,u)

#######################################################
                                
F1=free_group(3,"alpha")
G=free_group(2,"alpha")
h1="aaa"
h2="bcB"
h3="abc"
w="abBbA"
y="abbBA"
v=["b1","B1","b1","B2"]
F1.make_gens()
X=F1.mongens
print(X)
#F.is_element(v)
print(F1.is_element(h1))
#F.is_element(w)
print(F1.is_element(h2))
print("now G\n")
G.make_gens()
Y=G.mongens
print(Y)
G.is_element(v)
G.is_element(w)
H1=subgroup("H1",[h1,h2,h3],["u","v","w"])
print(H1.coherent)
GH=H1.make_flower()
print(GH.vertices[0].outedgesList)
print(GH.vertices[0].outedges)
print("now H2")
H2=subgroup("H2",[h1,h2,h3],)
print(H2.coherent)
H2.make_flower()
#R=H.flower
#print "digraph H.flower {"
#print (str(R))
#print "}"
#
#go = True
#while go:
# go = R.fold()
#
#S=R
print("now H1 stallings")
H1.stallings()
S=H1.flower
print "digraph H1.stallings {"
print (str(S))
print "}"


#z1=S.addVertex("z1")
#z2=S.addVertex("z2")
#S.addVertex("z3")
#S.addVertex("z4")
#z5=S.addVertex("z5")
#S.addEdge(z2,z1,'r')
#S.addEdge(z2,z5,'s')

T=bfs(S,)
print(id(T))
N=T.forest()
for v in S.vertices:
  print("S vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)

D= S.double()
print "digraph SxS {"
print (str(D))
print "}"

DB=bfs(D,sorted(D.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
DF=DB.forest()
for v in D.vertices:
  print("D vertex", v, "parent", v.parent, "colour", v.colour, "len, time, path", v.length,v.time, v.path)
print "digraph H1.stallings {"
print (str(S))
print "}"
print("h1", h1)
NF=normal_form(S,"aaaAabcBCBaaaaCaaa")


B3=NF.acc_read_rem()
print("acc, read, rem, final vertex read", B3)
q1=element(B3[2])
q=element(q1.freely_reduce())
Q=q.inverse()
print(Q)
B4=normal_form(S,Q)
B5=B4.acc_read_rem()
print("acc, read, rem, final vertex read", B4.acc_read_rem())
y1=element(B3[3].path)
y=y1.freely_reduce()
z1=element(B5[3].path)
z=z1.freely_reduce()
Z=z1.inverse()
Y=y1.inverse()
print("y path, y inverse", y, Y)
print("z path, z inverse", z, Z)
a1=element(B3[0]+B3[1]+Y)
a=a1.freely_reduce()
print(a)
e1=element(B5[2])
e=e1.inverse()
b1=element(y+e+Z)
b=b1.freely_reduce()
print(b)
t1=element(B5[1])
t=t1.freely_reduce()
T=t1.inverse()
g1=element(B5[0])
G=g1.inverse()
c1=element(z+T+G)
c=c1.freely_reduce()
print(c)
