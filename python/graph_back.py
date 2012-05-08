#Labelled vertex, with labelled edges.
#edges are doubles (label, vertex)
import os
import itertools

class Vertex:
	def __init__(self,label):
		self.label = label
		self.outedges = {}
		self.outedgesList = []
		self.inedges = {}
		self.inedgesList = []

	def __repr__(self):
		return str(self)

	def __str__(self):
		return 'v'+str(self.label)

	#add a labelled edge from v to this vertex
	def addInEdge(self,label,v):
		if (label,v) in self.inedgesList:
			return
		else:
			self.inedgesList.append((label,v))

		if not label in self.inedges:
			self.inedges[label] = [v]
		elif not v in self.inedges[label]:
			self.inedges[label].append(v)

	#remove the edge from v to this vertex with given label
	def removeInEdge(self,label,v):
		self.inedgesList.remove((label,v))
		if label in self.inedges:
			self.inedges[label].remove(v)

	#add a labelled edge from this vertex to v
	def addOutEdge(self,label,v):
		if (label,v) in self.outedgesList:
			return
		else:
			self.outedgesList.append((label,v))

		if not label in self.outedges:
			self.outedges[label] = [v]
		elif not v in self.outedges[label]:
			self.outedges[label].append(v)
	
	#remove the edge from this vertex to v with given label
	def removeOutEdge(self,label,v):
		self.outedgesList.remove((label,v))
		if label in self.outedges:
			self.outedges[label].remove(v)

	#get all possible folds around this vertex
	#returns a list of doubles (label,vs)
	#where label is lower-case if outward edges, upper-case if inward edges
	#vs is the list of vertices that would be merged
	def getFolds(self):
		outfolds = [(label,vs) for label,vs in self.outedges.items() if len(vs)>1]		#for each label, it can be folded if there are at least 2 outward edges with that label
		infolds = [(label.upper(),vs) for label,vs in self.inedges.items() if len(vs)>1]	#ditto for inward edges
		return outfolds+infolds

	#get the neighbouring vertex connected to this one by an edge with the given label
	#returns None if no such edge exists
	def neighbour(self,label):
		if label==label.lower():	#lower case means x, upper case means x^{-1}
			es = self.outedges		#if x, we want an outward edge
		else:
			es = self.inedges		#if x^{-1}, we want an inward edge

		label=label.lower()
		if label in es:				#if there is an edge with the right label in the right direction
			return es[label][0]			#move to the vertex it is pointing to
		else:
			return None				#otherwise, we can't go anywhere, so the word is not in the subgroup
		

