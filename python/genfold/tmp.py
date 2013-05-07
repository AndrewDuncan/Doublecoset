from graph import *
import string
v2=2
v4=4
v5=5
v6=6
l1=[('a', v2, "c"), ('b', v4, "c"), ('b', v5, "c"), ('a', v6, "c")]

print(l1[0][1])
print(l1[0][0:2])
label='b'
v=4
if (label, v) in l1[0][0:1]:
    print("hw")
print("loop")
for i in range(len(l1)):
 if l1[i][0:2]==(label,v):
     print(label,v, "=",l1[i])
     break    
 else:
     print("no")
 #    break
 
 #else:
 #    print("no")
        

