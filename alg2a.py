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
		elifj==2:
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

def reducelist(w)
	for c in w: #freely reducing each fi in w
		c = element(c)
		w[c]=c.freely_reduce()
	return(w)

if w[0] in f1.mongens:
	s=1
elif w[0] in f2.mongens:
	s=2
else:
	print (w[0]," isn't a word in either of the free groups.")

def nf_in_list(w,f1,f2,h1,h2):
	h1.make_flower
	h1.stallings
	h2.make_flower
	h2.stallings
	
	for c in w[0:len(w)]:
		if s==1:
			c = tt=Normal_form(h1.flower,c,DB).spit_out_nf()
			c = [c[3],c[1],c[4]]
			s=2
		else:
			c = tt=Normal_form(h2.flower,c,DB).spit_out_nf()
			c = [c[3],c[1],c[4]]
			s=1
	print(w)
	return(w)


def alg2(w,f1,f2,h1,h2):
	f1.make_gens()
	f2.make_gens()
	f1gens=f1.mongens
	f2gens=f2.mongens
	if w[0] in f1gens:
		nf_in_list(w,,,,)
	else:
		nf_in_list(w,,,,)