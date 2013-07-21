from alg1 import *

def listsplitter(w,f1gens,f2gens):
	l=len(w)
	ww=[] #ww is the "list of lists"
	ww.append([w[0]])
	if w[0] in f1gens:
		j=1
	else:
		j=2
	for c in range(1,l):
		if j==1:
				if w[c] in f1gens:
					ww[-1]=ww[-1]+[w[c]]
				else:
					j=2
					ww.append([w[c]])
		else:
				if w[c] in f2gens:
					ww[-1]=ww[-1]+[w[c]]
				else:
					j=1
					ww.append([w[c]])
	#print (ww)
	for c in range(1,l):
		if w[c]==[]:
			w.remove(w[c])
	#print(ww)
	return(ww)

def reducelist(w):
	for c in w: #freely reducing each fi in w
		c=element(c).word
	return(w)

def listtest(w,f1gens,f2gens):
	i=1
	genset=f1gens+f2gens
	#print(genset)
	for c in w:
		if c not in genset:
			print(c,' isn\'t an element of either free group')
			i=0
#	if i==0:
#		print(w,' isn\'t a word in the free (amalgamated) product')
	return(i)

def joiner(w):
	if w==[[[],[],[]]]:
		return []
	elif len(w)==1:
		ww=ww[0][0]+ww[0][1]+ww[0][2]
		return ww
	ww=[w[0][0]]
	#print('ww=[w[0][0]]= ', ww)
	for i in range(0,len(w)-1):
		#print('i is ', i)
		ww.append(w[i][1])
		#print('after appending w[i][1], ww is ', ww)
		t = [w[i][2] + w[i+1][0]]
		#print('t is ', t)
		ww = ww + t
		#print('ww becomes', ww)
		#ww.append(t)
	ww.append(w[-1][1])
	ww.append(w[-1][2])
	#print('so now ww is\n',ww)
	w=[]
	for c in ww:
		w.extend(c)
	#print('and w becomes ',w)
	w=element(w).word
	#print('which reduces to',w)
	#print('joiner returns\n',w)
	return(w)

def quickreduce(w): #reduces only the necessary elements in dcnf, not needed due to change to joiner function
		for i in range(0,len(w)):
			if w%2==0:
				w[i]=element(w[i]).word
		#print(w)
		return(w)

