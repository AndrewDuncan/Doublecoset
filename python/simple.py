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
