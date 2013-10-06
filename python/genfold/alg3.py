from alg2 import *
from input import * #temporary, will eventually be included in the above import
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
	(flower1,double1,forest1,bfs1)=alg2_pre(H1)
	(flower2,double2,forest2,bfs2)=alg2_pre(H2)
	H=(H1,H2)
	if F1.rank>F2.rank:
		Z=free_group(F1.rank,'z')
	else:
		Z=free_group(F2.rank,'z')
	return F,Z,H1,H2,flower1,double1,forest1,bfs1,flower2,double2,forest2,bfs2# this should return in a more systematic fashion


def MakeComps(delta,F,Z): #input Delta, free groups F=(F1,F2) and Z generators
	delta_k0=[] # to become a pair of graphs, one for each X_i
	delta_z=Graph(False,'Delta Z') # the Z component, composed of edges labelled with letters of Z, removed in the process of pruning shoots
	for k in (1,2): # do the following for X_1 and X_2 components
		delta_k0k=copy.deepcopy(delta) #take a new copy of delta, call it k0k
		for v in delta_k0k.vertices[::-1]: #part a,remove edges of k0k which are in X_[2-k] to make component
			for label,w in v.outedgesList[::-1]:
				if label in F[2-k].mongens: # 
					v.removeOutEdge(label,w)
					w.removeInEdge(label,v)
			for label,w in v.inedgesList[::-1]:
				if label in F[2-k].mongens:
					v.removeInEdge(label,w)
					w.removeOutEdge(label,v)
		shoots=1  #part b, remove Z shoots
		while shoots!=0:
			ind=0
			for v in delta_k0k.vertices[::-1]: #for each vertex of k0k
				#print("k is ", k, " v name, v label ", v.name, v.label)
				edgesList=v.inedgesList+v.outedgesList # make a list of all edges incident to v
				v_in_delta_z=0
				for u in delta_z.vertices: #now test to see if this vertex v is in the Z component, delta_z
							if v.label==u.label:
								v_in_delta_z=1# set this flag to 1 if v is already in delta_z
								vcopy=u # keep track of which vertex of delta_z is equal to v
				if len(edgesList)==1: # if we have a shoot with leaf v
					#print(edgesList)
					if edgesList[0][0] in Z.mongens: # and the shoot has a label in Z
						ind+=1
						#print("ind is ", ind)
						#print("we found an edge to remove:", edgesList[0])
						vv_in_delta_z=0
						for u in delta_z.vertices:
							#print("u is", u, " and edgesList[0] is ", edgesList[0])
							if edgesList[0][1].label==u.label: 
								vv_in_delta_z=1# set this flag to 1 if the other end of this edge is already in delta_z
								vvcopy=u # and in this case keep track of the vertex of delta_z at the other end of the shoot with leaf v
								#print("found that vertex ", edgesList[0][0], "is already in delta_z")
								break
						if v_in_delta_z==0: # v is not already in delta_z
							vcopy=delta_z.addVertex(v.name) # add a new vertex to delta_z with same descr as v
							vcopy.label=v.label
							#print("v looks like",v.label,v.name)
							#print("vcopy looks like",vcopy.label,vcopy.name)
							v_in_delta_z=1 # record that v is now in delta_z
							#print("k is", k, " added vertex v", vcopy.label)
						if vv_in_delta_z==0: #if the other end of the shoot is not in delta_z
							vv=edgesList[0][1]
							vvcopy=delta_z.addVertex(vv.name)# add it to delta_z
							vvcopy.label=vv.label
							#print("k is", k, " added vertex to delta_z vv with label and name", vvcopy.label, vvcopy.label)
							vv_in_delta_z=1 #record that this vertex is now in delta_z
					
						if len(v.inedgesList)==1: #if the shoot is an inedge at v
							#print("k is ", k,"v is ", v," inedges are", v.inedgesList, "outedges are ",v.outedgesList)
							#if the edge is already incident to vcopy in delta_z, do nothing
							if (edgesList[0][0],edgesList[0][1]) not in vcopy.inedgesList: 	#print("nothing to do")
							#else:   #else add an edge to delta_z
								delta_z.addEdge(vvcopy,vcopy,edgesList[0][0])#print("adding edge , edgesList[0] is ",edgesList[0],"vcopy.inedgesList is ", vcopy.inedgesList)	
							#print("k is", k, "vcopy,vvcopy=", vcopy,vvcopy, " added edge vv to v with label", edgesList[0][0])
						elif len(v.outedgesList)==1:#if the shoot is an outedge at v
							#if the edge is already incident to vcopy in delta_z, do nothing#print("nothing doing")
							if (edgesList[0][0],edgesList[0],[1]) not in vcopy.outedgesList:
							#else:  #else add an edge to delta_z
								delta_z.addEdge(vvcopy,vcopy,edgesList[0][0]) 
								#print("adding edge , edgesList[0] is ",edgesList[0],
								#	  "vcopy.inedgesList is ", vcopy.inedgesList)
								#print("k is", k, "vcopy,vvcopy=", vcopy,vvcopy, " added edge vv to v with label", edgesList[0][0])
						else:
							print("something is wrong in alg3_alt2 at vertex v", v)
						#print("vcopy.inedgesList is ",vcopy.inedgesList)
						#print("vcopy.outedgesList is ",vcopy.outedgesList)
						#print("vvcopy.inedgesList is ",vvcopy.inedgesList)
						#print("vvcopy.outedgesList is ",vvcopy.outedgesList)
						label=edgesList[0][0]
						w=edgesList[0][1]
						if (label,w) in v.inedgesList: #now remove the shoot from the in or out edges of the non-leaf end
							v.removeInEdge(label,w)
							w.removeOutEdge(label,v)
						else:
							v.removeOutEdge(label,w)
							w.removeInEdge(label,v)

			shoots=ind
		for v in delta_k0k.vertices[::-1]:
			if len(v.inedgesList)+len(v.outedgesList)==0: # remove isolated vertices from k0k
				delta_k0k.removeVertex(v)
		for v in delta_k0k.vertices: #give vertices of k0k their new names
			#print("v.label", v.label)
			v.nu_im={v.label} #part d
			v.name='({0},{1})'.format(v.label,k) #part c
			v.label='({0},{1})'.format(v.label,k) #part c
			#print("here we are in MakeComps and vertex v =", v.label, "has v-im set to", v.nu_im)
		delta_k0.append(delta_k0k) #append k0k to the list of delta1 and delta2
	return delta_k0[0],delta_k0[1],delta_z #these are distinct graphs built from copies of delta