def alg2_pre(H1,H2):
	H1.stallings()
	H2.stallings()
	flower1=H1.flower
	flower2=H2.flower
	T1=bfs(flower1,)
	T1.forest()
	T2=bfs(flower2,)
	T2.forest()
	double1=flower1.double()
	double2=flower2.double()
	bfs1=bfs(double1,sorted(double1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	forest1=bfs1.forest()
	bfs2=bfs(double2,sorted(double2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	forest2=bfs2.forest()
	H1.subgroup_free_gens=subgroup_basis(flower1)[1]
	H2.subgroup_free_gens=subgroup_basis(flower2)[1]
	#print("basis of H1",H1.subgroup_free_gens)
	#print("or", subgroup_basis(flower1)[0])
	#print("basis of H2",H2.subgroup_free_gens)
	#print("or", subgroup_basis(flower2)[0])
	return(flower1,flower2,double1,double2,forest1,forest2)

def alg2(w,F1,F2,H1,H2):
	print(w)
	w=element(w).word
	print('w=element(w).word\n',w)
	w=popper(w)
	print('w=popper(w)\n',w)
	if w==[]:
		print([])
		return []
	listtest(w,F1.mongens,F2.mongens)
	if listtest(w,F1.mongens,F2.mongens)==0:
		print(w,' isn\'t a word in the free (amalgamated) product')
		return
	w=listsplitter(w,F1.mongens,F2.mongens)
	print('w=listsplitter(w,F1.mongens,F2.mongens)\n',w)
	w=amalgamate(w,F1,F2,H1,H2)
	print('w=amalgamate(w,F1,F2,H1,H2)\n',w)
	w=listsplitter(w,F1.mongens,F2.mongens)
	print('w=listsplitter(w,F1.mongens,F2.mongens)\n',w)
	w=reducelist(w)
	print('w=reducelist(w)\n',w)
	(flower1,flower2,double1,double2,forest1,forest2)=alg2_pre(H1,H2)
	#print(w)
	#w=listsplitter(w,F1.mongens,F2.mongens)
	#print('w=listsplitter(w,F1.mongens,F2.mongens)\n',w)
	w=nf_in_list(w,flower1,flower2,double1,double2,F1,F2)
	print('w=nf_in_list(w,flower1,flower2,double1,double2,F1,F2)\n',w)
	w=joiner(w)
	print('w=joiner(w)\n',w)
	w=popper(w)
	print('w=popper(w)\n',w)
	w=element(w).word
	print('w=element(w).word\n',w)
	print(w)
	return(w)

def nf_in_list(w,flower1,flower2,double1,double2,F1,F2):
	ww = []
	for c in w:
		#print("here  1, F1.is_element(c), F2.is_element(c)", F1.is_element(c), F2.is_element(c))
		if F1.is_element(c)!=0:
			#print("c is ",c, "in F1", F1.is_element(c))
			d = Normal_form(flower1,c,double1).spit_out_nf()
			#e = [d[3],d[1],d[4]]
			e = [d[0],d[1],d[2]]
			#print("here  2")
		elif F2.is_element(c)!=0:
			#print("c is ",c, "in F2",F2.is_element(c))
			d = Normal_form(flower2,c,double2).spit_out_nf()
			#e = [d[3],d[1],d[4]]
			e = [d[0],d[1],d[2]]
			#print("here  3")
		else:
			print(c," isn't a word in either free group")
		#print("Syllable in normal form is ",e)
		ww.append(e)
		#print("here  4")
	return(ww)

#def subgroup_basis(flower): #from the stallings folding and labelled subtree for a subgroup construct a free generating set
#	fgens=[]
#	for v in flower.vertices:
#		print("I am a vertex", v)

def popper(w):
	return [e for e in w if e!=""]

def amalgamate(w,F1,F2,H1,H2):
	if w==[]:
		print('w is the empty word')
		return([])
	F=(F1,F2)
	error=0
	n=len(w)-1
	if F[0].is_element(w[n])==1:
		f=0
		#print('f is ',f)
	elif F[1].is_element(w[n])==1:
		f=1
		#print('f is ',f)
	else:
		print('Error: ',w[n],'not in F1 or F2')
		return
	ff=f
	for s in range(n,-1,-1):
		#print('s is',s,'f is',f)
		if F[f].is_element(w[s])==0:
			print("Error: ",w[s],'is not in F',f)
			error=1
			#print('error becomes 1')
			break
		f=1-f
	if error==1:
		return
	H=(H1,H2)
	f=ff
	for s in range(n,-1,-1):
		#w[s] in H[f]: #need to make this work - H[f] isn't actually a list of generators here, making a new hf_test function
		#put w[s] in terms of H[1-f] here
		print('Start of loop. w is', w)	
		print('s is',s)
		print('w[s] is',w[s])
		print("H[f] is ", H[f].name)
		t=hf_test(w[s],H[f])
		if t[0]==1: #if w[s] is in H[f]
			w[s]=phi(H[1-f],t[1])[0] #swap w[s] from H[f] to H[1-f]
			if s==0:#  if the first syllable is in H[f]
				if len(w)>1:# if w has already been reduced to a single syllable there is no need to do anything more
					w[s]=w[s]+w[s+1]
					w[s]=element(w[s]).word
					for i in range(s+2,len(w)):
						w[i-1]=w[i]
					print("a,len(w)", len(w))
					w.pop(len(w)-1)
					print("b, len(w)", len(w))
			elif s==len(w)-1:# when the amalgamated syllable is the last one
				w[s-1]=w[s-1]+w[s]
				w[s-1]=element(w[s-1]).word
				print("c, len(w)",len(w))
				w.pop(s)
				print("d,len(w)", len(w))
			else: # the general case
				w[s-1]=w[s-1]+w[s]+w[s+1]
				w[s-1]=element(w[s-1]).word
				for i in range(s+2,len(w)):
					w[i-2]=w[i]
					print("len(w)", len(w)," and i,w[i-2], w[i]", i,w[i-2],w[i])
				print("e,len(w)", len(w))
				w.pop(len(w)-1)
				print("f,len(w)", len(w))
				w.pop(len(w)-1)
				print("g,len(w)", len(w))

		f=1-f

	return(w)

def hf_test(w,H):
	t=graph_pass(H.flower,w).acc_read_rem()
	print("in hf_test t is ", t)
	#print("H name, gens, free_gens", H.name, H.subgp_gens, H.subgroup_free_gens, "and t[4] is ", t[4])
	if len(t[1])==0 and len(t[2])==0:# in this case w[s] is in H[f]
		j=1
		#w=phi(H[1-k],t[4])[0]
	else:
		j=0
	print("after hf_test j is",j)
	return(j,t[4])
