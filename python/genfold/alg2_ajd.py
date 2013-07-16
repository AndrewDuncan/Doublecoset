from alg1 import *

#def listsplitter(w,f1gens,f2gens):
#	l=len(w)
#	ww=[]
#	genset=f1gens+f2gens
#	print(genset)
#	for c in w:
#		if c not in genset:
#			print(c,'isn\'t in the generating set of either free group,\nso ',w,' isn\'t a word in the free (amalgamated) product')

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
	#print(ww)
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
		c=element(c).word
	return(w)

#def nf_in_list(w,F1,F2,H1,H2): #doesn't work, can't quite figure out why yet
#	H1.stallings()
#	H2.stallings()
#
#	S1 = H1.flower
#	D1 = S1.double()
#	DB1 = bfs(D1,sorted(D1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
#	S2 = H2.flower
#	D2 = S2.double()
#	DB2 = bfs(D2,sorted(D2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
#	DB1.forest()
#	DB2.forest()
#	
#	if w[0] in F1.mongens:
#		s=1
#	else:
#		s=2
#	for c in w[0:len(w)]:
#		
#		if s==1:
#			c = Normal_form(S1,c,DB1).spit_out_nf() #AttributeError:'Vertex' object has no attribute 'path'
#			c = [c[3],c[1],c[4]]
#			s=2
#		else:
#			c = Normal_form(S2,c,DB2).spit_out_nf()
#			c = [c[3],c[1],c[4]]
#			s=1
#	print(w)
#	return(w)


#def nf_in_list2(w,F1,F2,H1,H2): #alternative function to avoid problem with the other nf_in_list function, currently untested
#	H1.stallings()
#	H2.stallings()
#	S1 = H1.flower
#	D1 = S1.double()
#	DB1 = bfs(D1,sorted(D1.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
#	S2 = H2.flower
#	D2 = S2.double()
#	DB2 = bfs(D2,sorted(D2.vertices, key=lambda pairs: [pairs.sortkey[1],pairs.sortkey[0]]))
#	DB1.forest()
#	DB2.forest()
#	new_w = []
#	for c in w:
#		if F1.is_element(c)!=0:
#			c = Normal_form(S1,c,DB1).spit_out_nf()
#			c = [c[3],c[1],c[4]]
#		elif F2.is_element(c)!=0:
#			c = Normal_form(S2,c,DB2).spit_out_nf()
#			c=[c[3],c[1],c[4]]
#		else:
#			print(c," isn't a word in either free group")
#		print("syllable in normal form is ",c)
#		new_w.append(c)
#	return(new_w)
			

#def listtest(w,F1,F2): #w is a word, F1 and F2 free groups
#	i=1
#	for c in w:
#		if F1.is_element(c)==0 and F2.is_element(c)==0:
#			print(c,' isn\'t an element of either free group')
#			i=0
#	return(i)

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

#def alg2_main(w,F1,F2,H1,H2):
#	f1gens=F1.mongens
#	f2gens=F2.mongens
#	listtest(w,F1,F2)
#	w=listsplitter(w,f1gens,f2gens)
#	if w[0] in f1gens:
#		w=nf_in_list(w,F1,F2,H1,H2)
#	else:
#		w=nf_in_list(w,F2,F1,H2,H1)
#	w=nf_in_list2(w)
#	w=joiner(w)
#	
#	print(w)
#	return(w)

def joiner(w):
	ww=[w[0][0]]
	for i in range(0,len(w)-1):
		ww.append(w[i][1])
		t = [w[i][2]] + [w[i+1][0]]
		t = element(t).word
		ww = ww + t
#ww.append(t)
	ww.append(w[-1][1])
	ww.append(w[-1][2])
	print(ww)
	return(ww)

def quickreduce(w): #reduces only the necessary elements in dcnf, not needed due to change to joiner function
		for i in range(0,len(w)):
			if w%2==0:
				w[i]=element(w[i]).word
		print(w)
		return(w)

######################################

#def alg2_main2(w,F1,F2,H1,H2):
#	f1gens=F1.mongens
#	f2gens=F2.mongens
#	print("Generators\n",f1gens,'\n',f2gens)
#	listtest2(w,f1gens,f2gens)
#	w=listsplitter(w,f1gens,f2gens)
#	print("Syllables:",w)
#	
#	#convert to normal forms here
#	w=nf_in_list2(w,F1,F2,H1,H2)
#	print("Normal form word",w)
	
	#w=joiner(w)
	#print(w)


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
	return(flower1,flower2,double1,double2,forest1,forest2)

def alg2(w,F1,F2,H1,H2):
	listtest(w,F1.mongens,F2.mongens)
	if listtest(w,F1.mongens,F2.mongens)==0:
		print(w,' isn\'t a word in the free (amalgamated) product')
		return
	w=reducelist(w)
	(flower1,flower2,double1,double2,forest1,forest2)=alg2_pre(H1,H2)
	w=listsplitter(w,F1.mongens,F2.mongens)
	w=nf_in_list(w,flower1,flower2,double1,double2,F1,F2)
	w=joiner(w)
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
			print("here  2")
		elif F2.is_element(c)!=0:
			print("c is ",c, "in F2",F2.is_element(c))
			d = Normal_form(flower2,c,double2).spit_out_nf()
			e = [d[3],d[1],d[4]]
			print("here  3")
		else:
			print(c," isn't a word in either free group")
		print("Syllable in normal form is ",e)
		ww.append(e)
		print("here  4")
	return(ww)