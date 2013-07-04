from alg1a import *

def listsplitter4(w,f1gens,f2gens): #Takes a word in F1*F2 and two sets of generators as input
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

###This is a test, can be removed or altered to test the function###
w=['a1','A1','A2','b3','b1','b2','B12','a4']
v=['cat','B1','B2','bat','a1','A1','fat','A2','hat','b3','d','a1','b2','c','a4']
f1=free_group(4,'a')
f2=free_group(3,'b')
f1.make_gens()
f2.make_gens()
a=f1.mongens
b=f2.mongens
listsplitter4(w,a,b)
listsplitter4(v,a,b)

