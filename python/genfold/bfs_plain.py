class bfs_plain(object): # breadth first search of given connected graph to return, with each vertex its distance from the given root
    #its parent and the time it was added to the tree. This version is not used in the current program
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
                    
