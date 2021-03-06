def d1(delta,F,Z):
#	delta_10=Graph(False,'Delta\' 1,0')
#	delta_20=Graph(False,'Delta\' 2,0')
#	delta_k0=[delta_10,delta_20]
	delta_k0=[0,0]
	delta_z=Graph(False,'Delta Z')
	for k in (1,2):
		delta_k0[k-1]=delta
		for v in delta_k0[k-1].vertices: #part a
			for outedges in v.outedgesList:
				if outedges[0] in F[2-k].mongens:
					v.removeOutEdge(outedges[0],outedges[1])
			for inedges in v.inedgesList:
				if inedges[0] in F[2-k].mongens:
					v.removeInEdge(inedges[0],inedges[1])
		for v in delta_k0[k-1].vertices: #part b
			edgesList=v.inedgesList+v.outedgesList
			print(v,edgesList)
			if len(edgesList)==1:
				for edge in edgesList:
					if edge[0] in Z.mongens:
						delta_z.addVertex(v.name)
						if edge in v.inedgesList:
							if v not in delta_z.vertices:
								vv=delta_z.addVertex(v.label)
							else:
								vv=v
							if edge[1] not in delta_z.vertices:
								delta_z.addVertex(edge[1])
							#vv.addInEdge(edge[0],v,edge[1],v.inedges_write['({0},{1})'.format(v.label,edge[1])])
							vv.addInEdge(edge[0],v,edge[1])
							if edge in v.outedgesList:
								v.removeOutEdge(edge[0],edge[1])
						elif edge in v.outedgesList:
							if v not in delta_z.vertices:
								vv=delta_z.addVertex(v.label)
							else:
								vv=v
							if edge[1] not in delta_z.vertices:
								delta_z.addVertex(edge[1])
							#vv.addOutEdge(v,edge[0],edge[1],v.inedges_write['({0},{1})'.format(v.label,edge[1])])
							vv.addOutEdge(v,edge[0],edge[1])
							if edge in v.inedgesList:
								v.removeInEdge(edge[0],edge[1])
		print(str(delta_z))
#		if k==1:
#			delta_k0[1]=delta_k0[0]
		for v in delta_k0[k-1].vertices:
			v.nu_im=('{v}') #part d
			v.label='({0},{1})'.format(v.label,k) #part c
	print(delta_z.vertices)
	print('digraph H {')
	print(delta_k0[0].graphViz('Delta 1,0'))
	print('}')
	print('digraph H {')
	print(delta_k0[1].graphViz('Delta 2,0'))
	print('}')
	print('digraph H {')
	print(delta_z.graphViz('Delta Z'))
	print('}')
	return delta_k0, delta_z

def d1_alt(delta,F,Z): #still has problems, but is in general nicer code than d1 and should work better once completed
	delta_10=Graph(False,'Delta\' 1,0')
	delta_20=Graph(False,'Delta\' 2,0')
	delta_k0=[delta_10,delta_20]
	delta_z=Graph(False,'Delta Z')
	vlabs=[]
	delta_z.vertices=delta.vertices
#	for i in range(0,len(delta.vertices)):
#		j='vz'+str(i)
#		vlabs.append(j)
	for k in (1,2):
		delta_k0[k-1]=delta
		for v in delta_k0[k-1].vertices: #part a
			for outedges in v.outedgesList:
				if outedges[0] in F[2-k].mongens:
					v.removeOutEdge(outedges[0],outedges[1])
			for inedges in v.inedgesList:
				if inedges[0] in F[2-k].mongens:
					v.removeInEdge(inedges[0],inedges[1])
		shoots=1
		while shoots!=0:
			for v in delta_k0[k-1].vertices: #part b
				ind=0
				edgesList=v.inedgesList+v.outedgesList
				if len(edgesList)==1:
					#print(edgesList)
					if edgesList[0][0] in Z.mongens:
						ind+=1
						print(ind)
						print(edgesList[0])
						delta_z.addEdge(v,edgesList[0][1],edgesList[0][0])
						#problems start here
						#delta_k0[k-1].removeEdge(v,edgesList[0][1],edgesList[0][0])
						removeEdge(delta_k0[k-1],v,edgesList[0][1],edgesList[0][0])
				shoots=ind
	for k in (1,2):
		for v in delta_k0[k-1].vertices:
			v.nu_im=('{v}') #part d
			v.label='({0},{1})'.format(v.label,k) #part c
	print('digraph H {')
	#print(str(delta_z))
	print(str(delta_k0[0]))
	print('}')
	return delta_k0,delta_z

def d2(delta_k0):
	deltap_k1=[delta_k0[0],delta_k0[1]]
	for k in (1,2):
		for v in delta_k0[k-1].vertices:
			for outedges in v.outedgesList:
				if edge[0] in Z.mongens:
					deltap_k1[k-1].addPath(v,outedges[1],phi(outedges[0]))
		for v in deltap_k1[k-1].vertices:
			if v not in delta_k0[k-1]:
				v.nu_im=('{v}')
	return deltap_k1

def removeEdge(graph,u,v,label): #to replace the non-working class attribute, at least temporarily
	if label==label.lower():
		u.removeOutEdge(label,v)
		v.removeInEdge(label,u)
	else:
		self.removeEdge(v,u,label.lower())

def addEdge(graph,u,v,label,write=None):
	if write is None:
		write =""
	if label==label.lower():		
		u.addOutEdge(label,v,write.lower())
		v.addInEdge(label,u,write.lower())
	else:
		self.addEdge(v,u,label.lower(),write)
