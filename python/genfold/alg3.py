from alg2 import *
from input_ajd import * #temporary, will eventually be included in the above import

def alg3_pre():
	F1=enter_free_group()
	F2=enter_free_group()
	F=(F1,F2)
	H1=enter_subgroup()
	H2=enter_subgroup()
	(flower1,double1,forest1)=alg2_pre(H1)
	(flower1,double1,forest1)=alg2_pre(H2)
	if F1.rank>F2.rank:
		Z=free_group(F1.rank,'z')
	else:
		Z=free_group(F2.rank,'z')

def d1(delta,F,Z):
	delta_10=Graph(False,'Delta\' 1,0')
	delta_20=Graph(False,'Delta\' 2,0')
	delta_k0=[delta_10,delta_20]
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
		for v in delta_k0[k-1]: #part b
			edgesList=v.inedgesList+v.outedgesList
			if len(edgesList)==1:
				for edge in edgeslist:
					if edge in Z.mongens:
						delta_z.addVertex(v.name)
						if edge in v.inedgesList:
							delta_z.addEdge(edge[0],v,edge[1])
							v.removeOutEdge(edge[0],edge[1])
						elif edge in v.outedgesList:
							addOutEdge(v,edge[0],edge[1])
							v.removeInEdge(edge[0],edge[1])
#		if k==1:
#			delta_k0[1]=delta_k0[0]
		for v in delta_k0[k-1]:
			v.nu_im=('{v}') #part d
			v.label='({0},{1})'.format(v.label,k) #part c
	print(delta_k0[0].graphViz('Delta 1,0'))
	print(delta_k0[1].graphViz('Delta 2,0'))
	print(delta_z.graphViz('Delta Z'))
	return delta_k0, delta_z

def d2(delta_k0):
	(deltap_11,deltap_21)=delta_k0
	deltap_k1=[deltap_11,deltap_21]
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
