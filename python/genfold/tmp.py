from graph import *
import string
v2=2
v4=4
v5=5
v6=6
l1=[('a', v2, "c"), ('b', v4, "d"), ('b', v5, "e"), ('a', v6, "f")]
d1={'a': [v2, v6], 'b': [v4, v5]}
do1={'a': ["c", "f"], 'b': ["d", "e"]}
#print(l1[0][1])
#print(l1[0][0:2])
label='b'
v=4
#if (label, v) in l1[0][0:1]:
#    print("hw")
#print("loop")
#for i in range(len(l1)):
# if l1[i][0:2]==(label,v):
#     print(label,v, "=",l1[i])
#     break    
# else:
#     print("no")
 #    break
 
 #else:
 #    print("no")
        
itList=[]
inedges=[]
inedges_outlabels=[]
def addIt(label,v,olabel):
                for i in range(len(l1)):
                    if l1[i][0:2]==(label,v):
                        print("fn", label,v, "=",l1[i])
		        #if (label,v) in self.inedgesList:
			return
		else:
			#itList.append((label,v,olabel))
                        print("add edge to list when label, v =", label, v)

		if not label in d1:
                        print("make new dict entry when label,v =", label, v)
			#inedges[label] = [v]
                        #inedges_outlabels[label] = [olabel]
		elif not v in d1[label]:
                        print("append dict entry when label,v =", label, v)
			#inedges[label].append(v)
                        #inedges_outlabels[label] = [olabel]

addIt("a", 3, "z")

l2=[('a', v2, "+"), ('b', v4, "+"), ('b', v5, "-"), ('a', v6, "-")]
for (x,y,z) in l2:
    print(x,y,z)
