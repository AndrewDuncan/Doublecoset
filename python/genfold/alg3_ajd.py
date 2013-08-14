from alg2_2 import * #names and imports changed to remove dependency issues, will be returned to normal later
from input_ajd import * #temporary, will eventually be included in the above import
import copy

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

def d1_alt2(delta,F,Z): #still has problems, but is in general nicer code than d1 and should work better once completed
	#delta_10=Graph(False,'Delta\' 1,0')
	#delta_20=Graph(False,'Delta\' 2,0')
	delta_k0=[]
	delta_z=Graph(False,'Delta Z')
	vlabs=[]
	#delta_z.vertices=copy.deepcopy(delta.vertices)
#	for i in range(0,len(delta.vertices)):
#		j='vz'+str(i)
#		vlabs.append(j)
	for k in (1,2):
		delta_k0k=copy.deepcopy(delta)
		for v in delta_k0k.vertices[::-1]: #part a
			for label,w in v.outedgesList[::-1]:
				if label in F[2-k].mongens:
					#w=outedges[1]
					v.removeOutEdge(label,w)
					w.removeInEdge(label,v)
			for label,w in v.inedgesList[::-1]:
				if label in F[2-k].mongens:
					#w=inedges[1]
					v.removeInEdge(label,w)
					w.removeOutEdge(label,v)
		#print("vertices of delta k0k", delta_k0k.vertices)
		shoots=1
		while shoots!=0:
			ind=0
			for v in delta_k0k.vertices[::-1]: #part b
				print("k is ", k, " v name, v label ", v.name, v.label)
				edgesList=v.inedgesList+v.outedgesList
				v_in_delta_z=0
				for u in delta_z.vertices:
							if v.label==u.label:
								v_in_delta_z=1# set this flag to 1 if v is already in delta_z
								vcopy=u
				if len(edgesList)==1:
					#print(edgesList)
					if edgesList[0][0] in Z.mongens:
						ind+=1
						print("ind is ", ind)
						print("we found an edge to remove:", edgesList[0])
						vv_in_delta_z=0
						for u in delta_z.vertices:
							if edgesList[0][0]==u.label:
								vv_in_delta_z=1# set this flag to 1 if the other end of this edge is already in delta_z
								vvcopy=u

						if v_in_delta_z==0:
							vcopy=delta_z.addVertex(v.name)
							vcopy.label=v.label
							print("v looks like",v.label,v.name)
							print("vcopy looks like",vcopy.label,vcopy.name)
							v_in_delta_z=1
							print("k is", k, " added vertex v", vcopy.label)
						if vv_in_delta_z==0:
							vv=edgesList[0][1]
							#vv_name=edgesList[0][1].name
							#vv_label=edgesList[0][1].name
							vvcopy=delta_z.addVertex(vv.name)
							vvcopy.label=vv.label
							print("k is", k, " added vertex vv with label and name", vvcopy.label, vvcopy.label)
							vv_in_delta_z=1
					
						if len(v.inedgesList)==1:
							print("k is ", k,"v is ", v," inedges are", v.inedgesList, "outedges are ",v.outedgesList)
							if len(vcopy.inedgesList)>0:	
								if edgesList[0][0]==vcopy.inedgesList[0][0]:
									print("equal")
								else:
									print(">>>>")
								if edgesList[0][1].label==vcopy.inedgesList[0][1].label:
									print("equal again")
								else:
									print(">>>><<<<<<<")	
							if (edgesList[0][0],edgesList[0][1]) in vcopy.inedgesList:
								print("nothing to do")
							else:
								print("adding edge , edgesList[0] is ",edgesList[0],
									  "vcopy.inedgesList is ", vcopy.inedgesList)
								delta_z.addEdge(vvcopy,vcopy,edgesList[0][0])
								print("k is", k, "vcopy,vvcopy=", vcopy,vvcopy, " added edge vv to v with label", edgesList[0][0])
						elif len(v.outedgesList)==1:
							if edgesList[0] in vcopy.outedgesList:
								print("nothing doing")
							else:
								print("adding edge , edgesList[0] is ",edgesList[0],
									  "vcopy.outedgesList is ", vcopy.outedgesList)
								delta_z.addEdge(vcopy,vvcopy,edgesList[0][0])
								print("k is", k, "vcopy,vvcopy=", vcopy,vvcopy, " added edge v to vv with label", edgesList[0][0])
						else:
							print("something is wrong in alg3_alt2 at vertex v", v)
						#delta_z.addEdge(vcopy,vvcopy,edgesList[0][0])
						#addEdge(delta_z,v,edgesList[0][1],edgesList[0][0])
						#problems start here
						print("vcopy.inedgesList is ",vcopy.inedgesList)
						print("vcopy.outedgesList is ",vcopy.outedgesList)
						print("vvcopy.inedgesList is ",vvcopy.inedgesList)
						print("vvcopy.outedgesList is ",vvcopy.outedgesList)
						label=edgesList[0][0]
						w=edgesList[0][1]
						if (label,w) in v.inedgesList:
							#delta_k0[k-1].removeEdge(v.label,edgesList[0][1],edgesList[0][0])
							v.removeInEdge(label,w)
							w.removeOutEdge(label,v)
						else:
							v.removeOutEdge(label,w)
							w.removeInEdge(label,v)
						#removeEdge(delta_k0k,v,edgesList[0][1],edgesList[0][0])
						#delta_k0k.removeVertex(v)

			shoots=ind
		for v in delta_k0k.vertices[::-1]:
			if len(v.inedgesList)+len(v.outedgesList)==0:
				delta_k0k.removeVertex(v)
		for v in delta_k0k.vertices:
			v.nu_im=('{v}') #part d
			v.label='({0},{1})'.format(v.label,k) #part c		
		delta_k0.append(delta_k0k)
	#for v in delta_z.vertices[::-1]:
	#	if len(v.inedgesList)+len(v.outedgesList)==0:
	#		delta_z.removeVertex(v)
	print('digraph k0 {')
	print(str(delta_k0[0]))
	print('}')
	print('digraph k1 {')
	print(str(delta_k0[1]))
	print('}')
	print('digraph Z {')
	print(str(delta_z))
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

def d3(deltap_k1):
	delta_k1=[]
	for k in (1,2):
		delta_k1.append(bfs(deltap_k1[k-1],sorted(double1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]])))
		delta_k1[k-1].forest
		for g in bfs[k-1].graph.components:
			g.stallings()
	return delta_k1

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
