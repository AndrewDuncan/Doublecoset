L=['a','b','c']
M=['u','v']
print("The generators are:\n",L,"\n and the basis is: \n",M)
print("There are more elements in the set of generators given  than the rank computed by Stallings folding.")
print("Halt!")
user_input = input("Who goes there? ")
print("You may pass, " + user_input)
resp = input("Either 1) enter q to quit or \n 2) enter c: ")
print("resp is " + resp)

while str(resp)!='q' and str(resp)!='c':
    print("resp is", resp)
    resp=input("Please enter q or c: ")
    
if str(resp)=='q':
    print("found q and resp is", resp)
else:
    L=input("enter your new generators: ")
        

