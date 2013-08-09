from alg2_2 import * #names and imports changed to remove dependency issues, will be returned to normal later
from input_ajd import * #temporary, will eventually be included in the above import

def alg3_pre():
	print('For the first free group:')
	F1=enter_free_group()
	print('For the second free group:')
	F2=enter_free_group()
	F=(F1,F2)
	print('For the first subgroup:')
	H1=enter_subgroup()
	print('For the second subgroup:')
	H2=enter_subgroup()
	(flower1,double1,forest1)=alg2_pre(H1)
	(flower2,double2,forest2)=alg2_pre(H2)
	H=(H1,H2)
	if F1.rank>F2.rank:
		Z=free_group(F1.rank,'z')
	else:
		Z=free_group(F2.rank,'z')
	return F,Z,H1,H2,flower1,double1,forest1,flower2,double2,forest2

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

def d1_alt(delta,F,Z): #still has a few problems, but is in general nicer code than d1 and should work better once completed
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
		for v in delta_k0[k-1].vertices: #part b
			ind=0
			while shoots!=0:
				edgesList=v.inedgesList+v.outedgesList
				if len(edgesList)==1:
					print(edgesList)
					ind+=1
					print(ind)
					delta_z.addEdge(v,edgesList[0][1],edgesList[0][0])
					#delta_z.addEdge(edgesList[0][0],edgesList[0][1],edgesList[0][2],edgesList[0][3])
					#problems start here
					delta_k0[k-1].removeEdge(v,edgesList[0][1],edgesList[0][0])
				shoots=ind
	for k in (1,2):
		for v in delta_k0[k-1].vertices:
			v.nu_im=('{v}') #part d
			v.label='({0},{1})'.format(v.label,k) #part c
	return delta_k0,delta_z

def d2(delta_k0):
	deltap_k1=[delta_k0[0],delta_k0[1]]
	for k in (1,2):
		for v in delta_k0[k-1].vertices:
			for outedges in v.outedgesList:
				deltap_k1[k-1].addPath(v,outedges[1],phi(outedges[0]))
		for v in deltap_k1[k-1].vertices:
			if v not in delta_k0[k-1]:
				v.nu_im=('{v}')
	return deltap_k1

def d3(deltap_k1):
	delta_k1=[]
	for k in (1,2):
		delta_k1.append(bfs(deltap_k1[k-1],sorted(double1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]])))
		delta_k1[k-1].forest
		for g in bfs[k-1].graph.components:
			g.stallings()
	return delta_k1
