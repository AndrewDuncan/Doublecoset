						
	#if len(vcopy.inedgesList)>0:# can probably delete this if and the following if, if, else	
								#if edgesList[0][0]==vcopy.inedgesList[0][0]:
								#	print("equal")
								#else:
								#	print(">>>>")
								#if edgesList[0][1].label==vcopy.inedgesList[0][1].label:
								#	print("equal again")
								#else:
								#	print(">>>><<<<<<<")	


def d3(deltap_k1): #input delta_k1,  both components - not sure what this is doing- the output above appears to be folded already, so this d3 seems to be redundant
	delta_k1=[]
	for k in (1,2):
		deltap_k1k=copy.deepcopy(deltap_k1[k-1]) #why?
		delta_k1.append(bfs(deltap_k1[k-1],sorted(double1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]])))# add bfs to delta_k1
		delta_k1[k-1].forest
		for g in bfs[k-1].graph.components:
 			g.stallings()
		delta_k1.append(deltap_k1k)
	print('digraph 1,0 {')
	print(str(delta_k1[0]))
	print('}')
	print('digraph 1,1 {')
	print(str(delta_k1[1]))
	print('}')
	return delta_k1[0],delta_k1[1]
