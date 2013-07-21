import string
from graph import *


class element(object): #reduced word 
	def __init__(self,word):
		self.word = word
		i=0
		while i<len(self.word)-1:
			if (self.word[i]==self.word[i].lower() and self.word[i].upper()==self.word[i+1]) or (self.word[i]==self.word[i].upper() and self.word[i].lower()==self.word[i+1]):
				self.word = self.word[:i]+self.word[i+2:]
				if i>0: i-=1
			else:
				i+=1

	def inverse(self): #inverse of word, not necessarily reduced
		return [c.upper() if c==c.lower() else c.lower() for c in self.word[::-1]]


class free_group(object):
	def __init__(self, rank, alpha): # alpha = "alpha", or a single alpanumeric letter 
		self.rank = rank
		self.alpha = alpha
		self.gens =[]
		self.GENS =[]
		self.mongens =[]
		self.Alph =  string.ascii_lowercase
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
            
		#if i == 0:
		#	print("Warning word", word, "is not in the free group")

		return(i) # i = 0 if word is not in given gens


class subgroup(object): #subgroup of freegroup, given by a set of generators, mapped to a set of generators of a free group of rank = rank of subgroup
	def __init__(self, name, subgp_gens, basis=None):
		self.name = name
		self.subgp_gens = subgp_gens# original generators 
		self.flower = Graph(rooted=True,label= self.name)
		self.coherent = True
		self.subgp_free_gens=[] #free generators to be constructed from stallings folding

		if basis is None: #basis of free group isomorphic to subgroup
			self.basis =[]
		else:
			self.basis = basis
          
		if not self.basis == []:
			if not len(self.basis) == len(self.subgp_gens):
				print("number of generators of subgroup", len(self.subgp_gens),
                   "not equal to rank of basis", len(self.basis))
				self.coherent = False

		for w in self.subgp_gens: # creates flower automaton for given generators
			if not self.basis ==[]:
				i_w = self.subgp_gens.index(w)
				v = self.basis[i_w]
			else:
				v = None 

			#print(v)
			self.flower.addLoop(self.flower.root,w,v)

	def stallings(self): #stallings automaton for given generators
		go = True
		R=self.flower
		while go:
			go = R.fold()

   


class bfs(object): # breadth first search of given (possibly disconnected) graph to return, with each vertex its
    #connected component, its distance from the root of its connected component
    #its parent, the time it was added to the forest
    #and the label of the path back to the root
    #for a graph and a list of vertices L of this graph it will select the root of a conn comp C to be the
    #first element of L which is in C
	def  __init__(self, graph, vertices=None):#this must be a graph and a list of its vertices.
		self.graph = graph
		self.root = self.graph.root
		if vertices is None:
			self.vertices = self.graph.vertices
			self.root = self.graph.root
		else:
			self.vertices = vertices
			self.root = self.vertices[0]
		self.components=self.graph.components
        
	def forest(self):
		i = 0 #time a vertex is added
		q = [] #queue of vertices to be processed within a connected component
		N = {} #dictionary of adjacent edges to a vertex
		for v in self.vertices:
			v.colour = 0 #colour is synonomous with connected component. Here is is initialised
			N[v]=[]
			for (a,b) in v.outedgesList: 
				N[v].append((a,b,"+")) #record + for outedges
              
			for (a,b) in v.inedgesList:
				N[v].append((a.swapcase(),b,"-"))#record - for inedges

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
			v.path =[]
			self.graph.components[c]=v
			#print("components are now", self.graph.components)
			q.append(v)# add v to the end of the queue
			while q:
				u=q[0] # for the first element u of the queue
				for (a,b,d) in N[u]: #and all edges incident to u, with label a to vertex b (and in/out indicator c) 
					if b.colour == 0: # if b is not already in a component 
						i += 1         #increase time by 1 
						b.colour = c   #put b in the current component
						b.parent = u   #make u the parent of b
						b.length = u.length + 1 #make the distance of b from the root one more than the distance of u
						b.time = i     # time b was added
						b.path =u.path + [a] # path from the root to b
						if d=="-":
							u.inedges_write[(a.lower(),b)]=""#make the write-label of the inedge u <- b equal to 1
							b.outedges_write[(a.lower(),u)]=""#and  the write-label of the outedge b-> u equal to 1
						else:
							u.outedges_write[(a.lower(),b)]=""#make the write-label of the outedge u -> b equal to 1
							b.inedges_write[(a.lower(),u)]=""#and  the write-label of the inedge b-> u equal to 1
						q.append(b)    # add b to the end of the queue 
						Nout.remove(b) # remove b from the list of all vertices
                    
				q.pop(0) # remove the first element of the queue

