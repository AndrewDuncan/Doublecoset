L=['a','b','c']
M=['u','v']
resp=''
while len(L)>len(M):
    print("The generators are:\n",L,"\n and the basis is: \n",M)
    print("There are more elements in the set of generators given  than the rank computed by Stallings folding.")
    resp=raw_input("Either 1) enter q to quit or \n 2) enter c to continue with M as a generating set for the subgroup or\n 3) enter r to continue and enter a new set of subgroup generators: ")
    #resp=input("q,c or r?")
    while str(resp)!='q' and str(resp)!='c' and str(resp)!='r':
        print("resp is", resp)
        resp=raw_input("Please enter q,c or r: ")
    
    if resp=='q' or resp=='c':
        break
    else:
        L=input("enter your new generators: ")

print("resp", resp)
