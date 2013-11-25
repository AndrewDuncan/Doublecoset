list=[1,2,3,4,5,6,7,8]
dely=[]
print("dely is ", dely)
for a in list:
    print("a is ", a)
    print("index of a is ", list.index(a))
    ind=list.index(a)
    for b in list[ind:-1]:
        print("b is ", b)
        if not b in dely:
            if b % 2 == 0:
                print("even b is ",b)
                dely.append(b)
                print("dely is now ", dely)
    
print("list is so ", list)
for b in dely:
    list.remove(b)


print("list is ", list)
