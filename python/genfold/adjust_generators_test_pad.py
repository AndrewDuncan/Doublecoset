
############################
#Hgens=H1.subgp_gens  


# Open  new file to see effect of relabelling
with open(testfile+"stall1.gv", "w") as f1:
    f1.write("digraph D {\n") #and write to it
with open(testfile+"stall1.gv", "a") as f1: #then open it in append mode
    f1.write(str(stall)) #and continue to write to it
    f1.write("}")
f1.close()

print(stall.root)
forced_bfs(stall)
print("stall components", stall.components)

for v in stall.vertices:
    print("vertex ", v,"colour, length, time, parent, path",v.colour,v.length,v.time, v.parent,v.path)


print("stall components",stall.components)
print("H subgroup_free_gens", H1.subgroup_free_gens, "H1.subgp_gens", H1.subgp_gens)


for u in stall.vertices:
    print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write)
    print(u,"inedgeslist", u.inedgesList)
    print(u, "outedgeslist", u.outedgesList,"\n\n")

ec,cn=check_neilsen_reduced(stall)
print( "edges covered", ec,"neilsen reduced =", cn)

#stall=
build_new_labelling(stall,FZ)

reverse_a_z(stall,'z1')
reverse_a_z(stall,'z1')

# Open  new file to see effect of relabelling
with open(testfile+"stall1.gv", "w") as f1:
    f1.write("digraph D {\n") #and write to it
with open(testfile+"stall1.gv", "a") as f1: #then open it in append mode
    f1.write(str(stall)) #and continue to write to it
    f1.write("}")
f1.close()

print(stall.root)
forced_bfs(stall)
print("stall components", stall.components)

for v in stall.vertices:
    print("vertex ", v,"colour, length, time, parent, path",v.colour,v.length,v.time, v.parent,v.path)


print("stall components",stall.components)
print("H subgroup_free_gens", H1.subgroup_free_gens, "H1.subgp_gens", H1.subgp_gens)


for u in stall.vertices:
    print(u, "out_write", u.outedges_write,"\n in_write", u.inedges_write,"\n")
    print(u,"inedgeslist", u.inedgesList,"\n")
    print(u, "outedgeslist", u.outedgesList,"\n\n")

H1.subgroup_free_gens=subgroup_basis(stall)[1]
print("New H subgroup_free_gens", H1.subgroup_free_gens, " and H1.subgp_gens", H1.subgp_gens)
