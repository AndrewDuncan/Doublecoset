from graph import *
#import copy

#######################################################
#function to make a distinct copy of graph G, ignoring edges with label in L.
#If a vertex has an edge with label in L it is marked as a boundary=1
#otherwise it has boundary =0
########################################################
def CopyGraph(G,L):

	Clabel=G.label# the label of the copy C is the label of G
	C=Graph(rooted=False,label=Clabel,Olabel=0) #creat copy
	for v in G.vertices:#create vertices of the copy
		vname=v.name
		vlabel=v.label
		if G.root==v:
			C.root=C.addVertex(vname)#if v is the root of G make it root of the copy
			Cv=C.root 
		else:
			Cv=C.addVertex(vname)#and in both cases add a vertex

		Cv.label=vlabel
		Cv.boundary=0#initialise the boundary, which will be set to 1 later if necessary

	for v in G.vertices:#now add edges 
		found=0
		for u in C.vertices: #find the vertex of C corresponding to v in G
			if v.label==u.label:
				Cv=u
				found=1
				break

		if found==0:
			error_message="Exiting from CopyGraph: a vertex of original was not recreated in the copy. Original vertex "+str(v)
			sys.exit(error_message)
			
		#now v is equal to Cv and an edge is added at Cv for each edge at v (unless the label is in L)
		for (label,s) in  v.outedgesList:
			if label in L:
				Cv.boundary = 1
			else:
				o=v.outedges_write[(label,s)]
				found=0
				for u in C.vertices:
					if s.name==u.name:
						C.addEdge(Cv,u,label,o) #add a labelled edge
						found=1
						break
				if found==0:
					error_message="Exiting from CopyGraph: a edge of original was not recreated in the copy. Original vertex "+str(v)+" original edge "+str((label,s))
					sys.exit(error_message)

		for (label,s) in  v.inedgesList:# in edges with label in L also make the bounary of Cv =1 
			if label in L:
				Cv.boundary = 1
				

	return(C)

def CompareGraphs(H,C):#only works if the vertices of both are in the same order
	same=1
	diff=[]
	if str(H.vertices)!=str(C.vertices):
		diff.append('v')
		same=0
		print("differ")
		print(str(H.vertices))
	else:
		print("saame")
		V=len(H.vertices)
		i=0
		print(V)
		while i<V:
			v=H.vertices[i]
			u=C.vertices[i]
			print("i", i, "verts ", v," and ",u)
			if str(v.outedgesList)!=str(u.outedgesList):
				same=0
				diff.append('e')
				diff.append([v,u])
				print(u,v, "edges differ", v.outedgesList, " and ", u.outedgesList)
			else:
				print(u,v, "edges saame")
			i+=1

	return(same,diff)