class graph_pass(object):  #read word from left to right finding max accepted prefix, them max readable prefix and
        #outputing these along with the remaining suffix, and the output labels of the path read
	def  __init__(self, graph, word):#graph is a stallings folding
		self.graph = graph
		self.word = element(word).word
		self.vertex = None

	def acc_read_rem(self): #read word from left to right finding max accepted prefix, them max readable prefix and
        #outputing these along with the remaining suffix, and the output labels of the path read
		Apref=[]
		Rpref=[]
		Apref_in_Z=[]
		suffix=self.word
		u=self.graph.root
		#print("u is the root of the graph passed to acc_read_rem and is ",u)
		z=""
		#print("u, u.out.keys, u.outedges", u,u.outedges.keys(),u.outedges)
		#print("u, u.in.keys, u.inedges", u,u.inedges.keys(),u.inedges)
		#if suffix==[]:
			#print ("suffix is empty")
		#else:
			#print("suff 0 and swapcase", suffix[0], suffix[0].swapcase())		
		while len(suffix)>0 and (suffix[0] in u.outedges.keys() or suffix[0].swapcase() in u.inedges.keys()):
			#print("suff 0 and swapcase", suffix[0], suffix[0].swapcase())
			#print("u, u.out.keys, u.outedges", u,u.outedges.keys(),u.outedges)
			#print("u, u.in.keys, u.inedges", u,u.inedges.keys(),u.inedges)
			if suffix[0] in u.outedges.keys():
				#print("u.outedges[suffix[0]] ", u.outedges[suffix[0]])
				#print("u.outedges.keys ",u.outedges.keys())
				#print("u outedgeslist ", u.outedgesList)
				#print("u outedges_write", u.outedges_write)
				for x in u.outedgesList:
					#print("x[0] ", x[0])
					#print("x[1].outedgeslist ", x[1].outedgesList)
					if suffix[0] == x[0]:
						z=u.outedges_write[(suffix[0].lower(),x[1])]
						#print("suffix[0]==x[0] and z=", z)
						u=x[1]
						break
                   
                   
			if suffix[0].swapcase() in u.inedges.keys():
				for x in u.inedgesList:
					#print("x[0] ", x[0])
					#print("x[1].inedgeslist ",x[1].inedgesList)
					if suffix[0].swapcase() == x[0]:
						z=u.inedges_write[(suffix[0].lower(),x[1])].upper()
						#print("suffix[0].swapcase()==x[0] and z=", z)	
						u=x[1]
						break

			Rpref=Rpref+[suffix[0]]
			if z!="":
				Apref_in_Z.append(z)

			if u==self.graph.root:
				Apref=Apref+Rpref
				Rpref=[]
              
			#print("all stuff",Apref,Rpref,Apref_in_Z,u)
              
			#print("u outedges ", u.outedges)
			#print("u at end of loop ", u)
                         
			suffix = suffix[1:]
			#print("suffix ",suffix)
               
		return(Apref,Rpref,suffix,u,Apref_in_Z)

