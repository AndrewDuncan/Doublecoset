from alg2a import * #alg2a imports alg1a 
#from alg1a_backup import *

###freely_reduce tests###
#print(element([]).freely_reduce())
#print(element(['a1','A1','A1','A1','a1']).freely_reduce())
#print(element(['a1','b1','c1','d1','D1','C1','B1','A1','D3','D3']).freely_reduce())
#print(element(['z7','D6','b2','A4','A4']).freely_reduce())
#print(element(['','a1','A1','A1','','A1','a1']).freely_reduce()) #(1)
#print(element(['','a1','','A1','A1','','A1','a1']).freely_reduce())#(2)
#print(element(['','a1','','','A1','A1','','A1','a1']).freely_reduce())

#(1) identity elements are treated as being a unique element and must be removed by another function
#(2) identity elements can block other cancellation so early removal is a good idea
#(3) identity elements do cancel each other out (as ''is just '' in any case)

#freely_reduce seems to work

###inverse tests###

#print(element([]).inverse())
#print(element(['a1']).inverse())
#print(element(['a1','B2','d7','T19']).inverse())
#print(element(['a1','A1','A1','A1','A1']).inverse())

#inverse seems to work, so no problems found with any of the class element

###generators test###

#print(free_group(3,'t').mongens)

#the generators in the free group work as expected
#note that they are now in the initialiser, rather than made using the make_gens function

###is_element tests###

#print(free_group(3,'t').is_element([]))
#print(free_group(3,'t').is_element(['T2']))
#print(free_group(3,'t').is_element(['t1','t1','t2','t3','T3','t2','t2','t1']))

#is_element seems to work, so no problems found with any of the class free_group

###subgroup tests###

h1=['a1','a1','A2','A3','a2','a1']
h2=['a1','a2','A3','A2','a1','a1']
H1=subgroup('H1',[h1,h2])
#H1.make_flower()
type(H1.flower)
print(H1.flower)
