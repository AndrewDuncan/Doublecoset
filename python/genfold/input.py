r1=input("Enter the rank of the first free group: ")
l1=input("Enter the letter to represent the first free group: ")
r2=input("Enter the rank of the second free group: ")
l2=input("Enter the letter to represent the second free group: ")
F1=free_group(r1,l1)
F2=free_group(r2,l2)

c=input("How many generators do the subgroups have? ")
h1=[]
h2=[]

print("Enter the generators of the first subgroup, pressing enter after each one:")
for i in range(0,c):
	c=input("Enter generator ",i+1,":/n")
	c.split(",")
	h1.append(c)

print("Now enter the generators for the second subgroup:")
for i in range(0,c):
	c=input("Enter generator ",i+1,":/n")
	c.split(",")
	h2.append(c)

H1=subgroup("H1",h1,)
H2=subgroup("H2",h2,)