class   Normal_form(object): #read word forward, find acc, read, rem, as above, then read inverse to find the same
	def  __init__(self, graph, word,double):#graph is a stallings folding
		self.graph = graph
		self.word = word
		self.word = element(self.word).word
		self.double= double

	def spit_out_nf(self):
		LHS=graph_pass(self.graph,self.word).acc_read_rem()
		#print("the LHS is ",LHS)
		LHS_u=LHS[3].label
		h=element(LHS[0]).word
		p=element(LHS[1]).word
		q=element(LHS[2]).word
		#print(q)
		Q=element(q).inverse()
		RHS=graph_pass(self.graph,Q).acc_read_rem()
		#print("the RHS is ",RHS)
		RHS_u=RHS[3].label
		e=element(RHS[2]).inverse()
		if not e==[]:
			a_Z=element(LHS[4]).word
			y=element(LHS[3].path).word 
			z=element(RHS[3].path).word
			Y=element(y).inverse()
			Z=element(z).inverse()
			a=element(h+p+Y).word
			b=element(y+e+Z).word
			t=element(RHS[1]).word
			T=element(t).inverse()
			G=element(RHS[0]).inverse()
			c=element(z+T+G).word
			C_Z=element(RHS[4]).word
			c_Z=element(C_Z).inverse()
			#print("type 1 nf")
			return([a,b,c,a_Z,c_Z])
		else:
			conn=[]
			repr=[]
			for x in self.double.vertices:
				#print("vertex x of double is ", x)
				#print("LHS_u-RHS_u is ",str(LHS_u)+"-"+str(RHS_u))
				if x.label==str(LHS_u)+"-"+str(RHS_u):
					conn=element(x.path).inverse()
					#child = True 
					#xc = x
					#print("colour of x is ",x.colour)
					xroot=self.double.components[x.colour]
					#print("root of comp of x is ", xroot)
					repr = xroot.parent.label.partition("-")
					#while child:
					#	if xc.parent == xc:
					#		child = False
					#		repr = xc.parent.label.partition("-")
					#		print("root found  and root, repr is", xc, repr)
					#	xc = xc.parent 
               
						# for r in self.double.vertices:
						#    if r.colour == x.colour:
						#       if r.parent == r:
						#          repr = r.parent.label.partition("-")
						#          break
						# print("root found  and root, repr is", r, repr)
						# break
            
					y=[]
					for v in self.graph.vertices:
						if v.label == int(repr[0]):
							y=v.path    
							#print("y is", y)
							break

					z=[]
					for v in self.graph.vertices:
						if v.label == int(repr[2]):
							z=v.path
							#print("z is", z)
							break
               
					Y=element(y).inverse()
					a=element(h+p+conn+Y).word
					a_Z=graph_pass(self.graph,a).acc_read_rem()[4]
					Z=element(z).inverse()
					B=element(RHS[0]+RHS[1]+conn+z).word
					b=element(B).inverse()
					b_Z=graph_pass(self.graph,b).acc_read_rem()[4]
					#print("y,z,conn,RHS[0],RHS[1]", y,z,conn,RHS[0],RHS[1])
					#print("type 2 nf", [a,y+Z, b,a_Z,b_Z])
					return([a,y+Z, b,a_Z,b_Z])


def subgroup_basis(folding): #Find a free generating set for the subgroup H with stallings folding "folding". For this to work a stallings() and bfs() must have been run#folding.subgp_free_gens = []
	fgens = []
	dgens = {}
	for v in folding.vertices: #for each vertex v of the stallings folding of H
		for e in v.outedgesList: #and for each edge e out of v
			if v.outedges_write[e]!="": #if the output label of e is non-trivial (so e is not in the spanning tree) 
				fgens.append([v.path+[e[0]]+element(e[1].path).inverse(),[v.outedges_write[e]]]) #append the generator corresponding to e and its image in Z to the list of free generators
				dgens[v.outedges_write[e]]=v.path+[e[0]]+element(e[1].path).inverse()

	return(fgens,dgens)


def phi(subgroup,zword): #map a word in the free group on the Z generators of subgroup H into a word on the free generators of H in F
	yy=[]
	for i in range(0,len(zword)):
		if zword[i] in subgroup.subgroup_free_gens.keys():#if zword[i] is in the list of keys of genrs of H
			yy.extend(subgroup.subgroup_free_gens[zword[i]])
		elif zword[i].swapcase() in subgroup.subgroup_free_gens.keys():#if zword[i]^-1 is in the list of keys of genrs of H
			yy.extend(element(subgroup.subgroup_free_gens[zword[i].swapcase()]).inverse())
		else:
			print("the word passed to phi contains a letter not in Z:", zword[i]) # otherwise set the error flag to 0 and return 
			return([],0)
		print("in phi for loop with i =", i, "yy is ",yy)
	print("at end of phi yy is", yy)
	return(element(yy).word,1)

	 
