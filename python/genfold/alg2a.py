from alg1a import *

def listsplitter(w,f1gens,f2gens,f1,f2): #Takes a word in F1*F2 and two sets of generators as input
	l=len(w)
	ww=[] #ww is the "list of lists"
	ww.append([w[0]])
	if w[0] in f1gens:
		j=1
	elif w[0] in f2gens:
		j=2
	else:
		print (w[0], 'isn\t in either free group')
		j=0
	for c in range(1,l):
		if f1.is_element(c)==0 and f2.element()==0:
			print (c, 'isn\t an element in either free group')
			break
		if j==1:
				if w[c] in f1gens:
					ww[-1]=ww[-1]+[w[c]]
				else:
					j=2
					ww.append([w[c]])
		elif j==2:
				if w[c] in f2gens:
					ww[-1]=ww[-1]+[w[c]]
				else:
					j=1
					ww.append([w[c]])
	print (ww)
	for c in range(1,l):
		if w[c]==[]:
			w.remove(w[c])
	print(ww) #likely unnecessary but makes testing a lot easier
	return(ww)

def reducelist(w):
	for c in w: #freely reducing each fi in w
		c = element(c)
		w[c]=c.freely_reduce()
	return(w)

def nf_in_list(w,f1,f2,h1,h2):
	h1.make_flower
	h1.stallings
	h2.make_flower
	h2.stallings
	
	
	S1 = h1.flower
	D1 = S1.double()
	DB1 = bfs(D1,sorted(D1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	S2 = h2.flower
	D2 = S2.double()
	DB2 = bfs(D2,sorted(D2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	
	
	if w[0] in f1.mongens:
		s=1
	else:
		s=2
	for c in w[0:len(w)]:
		if s==1:
			c = tt=Normal_form(S1,c,DB1).spit_out_nf()
			c = [c[3],c[1],c[4]]
			s=2
		else:
			c = tt=Normal_form(S1,c,DB2).spit_out_nf()
			c = [c[3],c[1],c[4]]
			s=1
	print(w)
	return(w)

def listtest(w,f1,f2): #w is a word, f1 and f2 free groups
	i=1
	for c in range(1,len(w)):
		if f1.is_element(w)==0 and f2.is_element(w)==0:
			print('c isn\'t an element of either free group')
			i=0
	return(i)

def alg2(w,f1,f2,h1,h2):
	f1.make_gens()
	f2.make_gens()
	f1gens=f1.mongens
	f2gens=f2.mongens
	listtest(w,f1,f2)
	w=listsplitter(w,f1gens,f2gens,f1,f2)
	if w[0] in f1gens:
		nf_in_list(w,f1,f2,h1,h2)
	else:
		nf_in_list(w,f1,f2,h1,h2)
	print(w)
	return(w)

def joiner(w): #
	ww=[w[0][0]]
	for i in range(0,len(w)-1):
		ww.append(w[i][1])
		t = w[i][2] + w[i+1][0]
		ww.append(t)
	ww.append(w[-1][1])
	ww.append(w[-1][2])
	print(ww)
	return(ww)

def quickreduce(w): #reduces only the necessary elements in dcnf
		for i in range(0,len(w))
			if w%2==0:
				c = element(w[i])
				w[i]=c.freely_reduce()
		print(w)
		return(w)