#A general graph object
#not necessarily connected
class Graph:
	vertexCount = 0	#accumulator for labelling vertices
	root = None

	#graph constructor
	#if rooted=True, then a root node is created and added to the graph
	#otherwise graph begins empty
	def __init__(self,rooted=False):
		self.vertices = []
		if rooted:
			self.root = self.addVertex()
	
	#create a new vertex in the graph and return it
	def addVertex(self):
		self.vertexCount += 1
		v=Vertex(self.vertexCount)
		self.vertices.append(v)
		return v
	
	#merge vertices u and v, removing v from the graph
	def mergeVertices(self,u,v):
		if u==v: return

		self.vertices.remove(v)
		for label,w in v.outedgesList:		#for each labelled edge v->w
			w.removeInEdge(label,v)			#remove edge from w's list of in-edges
			w.addInEdge(label,u)			#add an edge u->w to w's in-edges
			u.addOutEdge(label,w)			#add "			" to u's out-edges

		for label,w in v.inedgesList:		#for each labelled edge joining w->v
			w.removeOutEdge(label,v)		#remove edge from w's list of out-edges
			w.addOutEdge(label,u)			#add an edge w->u to w's out-edges
			u.addInEdge(label,w)			#add "			" to u's in-edges

		return u							#return the surviving vertex
	
	#add a labelled edge u->v
	#lower-case labels are forwards edges
	#upper-case labels are backwards edges
	def addEdge(self,u,v,label):
		if label==label.lower():		
			u.addOutEdge(label,v)
			v.addInEdge(label,u)
		else:
			self.addEdge(v,u,label.lower())	

	#add a labelled circle rooted at u, so reading round edge labels gives word
	def addLoop(self,u,word):
		root = u
		for c in word[:-1]:				#for each letter in the word:
			v = self.addVertex()		#create a new vertex
			self.addEdge(u,v,c)			#add a labelled edge connecting previous vertex to the new one
			u=v

		self.addEdge(u,root,word[-1])	#add a final edge connecting back to the root, with label the last letter of the word
	
	#fold the graph once
	#that is: any number of vertices might be merged, but each vertex will be merged at most once
	def fold(self):
		folds = sum([v.getFolds() for v in self.vertices],[])	#get all possible folds
		folded = []												#keep track of which vertices have been folded

		for label,vs in folds:							#for each possible fold
			vs = [v for v in vs if not v in folded]		#remove vertices that have been involved in a previous fold
			if len(vs)>1:								#if there are still vertices to be folded
				u=vs[0]									#the first vertex in the list. at the end of the loop, the node pointed to by u is the one that survived
				folded.append(u)						#add u to the list of vertices not to merge again
				for v in vs[1:]:						#for each other vertex v in this fold
					self.mergeVertices(u,v)			#merge it with u, and reassign u to the surviving
					folded.append(v)					#add v to the list of vertices not to merge again

		return len(folds)>0								#return true if any folds took place

	#return double of this graph
	#has a vertex labelled (u,v) for each u,v in original graph
	#there is an edge (u,v) -> (a,b) with label x iff there are an edge u->a with label x and an edge v->b with label x in the original graph
	def double(self):

		def joinName(u,v):	#create a new name for vertices in the double graph so names of original pair can be easily seen
			return str(u.label)+'-'+str(v.label)

		newverts = {}	#a dictionary to keep track of new vertices


		g=Graph()	#g will be the double graph

		for u,v in itertools.product(self.vertices,self.vertices):	#for every ordered pair of vertices
			uv = g.addVertex()			#add a vertex
			uv.label = joinName(u,v)	#give it a name created from the names of the pair of original vertices
			newverts[uv.label] = uv		#add the vertex to the dictionary

		for u,v in itertools.product(self.vertices,self.vertices):	#for every ordered pair (u,v) of vertices
			for label in u.outedges.keys():		#for each label for which u has one or more out-edges
				if label in v.outedges.keys():	#if v has out-edges with the same label
					uv=newverts[joinName(u,v)]	#get the vertex (u,v)
					for a,b in itertools.product(u.outedges[label],v.outedges[label]):	#for each vertex a such that u->a and each b such that v->b,
						g.addEdge(uv,newverts[joinName(a,b)],label)						#create an edge (u,v) -> (a,b)

		return g

	#product of this graph and graph g2
	def product(self,g2):
		def joinName(u,v):	#create a new name for vertices in the double graph so names of original pair can be easily seen
			return str(u.label)+'-'+str(v.label)

		newverts = {}	#a dictionary to keep track of new vertices


		g=Graph()	#g will be the double graph

		for u in self.vertices:	#for every vertex in this graph
			for v in g2.vertices:	#for every vertex in g2
				uv = g.addVertex()			#add a vertex
				uv.label = joinName(u,v)	#give it a name created from the names of the pair of original vertices
				newverts[uv.label] = uv		#add the vertex to the dictionary

		for u in self.vertices:	#for every ordered pair of vertices
			for v in g2.vertices:	#for every vertex in g2
				for label in u.outedges.keys():		#for each label for which u has one or more out-edges
					if label in v.outedges.keys():	#if v has out-edges with the same label
						uv=newverts[joinName(u,v)]	#get the vertex (u,v)
						for a,b in itertools.product(u.outedges[label],v.outedges[label]):	#for each vertex a such that u->a and each b such that v->b,
							g.addEdge(uv,newverts[joinName(a,b)],label)						#create an edge (u,v) -> (a,b)

		return g



	def graphViz(self,name='G'):
		out = []
		for u in self.vertices:
			out.append('"%s%s" [shape=point];' % (name,u))
			for label,vs in u.outedges.items():
				for v in vs:
					out.append( '"%s%s" -> "%s%s" [label="%s"];' % (name,u,name,v,label) )
		return '\n'.join(out)
	
	def __str__(self):
		return self.graphViz('G')

#little demo/test
def _test_():
	g=Graph(rooted=True)
	g.addLoop(g.root,'abAB')
	g.addLoop(g.root,'abC')
	g.addLoop(g.root,'adbC')
	out = '';
	step = 0
	out = g.graphViz('g'+str(step))
	go = True
	while go:
		step += 1
		out = g.graphViz('g'+str(step))
		out = 'digraph {\n%s\n}' % out
		open('test%s.gv' % step,'w').write(out)
		os.system('neato -Tpng test%s.gv > test%s.png' % (step,step))
		go = g.fold()

if __name__=='__main__':
	_test_()
