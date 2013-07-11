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
	print (ww)
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
		print(w)
		return(w)

def alg2_pre(H1,H2):
	H1.stallings()
	H2.stallings()
	flower1=H1.flower
	flower2=H2.flower
	bfs(flower1,)
	bfs(flower2,)
	double1=flower1.double()
	double2=flower2.double()
	forest1=bfs(double1,sorted(double1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	forest1=forest1.forest()
	forest2=bfs(double2,sorted(double2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	forest2=forest2.forest()
	H1.subgroup_free_gens=subgroup_basis(flower1)
	H2.subgroup_free_gens=subgroup_basis(flower2)
	return(flower1,flower2,double1,double2,forest1,forest2)

def alg2(w,F1,F2,H1,H2):
	w=popper(w)
	listtest(w,F1.mongens,F2.mongens)
	w=amalgamate(w,F1,F2,H1,H2)
	if listtest(w,F1.mongens,F2.mongens)==0:
		print(w,' isn\'t a word in the free (amalgamated) product')
		return
	w=reducelist(w)
	(flower1,flower2,double1,double2,forest1,forest2)=alg2_pre(H1,H2)
	w=listsplitter(w,F1.mongens,F2.mongens)
	w=nf_in_list(w,flower1,flower2,double1,double2,F1,F2)
	w=joiner(w)
	w=popper(w)
	w=element(w).word
	print(w)
	return(w)

def nf_in_list(w,flower1,flower2,double1,double2,F1,F2):
	ww = []
	for c in w:
		#print("here  1, F1.is_element(c), F2.is_element(c)", F1.is_element(c), F2.is_element(c))
		if F1.is_element(c)!=0:
			print("c is ",c, "in F1", F1.is_element(c))
			d = Normal_form(flower1,c,double1).spit_out_nf()
			e = [d[3],d[1],d[4]]
			#e = [d[0],d[1],d[2]]
			#print("here  2")
		elif F2.is_element(c)!=0:
			print("c is ",c, "in F2",F2.is_element(c))
			d = Normal_form(flower2,c,double2).spit_out_nf()
			e = [d[3],d[1],d[4]]
			#e = [d[0],d[1],d[2]]
			#print("here  3")
		else:
			sprint(c," isn't a word in either free group")
		print("Syllable in normal form is ",e)
		ww.append(e)
		#print("here  4")
	return(ww)

#def subgroup_basis(flower): #from the stallings folding and labelled subtree for a subgroup construct a free generating set
#	fgens=[]
#	for v in flower.vertices:
#		print("I am a vertex", v)

def popper(w):
	return [e for e in w if e!=""]

from alg2 import *

def amalgamate(w,F1,F2,H1,H2):
	F=(F1.mongens,F2.mongens)
	error=0
	n=len(w)-1
	if w[n] in F[0]:
		f=0
	else:
		f=1
	ff=f
	for s in range(n,-1,-1):
		if w[s] not in F[f]:
			print("error message")
			error=1
			break
	if error==1:
		return
	H=(H1,H2)
	for s in range(n,-1,-1):
		#w[s] in H[f]: #need to make this work - H[f] isn't actually a list of generators here, making a new hf_test function
			#put w[s] in terms of H[1-f] here
		t=hf_test(w[s],H[f])
		if t[0]==1:
			w[s]=t[1]
		if s==n:
			w[s-1]=w[s-1]+w[s]
			w[s]=element(w[s]).word
			w.pop(s)
		elif s==1:
			w[s]=w[s]+w[s+1] #(reduced)
			w[s]=element(w[s]).word
			for i in range(s+2,n):
				w[i-1]=w[i]
				w.pop(len(w)-1)
		else:
			w[s-1]=w[s-1]+w[s]+w[s+1]
			w[s-1]=element(w[s-1]).word
			for i in range(s+2,n):
				w[i-2]=w[i]
				w.pop(len(w)-1)
				w.pop(len(w)-1)
		f=1-f
	return(w)

def hf_test(w,H):
	t=graph_pass(H).acc_read_rem()
	if len(t[1])==0 and len(t[2])==0:
		j=1
		w=phi(H,t[4])
	else:
		(j,w)=(0,[])
	return(j,w)