def Mod1(delta_k0,Z,H,flower):#input delta_k0(X1 and X2 components), Z gens, H subgroup and its folding. For each Z edge, add a corresponding path in X_k generators
	delta_k1=[]
	for k in (1,2):
		delta_k1k=delta_k0[k-1]# copy.deepcopy(delta_k0[k-1])# make a copy, k1k of delta_k0 - but why - should use copy already made
		for v in delta_k1k.vertices: #for each vertex v of delta_k0, set original to 0
			v.original=0
		for v in delta_k1k.vertices: #for each vertex v of k1k	
			for outedges in v.outedgesList:# for each outedge e incident to v
				if outedges[0] in Z.mongens: #with a Z label
					#print("v", v, "outedges [1]", outedges[1], "outedges [0]", [outedges[0]], "k", k)
					Xword=phi(H[k-1],[outedges[0]])[0]
					#print("Xword is ", Xword)
					Try_to_read_Xword=graph_pass(delta_k1k,Xword,v).acc_read_rem()
					#print("output of try to read", Try_to_read_Xword)
					delta_k1k.addPath(v,outedges[1],phi(H[k-1],[outedges[0]])[0])# add  a path of x's with the same end points as e
		for v in delta_k1k.vertices:# for each v in k1k
			#foundv=0
			if not hasattr(v,'original'):
				#print("here's a new vertex", v.label)
				v.original=1 # original equals 1, for those vertices added in modification 1
				v.nu_im={v.label}
				v.name='({0},{1})'.format(v.label,k) 
				v.label='({0},{1})'.format(v.label,k)
				#print("v is", v," v.nu_im is", v.nu_im)
		go = True
		while go: #fold k1k, updating of v.nu_im in the process
			go = delta_k1k.fold()
		delta_k1.append(delta_k1k)#add k1k to delta_k1
	return delta_k1[0],delta_k1[1] #return delta_k1, both components


