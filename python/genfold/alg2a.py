from alg1a import *

def listsplitter(w,f1gens,f2gens): #Takes a word in F1*F2 and two sets of generators as input, the new version (below) broke things
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
	print(ww) #likely unnecessary but makes testing a lot easier
	return(ww)

#def listsplitter(w,f1gens,f2gens,f1,f2): #Takes a word in F1*F2 and two sets of generators as input
#	l=len(w)
#	ww=[] #ww is the "list of lists"
#	ww.append([w[0]])
#	if w[0] in f1gens:
#		j=1
#	elif w[0] in f2gens:
#		j=2
#	else:
#		print (w[0], 'isn\t in either free group')
#		j=0
#	for c in range(1,l):
#		if f1.is_element(w[c])==0 and f2.is_element(w[c])==0:
#			print (w[c], 'isn\t an element in either free group')
#			break
#		if j==1:
#				if w[c] in f1gens:
#					ww[-1]=ww[-1]+[w[c]]
#				else:
#					j=2
#					ww.append([w[c]])
#		elif j==2:
#				if w[c] in f2gens:
#					ww[-1]=ww[-1]+[w[c]]
#				else:
#					j=1
#					ww.append([w[c]])
#	print (ww)
#	for c in range(1,l):
#		if w[c]==[]:
#			w.remove(w[c])
#	print(ww) #likely unnecessary but makes testing a lot easier
#	return(ww)

def reducelist(w):
	for c in w: #freely reducing each fi in w
		c = element(c)
		w[c]=c.freely_reduce()
	return(w)

def nf_in_list(w,F1,F2,H1,H2): #doesn't work, can't quite figure out why yet
	H1.make_flower()
	H1.stallings()
	H2.make_flower()
	H2.stallings()
	
	
	S1 = H1.flower
	D1 = S1.double()
	DB1 = bfs(D1,sorted(D1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	S2 = H2.flower
	D2 = S2.double()
	DB2 = bfs(D2,sorted(D2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
	DB1.forest()
	DB2.forest()
	
	if w[0] in f1.mongens:
		s=1
	else:
		s=2
	for c in w[0:len(w)]:
		if s==1:
			c = Normal_form(S1,c,DB1).spit_out_nf() #AttributeError:'Vertex' object has no attribute 'path'
			c = [c[3],c[1],c[4]]
			s=2
		else:
			c = Normal_form(S2,c,DB2).spit_out_nf()
			c = [c[3],c[1],c[4]]
			s=1
	print(w)
	return(w)


def nf_in_list2(w): #alternative function to avoid problem with the other nf_in_list function, currently untested
	for c in w:
		if f1.is_element(c)!=0:
			c = Normal_form(S1,c,DB1).spit_out_nf()
			c = [c[3],c[1],c[4]]
		elif f2.is_element(c)!=0:
			c = Normal_form(S2,c,DB1).spit_out_nf()
			c=[c[3],c[1],c[4]]
		else:
			print(c," isn't a word in either free group")
		print(w)
		return(w)
			

def listtest(w,F1,F2): #w is a word, F1 and F2 free groups
	i=1
	for c in range(1,len(w)):
		if F1.is_element(w)==0 and F2.is_element(w)==0:
			print('c isn\'t an element of either free group')
			i=0
	return(i)

def alg2_main(w,f1,f2,h1,h2):
	f1.make_gens()
	f2.make_gens()
	f1gens=f1.mongens
	f2gens=f2.mongens
	listtest(w,f1,f2)
	w=listsplitter(w,f1gens,f2gens,f1,f2)
	if w[0] in f1gens:
		w=nf_in_list(w,f1,f2,h1,h2)
	else:
		w=nf_in_list(w,f2,f1,h2,h1)
#	w=nf_in_list2(w)
	w=joiner(w)
	
	print(w)
	return(w)

def joiner(w):
	ww=[w[0][0]]
	for i in range(0,len(w)-1):
		ww.append(w[i][1])
		t = [w[i][2]] + [w[i+1][0]]
		c = element(t)
		t = c.freely_reduce()
		ww = ww + t
		#ww.append(t)
	ww.append(w[-1][1])
	ww.append(w[-1][2])
	print(ww)
	return(ww)

def quickreduce(w): #reduces only the necessary elements in dcnf, not needed due to change to joiner function
		for i in range(0,len(w)):
			if w%2==0:
				c = element(w[i])
				w[i]=c.freely_reduce()
		print(w)
		return(w)

######################################
