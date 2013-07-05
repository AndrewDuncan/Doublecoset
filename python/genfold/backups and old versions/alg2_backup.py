from alg1 import *

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
	print('ww=[w[0][0]]= ', ww)
	for i in range(0,len(w)-1):
		print('i is ', i)
		ww.append(w[i][1])
		print('after appending w[i][1], ww is ', ww)
		t = [w[i][2] + w[i+1][0]]
		print('t is ', t)
		ww = ww + t
		print('ww becomes', ww)
		#ww.append(t)
	ww.append(w[-1][1])
	ww.append(w[-1][2])
	print('so now ww is\n',ww)
	w=[]
	for c in ww:
		w.extend(c)
	print('and w becomes ',w)
	w=element(w).word
	print('which reduces to',w)
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
	w=nf_in_list(w,flower1,flower2,forest1,forest2,F1,F2)
	w=joiner(w)
	print(w)
	return(w)

def nf_in_list(w,flower1,flower2,forest1,forest2,F1,F2):
	ww = []
	for c in w:
		if F1.is_element(c)!=0:
			c = Normal_form(flower1,c,forest1).spit_out_nf()
			c = [c[3],c[1],c[4]]
		elif F2.is_element(c)!=0:
			c = Normal_form(flower2,c,forest2).spit_out_nf()
			c=[c[3],c[1],c[4]]
		else:
			print(c," isn't a word in either free group")
		print("Syllable in normal form is ",c)
		ww.append(c)
	return(ww)