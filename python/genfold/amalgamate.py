from alg2 import *

def amalgamate(w,F1,F2):
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
		if w[s] in H[f]: #need to make this work - H[f] isn't actually a list of generators here, making a new hf_test function
			#put w[s] in terms of H[1-f] here
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

def hf_test(w,H):
	t=graph_pass(H).acc_read_rem()
	if len(t[1])==0 and len(t[2])==0
		j=1
	else:
		(j,)=(0,)