def Mod2(delta1,flower): #each of delta1 and flower is a pair (delta1_1,delta1_2) and (flower1,flower2); the latter of Stallings foldings
#Mod2 constructs the product of delta_k and flowerk, then a spanning forest for this graph, then carries out Algorithm III steps D6 and D7
	delta2=[]
	Prod=[]
	Prod_Forest=[]
	Prod_components=[]
	for k in (0,1):
		delta2k=delta1[k]# the new component to be constructed
		Prod.append(delta1[k].product(flower[k]))# form the product  delat1_k x \Gamma_k
		Prod_bfs=bfs(Prod[k],sorted(Prod[k].vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
		Prod_bfs.forest()#assigns properties, like distance from root, path from root in forest, etc. to vertices of product
	
		#for v in delta1[k].vertices:
		#	v_by_one=str(v.label)+'-'+str('1')
		#	print(v.label, "v-by-one", v_by_one)
		#	for u in Prod[k].vertices:
		#		if v_by_one==u.label:
		#			v_1=u
		#			print("found v_1", v_1)
		#			break
		#	print("or man", v_1.label,v_1.colour, v_1.path)
		#	for u in Prod[k].vertices:
		#		if str(u.label).endswith('1') and u.colour==v_1.colour:
		#			print("ends in one",u.label, "and has right colour", u.colour, "and path ", u.path)
		#		else:
		#			print("does not", u.label, u.colour)
		Pcomponents={}
		#construct a dictionary with key the components of the product P_k and for such key a value list of vertices of form (a,1) in that component
		for u in  Prod[k].vertices:
			if str(u.label).endswith('1'): #if the right hand label is 1, add this vertex to the dictionary entry for its component
				if str(u.colour) in Pcomponents:
					L=Pcomponents[str(u.colour)]
					L.append(u)
					L.sort(key=lambda x: x.length)
					Pcomponents[str(u.colour)]=L
				else:
					Pcomponents[str(u.colour)]=[u]
		
		for col in Pcomponents:
			col_root=Pcomponents[col][0]#the first element of the list of vertices (a,k)-1, in this component
			delta_root3 = col_root.label.partition("-") # this splits the label into 3, with "-" in the middle
			print("del_root", delta_root3[0]) #strip off the lhs of the triple above to get the vertex in delta (it's label)
			delta_root_lab=delta_root3[0]
			for w in delta2k.vertices: #now find the vertex of delta2k with label delta_root_lab
				if w.label==delta_root_lab:
					delta_root=w
					break
			for v in Pcomponents[col][1:]:
				if len(v.path)>0:
					Xword=element(v.path).word
					Gword=graph_pass(flower[k],Xword).acc_read_rem() #find the Z word corresponding to Xword
					print("Gword is ",Gword)
					print("Gword[4] is ", Gword[4])
					if len(Gword[1])>0 or len(Gword[2])>0:
						print("Something bad happened in Modification 2: tried to add a path not in H. Here is the output of graph_pass:", Gword)
						print("and k is ", k, "colour is ", col," v is ",v.label,"path is ", v.path)
					else:
						Zword=Gword[4]
						delta_v_lab=v.label.partition("-")[0]
						print("delta_v",delta_v_lab)
						for w in delta2k.vertices: #now find the vertex of delta2k with label delta_v_lab
							if w.label==delta_v_lab:
								delta_v=w
								break
						delta2k.addPath(delta_root,delta_v,Zword)# add  a path of Z's from the root of component col to v 
					
						
		for v in delta2k.vertices:# for each v in k1k
			print("k is", k, "v is", v.label, "and hasattr orig is", hasattr(v,'original'))
			if not hasattr(v,'original'): #these are the vertices added in Modification 2
				v.original=2 # 
				v.nu_im={v.label}
				v.name='({0},{1})'.format(v.label,k) 
				v.label='({0},{1})'.format(v.label,k)
				#print("v is", v," v.nu_im is", v.nu_im)
		
		go = True
		while go: #fold k1k, updating of v.nu_im in the process
			go = delta2k.fold()
		Prod_components.append(Pcomponents)
		delta2.append(delta2k)
		
			
	
	return(Prod,Prod_components,delta2)

